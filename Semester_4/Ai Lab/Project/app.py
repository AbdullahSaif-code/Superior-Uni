from flask import Flask, render_template, request, jsonify
import yaml
import PyPDF2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import os
from werkzeug.utils import secure_filename
import uuid
import time

import gemini_client

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Global variables for models and document storage
embedding_model = None
tokenizer = None
generation_model = None
config = None

# In-memory storage for processed documents (use database in production)
document_store = {}

# In-memory chat sessions per client (keyed by client_id). Each session stores two isolated
# chat histories: 'pdf' and 'ai'. This ensures switching chats does not erase messages.
chat_sessions = {}


def load_config():
    """Load configuration settings from YAML file"""
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config


def load_models():
    """Load all AI models"""
    global embedding_model, tokenizer, generation_model, config
    
    config = load_config()
    
    print("Loading embedding model...")
    embedding_model = SentenceTransformer(config['model_embedding_path'])
    
    print("Loading generation model...")
    tokenizer = AutoTokenizer.from_pretrained(config['model_generation_path'])
    generation_model = AutoModelForSeq2SeqLM.from_pretrained(config['model_generation_path'])
    
    print("All models loaded successfully!")


def extract_text_from_pdf(pdf_path):
    """Extract all text content from PDF file"""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def split_text_into_chunks(text, chunk_size, chunk_overlap):
    """Split text into chunks based on word count"""
    words = text.split()
    chunks = []
    step = chunk_size - chunk_overlap
    
    for i in range(0, len(words), step):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
        if i + chunk_size >= len(words):
            break
    
    return chunks


def create_embeddings(chunks):
    """Convert text chunks into embeddings"""
    embeddings = embedding_model.encode(chunks)
    return embeddings


def find_relevant_chunks(question, chunks, embeddings, top_k):
    """Find the most relevant chunks for a given question"""
    question_embedding = embedding_model.encode([question])[0]
    
    similarities = []
    for chunk_embedding in embeddings:
        similarity = np.dot(question_embedding, chunk_embedding) / (
            np.linalg.norm(question_embedding) * np.linalg.norm(chunk_embedding)
        )
        similarities.append(similarity)
    
    top_k_indices = np.argsort(similarities)[-top_k:][::-1]
    relevant_chunks = [chunks[i] for i in top_k_indices]
    return relevant_chunks


def generate_answer(question, context, answer_length):
    """Generate an answer using Flan-T5-Small"""
    length_mapping = {
        "short": 50,
        "medium": 150,
        "long": 250
    }
    max_length = length_mapping.get(answer_length, 150)
    
    prompt = f"Answer the following question based on the context provided.\n\nContext: {context}\n\nQuestion: {question}\n\nAnswer:"
    
    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
    
    with torch.no_grad():
        outputs = generation_model.generate(
            inputs.input_ids,
            max_length=max_length,
            min_length=30,
            num_beams=4,
            early_stopping=True,
            no_repeat_ngram_size=2
        )
    
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer


# Routes
@app.route('/')
def index():
    """Serve the main chatbot page"""
    return render_template('index.html')


@app.route('/api/upload', methods=['POST'])
def upload_pdf():
    """Handle PDF upload and processing"""
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No file selected'}), 400
    
    if not file.filename.lower().endswith('.pdf'):
        return jsonify({'success': False, 'error': 'Only PDF files are allowed'}), 400
    
    try:
        # Generate unique session ID for this document
        doc_id = str(uuid.uuid4())
        
        # Save the file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], f"{doc_id}_{filename}")
        file.save(filepath)
        
        # Extract text from PDF
        text = extract_text_from_pdf(filepath)
        
        if not text.strip():
            os.remove(filepath)
            return jsonify({'success': False, 'error': 'Could not extract text from PDF'}), 400
        
        # Split into chunks
        chunks = split_text_into_chunks(
            text,
            config['chunk_size'],
            config['chunk_overlap']
        )
        
        # Create embeddings
        embeddings = create_embeddings(chunks)
        
        # Store in document store
        document_store[doc_id] = {
            'filename': filename,
            'chunks': chunks,
            'embeddings': embeddings,
            'filepath': filepath
        }
        
        return jsonify({
            'success': True,
            'doc_id': doc_id,
            'filename': filename,
            'chunks_count': len(chunks),
            'message': f'PDF processed successfully! Created {len(chunks)} chunks.'
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages and generate responses"""
    data = request.get_json()
    
    if not data:
        return jsonify({'success': False, 'error': 'No data provided'}), 400
    
    question = data.get('message', '').strip()
    doc_id = data.get('doc_id', '')
    client_id = data.get('client_id')
    
    if not question:
        return jsonify({'success': False, 'error': 'No question provided'}), 400
    
    if not doc_id or doc_id not in document_store:
        return jsonify({'success': False, 'error': 'Please upload a PDF document first'}), 400
    
    try:
        doc_data = document_store[doc_id]
        
        # Find relevant chunks
        relevant_chunks = find_relevant_chunks(
            question,
            doc_data['chunks'],
            doc_data['embeddings'],
            config['top_k_chunks']
        )
        
        # Combine chunks as context
        context = " ".join(relevant_chunks)
        
        # Generate answer
        answer = generate_answer(
            question,
            context,
            config['answer_length']
        )
        
        # Store chat messages in session if client_id provided
        if client_id:
            sess = chat_sessions.setdefault(client_id, {'pdf': [], 'ai': []})
            sess['pdf'].append({'role': 'user', 'text': question, 'doc_id': doc_id, 'time': time.time()})
            sess['pdf'].append({'role': 'assistant', 'text': answer, 'time': time.time()})

        return jsonify({
            'success': True,
            'answer': answer,
            'relevant_chunks': relevant_chunks
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/status', methods=['GET'])
def status():
    """Check API status and model loading status"""
    return jsonify({
        'status': 'online',
        'models_loaded': embedding_model is not None and generation_model is not None
    })


@app.route('/api/ai_chat', methods=['POST'])
def ai_chat():
    """Handle messages for the AI Chat (Gemini). This is separate from the PDF RAG flow.

    Request JSON: { message: str, client_id: str }
    """
    data = request.get_json()
    if not data:
        return jsonify({'success': False, 'error': 'No data provided'}), 400

    message = data.get('message', '').strip()
    client_id = data.get('client_id')

    if not message:
        return jsonify({'success': False, 'error': 'No message provided'}), 400

    try:
        # Query Gemini via the isolated module
        response_text = gemini_client.query_gemini(message)

        # Store in session
        if client_id:
            sess = chat_sessions.setdefault(client_id, {'pdf': [], 'ai': []})
            sess['ai'].append({'role': 'user', 'text': message, 'time': time.time()})
            sess['ai'].append({'role': 'assistant', 'text': response_text, 'time': time.time()})

        return jsonify({'success': True, 'answer': response_text})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/get_session', methods=['GET'])
def get_session():
    """Return stored chat history for a client_id (both 'pdf' and 'ai')."""
    client_id = request.args.get('client_id')
    if not client_id:
        return jsonify({'success': False, 'error': 'client_id required'}), 400

    sess = chat_sessions.setdefault(client_id, {'pdf': [], 'ai': []})
    return jsonify({'success': True, 'session': sess})


if __name__ == '__main__':
    print("Starting RAG Chatbot API...")
    load_models()
    app.run(debug=True, host='0.0.0.0', port=5000)

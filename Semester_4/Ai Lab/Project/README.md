# RAG-based AI Assistant

A fully offline RAG (Retrieval-Augmented Generation) chatbot built with Streamlit that allows you to upload PDF documents and ask questions about them.

## Features

- **Offline Operation**: Works completely offline using local models
- **PDF Processing**: Upload and extract text from PDF documents
- **Smart Chunking**: Splits text into overlapping chunks for better context
- **Semantic Search**: Uses MiniLM-L6-v2 embeddings and cosine similarity to find relevant information
- **Answer Generation**: Generates natural answers using Flan-T5-Small
- **Easy Configuration**: Customize behavior through `config.yaml`

## Models Used

1. **all-MiniLM-L6-v2**: For creating text embeddings
2. **flan-t5-small**: For generating natural language answers

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Ensure the models are in the `models` folder:
   - `models/all-MiniLM-L6-v2/`
   - `models/flan-t5-small/`

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Upload a PDF document
3. Click "Process PDF" to analyze the document
4. Ask questions in the text input box
5. Click "Generate Answer" to get AI-powered responses

## Configuration

Edit `config.yaml` to customize:

- `chunk_size`: Number of words per chunk (default: 200)
- `chunk_overlap`: Overlap between chunks (default: 40)
- `top_k_chunks`: Number of relevant chunks to retrieve (default: 2)
- `answer_length`: Answer length - "short", "medium", or "long" (default: "medium")
- Model paths

## How It Works

1. **PDF Upload**: User uploads a PDF document
2. **Text Extraction**: Extract text from all pages
3. **Chunking**: Split text into overlapping chunks of 200 words
4. **Embedding**: Convert each chunk into a vector using MiniLM-L6-v2
5. **Question Processing**: Convert user question into an embedding
6. **Similarity Search**: Find top 2 most relevant chunks using cosine similarity
7. **Answer Generation**: Generate a medium-length answer using Flan-T5-Small with the relevant chunks as context

## Requirements

- Python 3.7+
- See `requirements.txt` for package dependencies

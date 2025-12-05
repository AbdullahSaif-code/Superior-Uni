// Global state
let currentDocId = null;
let isProcessing = false;
let clientId = null;
let activeChat = 'pdf'; // 'pdf' or 'ai'
let chatHistories = { pdf: [], ai: [] };

// DOM Elements
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const fileInfo = document.getElementById('fileInfo');
const fileName = document.getElementById('fileName');
const removeFile = document.getElementById('removeFile');
const uploadProgress = document.getElementById('uploadProgress');
const progressFill = document.getElementById('progressFill');
const progressText = document.getElementById('progressText');
const uploadStatus = document.getElementById('uploadStatus');
const chatForm = document.getElementById('chatForm');
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
const chatMessages = document.getElementById('chatMessages');
const inputHint = document.getElementById('inputHint');
const statusDot = document.getElementById('statusDot');
const statusText = document.getElementById('statusText');
const menuToggle = document.getElementById('menuToggle');
const sidebar = document.querySelector('.sidebar');
const contextModal = document.getElementById('contextModal');
const modalClose = document.getElementById('modalClose');
const modalBody = document.getElementById('modalBody');
const cardPdf = document.getElementById('cardPdf');
const cardAi = document.getElementById('cardAi');
const headerTitle = document.getElementById('headerTitle');
const headerSubtitle = document.getElementById('headerSubtitle');
const uploadSection = document.querySelector('.upload-section');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    checkAPIStatus();
    setupEventListeners();
    createOverlay();
    initClientId();
    loadSession();
    updateHeaderForActiveChat();
});

// Create sidebar overlay for mobile
function createOverlay() {
    const overlay = document.createElement('div');
    overlay.className = 'sidebar-overlay';
    overlay.id = 'sidebarOverlay';
    document.body.appendChild(overlay);
    
    overlay.addEventListener('click', () => {
        sidebar.classList.remove('active');
        overlay.classList.remove('active');
    });
}

// Setup event listeners
function setupEventListeners() {
    // File upload
    uploadArea.addEventListener('click', () => fileInput.click());
    fileInput.addEventListener('change', handleFileSelect);
    uploadArea.addEventListener('dragover', handleDragOver);
    uploadArea.addEventListener('dragleave', handleDragLeave);
    uploadArea.addEventListener('drop', handleDrop);
    removeFile.addEventListener('click', resetUpload);
    
    // Chat
    chatForm.addEventListener('submit', handleSubmit);
    messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSubmit(e);
        }
    });
    
    // Mobile menu
    menuToggle.addEventListener('click', toggleSidebar);
    
    // Modal
    modalClose.addEventListener('click', closeModal);
    contextModal.addEventListener('click', (e) => {
        if (e.target === contextModal) closeModal();
    });

    // Chat card switching
    cardPdf.addEventListener('click', () => switchChat('pdf'));
    cardAi.addEventListener('click', () => switchChat('ai'));
}


function initClientId(){
    clientId = localStorage.getItem('chat_client_id');
    if (!clientId){
        clientId = 'cli-' + Date.now() + '-' + Math.floor(Math.random()*100000);
        localStorage.setItem('chat_client_id', clientId);
    }
}

async function loadSession(){
    if (!clientId) return;
    try{
        const res = await fetch(`/api/get_session?client_id=${encodeURIComponent(clientId)}`);
        const data = await res.json();
        if (data.success && data.session){
            chatHistories = data.session;
        }
    }catch(e){
        console.warn('Could not load session', e);
    }
    renderChatHistory();
}

function switchChat(chat){
    if (chat !== 'pdf' && chat !== 'ai') return;
    activeChat = chat;
    // UI active class
    if (chat === 'pdf'){
        cardPdf.classList.add('active');
        cardAi.classList.remove('active');
        uploadSection.style.display = 'block';
    } else {
        cardAi.classList.add('active');
        cardPdf.classList.remove('active');
        uploadSection.style.display = 'none';
    }
    updateHeaderForActiveChat();
    renderChatHistory();
    // Enable/disable chat input depending on active chat
    if (activeChat === 'ai'){
        messageInput.placeholder = 'Ask general questions to the AI Chatbot...';
        enableChat();
    } else {
        messageInput.placeholder = 'Ask a question about your document...';
        if (currentDocId) enableChat(); else disableChat();
    }
}

function updateHeaderForActiveChat(){
    if (activeChat === 'ai'){
        headerTitle.textContent = 'AI Chatbot';
        headerSubtitle.textContent = 'General-purpose assistant powered by Gemini';
    } else {
        headerTitle.textContent = 'AI Document Assistant';
        headerSubtitle.textContent = 'Ask questions about your uploaded PDF document';
    }
}

// Check API status
async function checkAPIStatus() {
    try {
        const response = await fetch('/api/status');
        const data = await response.json();
        
        if (data.status === 'online' && data.models_loaded) {
            statusDot.classList.add('online');
            statusDot.classList.remove('offline');
            statusText.textContent = 'Models Ready';
        } else {
            statusDot.classList.remove('online');
            statusDot.classList.add('offline');
            statusText.textContent = 'Loading Models...';
        }
    } catch (error) {
        statusDot.classList.remove('online');
        statusDot.classList.add('offline');
        statusText.textContent = 'API Offline';
    }
}

// File handling
function handleDragOver(e) {
    e.preventDefault();
    uploadArea.classList.add('drag-over');
}

function handleDragLeave(e) {
    e.preventDefault();
    uploadArea.classList.remove('drag-over');
}

function handleDrop(e) {
    e.preventDefault();
    uploadArea.classList.remove('drag-over');
    
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        const file = files[0];
        if (file.type === 'application/pdf') {
            processFile(file);
        } else {
            showUploadStatus('Please upload a PDF file', 'error');
        }
    }
}

function handleFileSelect(e) {
    const file = e.target.files[0];
    if (file) {
        processFile(file);
    }
}

async function processFile(file) {
    if (isProcessing) return;
    isProcessing = true;
    
    // Show file info
    uploadArea.style.display = 'none';
    fileInfo.style.display = 'flex';
    fileName.textContent = file.name;
    
    // Show progress
    uploadProgress.style.display = 'block';
    uploadStatus.style.display = 'none';
    uploadStatus.className = 'upload-status';
    
    // Simulate progress
    let progress = 0;
    const progressInterval = setInterval(() => {
        progress += Math.random() * 15;
        if (progress > 90) progress = 90;
        progressFill.style.width = `${progress}%`;
        progressText.textContent = `Processing... ${Math.round(progress)}%`;
    }, 300);
    
    // Upload file
    const formData = new FormData();
    formData.append('file', file);
    
    try {
        const response = await fetch('/api/upload', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        clearInterval(progressInterval);
        progressFill.style.width = '100%';
        progressText.textContent = 'Complete!';
        
        setTimeout(() => {
            uploadProgress.style.display = 'none';
            
            if (data.success) {
                currentDocId = data.doc_id;
                showUploadStatus(data.message, 'success');
                // Add a system message into PDF chat history
                chatHistories.pdf.push({ role: 'system', text: `Processed document "${data.filename}" (${data.chunks_count} chunks)` });
                enableChat();
                clearWelcomeMessage();
                addBotMessage(`I've processed your document "${data.filename}". Created ${data.chunks_count} text chunks for analysis. Feel free to ask me any questions about the content!`, null, 'pdf');
            } else {
                showUploadStatus(data.error || 'Upload failed', 'error');
                resetUpload();
            }
        }, 500);
        
    } catch (error) {
        clearInterval(progressInterval);
        uploadProgress.style.display = 'none';
        showUploadStatus('Failed to upload file. Please try again.', 'error');
        resetUpload();
    }
    
    isProcessing = false;
}

function resetUpload() {
    currentDocId = null;
    uploadArea.style.display = 'block';
    fileInfo.style.display = 'none';
    uploadProgress.style.display = 'none';
    uploadStatus.style.display = 'none';
    uploadStatus.className = 'upload-status';
    fileInput.value = '';
    progressFill.style.width = '0%';
    disableChat();
}

function showUploadStatus(message, type) {
    uploadStatus.textContent = message;
    uploadStatus.className = `upload-status ${type}`;
    uploadStatus.style.display = 'block';
}

// Chat functions
function enableChat() {
    messageInput.disabled = false;
    sendButton.disabled = false;
    inputHint.innerHTML = '<i class="fas fa-info-circle"></i> Press Enter to send your message';
}

function disableChat() {
    messageInput.disabled = true;
    sendButton.disabled = true;
    inputHint.innerHTML = '<i class="fas fa-info-circle"></i> Upload a PDF document to start chatting';
}

function clearWelcomeMessage() {
    const welcome = chatMessages.querySelector('.welcome-message');
    if (welcome) {
        welcome.remove();
    }
}

async function handleSubmit(e) {
    e.preventDefault();
    const message = messageInput.value.trim();
    if (!message) return;

    // Add user message to current chat
    addUserMessage(message);
    messageInput.value = '';

    // Show typing indicator
    const typingId = showTypingIndicator();

    try {
        if (activeChat === 'pdf'){
            if (!currentDocId) {
                removeTypingIndicator(typingId);
                addBotMessage('Please upload a PDF document first.', null, 'pdf');
                return;
            }

            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: message, doc_id: currentDocId, client_id: clientId })
            });

            const data = await response.json();
            removeTypingIndicator(typingId);

            if (data.success) {
                addBotMessage(data.answer, data.relevant_chunks, 'pdf');
            } else {
                addBotMessage(`Sorry, I encountered an error: ${data.error}`, null, 'pdf');
            }

        } else {
            // AI chat
            const response = await fetch('/api/ai_chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: message, client_id: clientId })
            });

            const data = await response.json();
            removeTypingIndicator(typingId);

            if (data.success) {
                addBotMessage(data.answer, null, 'ai');
            } else {
                addBotMessage(`Sorry, I encountered an error: ${data.error}`, null, 'ai');
            }
        }

    } catch (error) {
        removeTypingIndicator(typingId);
        addBotMessage('Sorry, I encountered a network error. Please try again.', null, activeChat);
    }
}

function addUserMessage(text) {
    // Store in history for active chat
    chatHistories[activeChat].push({ role: 'user', text: text, time: Date.now() });
    // Render to DOM
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message user';
    messageDiv.innerHTML = `
        <div class="message-avatar">
            <i class="fas fa-user"></i>
        </div>
        <div class="message-content">
            <div class="message-bubble">${escapeHtml(text)}</div>
        </div>
    `;
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

function addBotMessage(text, chunks = null, targetChat = null) {
    const t = targetChat || activeChat;
    // Store in history
    chatHistories[t].push({ role: 'assistant', text: text, chunks: chunks || null, time: Date.now() });

    // If the bot message belongs to the currently visible chat, render it
    if (t !== activeChat) return;

    const messageDiv = document.createElement('div');
    messageDiv.className = 'message bot';
    
    let actionsHtml = '';
    if (chunks && chunks.length > 0) {
        actionsHtml = `
            <div class="message-actions">
                <button class="context-button">
                    <i class="fas fa-quote-left"></i> View Context
                </button>
            </div>
        `;
    }
    
    // Format text to remove markdown for AI chat responses
    const displayText = formatTextForDisplay(text);
    
    messageDiv.innerHTML = `
        <div class="message-avatar">
            <i class="fas fa-robot"></i>
        </div>
        <div class="message-content">
            <div class="message-bubble">${displayText}</div>
            ${actionsHtml}
        </div>
    `;
    
    // Store chunks data on the button
    if (chunks && chunks.length > 0) {
        const contextBtn = messageDiv.querySelector('.context-button');
        contextBtn.onclick = () => showContext(chunks);
    }
    
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

function renderChatHistory(){
    // Clear messages
    chatMessages.innerHTML = '';
    const history = chatHistories[activeChat] || [];
    if (!history || history.length === 0){
        // Show welcome message only on pdf chat when empty
        if (activeChat === 'pdf'){
            const welcomeDiv = document.createElement('div');
            welcomeDiv.className = 'welcome-message';
            welcomeDiv.innerHTML = `
                <div class="welcome-icon"><i class="fas fa-comments"></i></div>
                <h2>Welcome to RAG AI Assistant!</h2>
                <p>Upload a PDF document to get started. Once uploaded, you can ask any questions about the document content.</p>
            `;
            chatMessages.appendChild(welcomeDiv);
            disableChat();
        } else {
            const info = document.createElement('div');
            info.className = 'welcome-message';
            info.innerHTML = `<h2>AI Chatbot</h2><p>Ask general-purpose questions powered by Gemini.</p>`;
            chatMessages.appendChild(info);
            enableChat();
        }
        return;
    }

    // Render each message
    history.forEach(item => {
        if (item.role === 'user'){
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message user';
            messageDiv.innerHTML = `
                <div class="message-avatar"><i class="fas fa-user"></i></div>
                <div class="message-content"><div class="message-bubble">${escapeHtml(item.text)}</div></div>
            `;
            chatMessages.appendChild(messageDiv);
        } else if (item.role === 'assistant' || item.role === 'system'){
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message bot';
            let actionsHtml = '';
            if (item.chunks && item.chunks.length > 0){
                actionsHtml = `<div class="message-actions"><button class="context-button"> <i class="fas fa-quote-left"></i> View Context</button></div>`;
            }
            const displayText = formatTextForDisplay(item.text);
            messageDiv.innerHTML = `
                <div class="message-avatar"><i class="fas fa-robot"></i></div>
                <div class="message-content"><div class="message-bubble">${displayText}</div>${actionsHtml}</div>
            `;
            if (item.chunks && item.chunks.length > 0){
                const contextBtn = messageDiv.querySelector('.context-button');
                contextBtn.onclick = () => showContext(item.chunks);
            }
            chatMessages.appendChild(messageDiv);
        }
    });
    scrollToBottom();
}

function showTypingIndicator() {
    const id = 'typing-' + Date.now();
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message bot';
    typingDiv.id = id;
    typingDiv.innerHTML = `
        <div class="message-avatar">
            <i class="fas fa-robot"></i>
        </div>
        <div class="message-content">
            <div class="typing-indicator">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    `;
    chatMessages.appendChild(typingDiv);
    scrollToBottom();
    return id;
}

function removeTypingIndicator(id) {
    const typing = document.getElementById(id);
    if (typing) {
        typing.remove();
    }
}

function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function formatTextForDisplay(text) {
    // Remove markdown formatting
    let formatted = text;
    
    // Remove bold (**text** or __text__)
    formatted = formatted.replace(/\*\*([^*]+)\*\*/g, '$1');
    formatted = formatted.replace(/__([^_]+)__/g, '$1');
    
    // Remove italic (*text* or _text_)
    formatted = formatted.replace(/\*([^*]+)\*/g, '$1');
    formatted = formatted.replace(/_([^_]+)_/g, '$1');
    
    // Remove headers (# ## ###)
    formatted = formatted.replace(/^#{1,6}\s+/gm, '');
    
    // Remove code blocks (```code```)
    formatted = formatted.replace(/```[\s\S]*?```/g, (match) => {
        return match.replace(/```\w*\n?/g, '').replace(/```/g, '');
    });
    
    // Remove inline code (`code`)
    formatted = formatted.replace(/`([^`]+)`/g, '$1');
    
    // Remove links [text](url)
    formatted = formatted.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1');
    
    // Convert line breaks properly
    formatted = formatted.replace(/\n/g, '<br>');
    
    return formatted;
}

// Modal functions
function showContext(chunks) {
    modalBody.innerHTML = chunks.map((chunk, index) => `
        <div class="context-chunk">
            <h4>Chunk ${index + 1}</h4>
            <p>${escapeHtml(chunk)}</p>
        </div>
    `).join('');
    contextModal.classList.add('active');
}

function closeModal() {
    contextModal.classList.remove('active');
}

// Mobile sidebar toggle
function toggleSidebar() {
    sidebar.classList.toggle('active');
    document.getElementById('sidebarOverlay').classList.toggle('active');
}

// Expose showContext to global scope for onclick handlers
window.showContext = showContext;

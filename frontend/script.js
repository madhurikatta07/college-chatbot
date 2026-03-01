const chatMessages = document.getElementById('chat-messages');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

const API_URL = 'http://localhost:5000/chat';

function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function createMessageHTML(text, sender) {
    const isUser = sender === 'user';
    const msgClass = isUser ? 'user-message' : 'bot-message';
    
    const wrapper = document.createElement('div');
    wrapper.className = `message-wrapper ${sender}`;
    
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${msgClass}`;
    msgDiv.textContent = text;
    
    wrapper.appendChild(msgDiv);
    return wrapper;
}

function createTypingIndicatorHTML() {
    const wrapper = document.createElement('div');
    wrapper.className = 'message-wrapper bot';
    wrapper.id = 'typing-indicator-wrapper';
    
    const indicator = document.createElement('div');
    indicator.className = 'typing-indicator';
    indicator.innerHTML = '<div class="dot"></div><div class="dot"></div><div class="dot"></div>';
    
    wrapper.appendChild(indicator);
    return wrapper;
}

async function sendMessage() {
    const text = userInput.value.trim();
    if (!text) return;

    // 1. Add User Message
    chatMessages.appendChild(createMessageHTML(text, 'user'));
    userInput.value = '';
    userInput.focus();
    scrollToBottom();

    // 2. Add Typing Indicator
    const typingIndicator = createTypingIndicatorHTML();
    chatMessages.appendChild(typingIndicator);
    scrollToBottom();

    // 3. Fetch from API
    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ msg: text })
        });
        
        const data = await response.json();
        
        // Remove typing indicator safely
        if (chatMessages.contains(typingIndicator)) {
            chatMessages.removeChild(typingIndicator);
        }
        
        if (data.error) {
            throw new Error(data.error);
        }

        // 4. Render Bot Response
        chatMessages.appendChild(createMessageHTML(data.response, 'bot'));
        
        // Log details natively
        console.log(`[Chatbot Analytics] Intent: ${data.predicted_intent} | Confidence: ${(data.confidence * 100).toFixed(1)}%`);
        
    } catch (error) {
        if (chatMessages.contains(typingIndicator)) {
            chatMessages.removeChild(typingIndicator);
        }
        
        chatMessages.appendChild(createMessageHTML("Sorry, the server is unreachable right now. Please try again later.", 'bot'));
        console.error("Chatbot API Error:", error);
    }
    
    scrollToBottom();
}

// Event Listeners
sendBtn.addEventListener('click', sendMessage);

userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Auto-focus input on load
window.onload = () => userInput.focus();

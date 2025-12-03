"""Chatbot response logic and interaction handling."""

import random
from config import BOT_NAME


class Chatbot:
    """Handles chatbot responses based on user input."""
    
    def __init__(self):
        """Initialize chatbot with response templates."""
        self.name = BOT_NAME
        self.responses = {
            'greeting': [
                "Hello! How can I help you today?",
                "Hi there! What's on your mind?",
                "Hey! Feel free to share your thoughts with me."
            ],
            'positive': [
                "I'm glad to hear that!",
                "That's wonderful to know!",
                "Great! I'm happy for you."
            ],
            'negative': [
                "I understand your concern. I'll make sure it's addressed.",
                "I'm sorry to hear that. Let me help you with this.",
                "I appreciate you sharing this. How can I improve things?"
            ],
            'neutral': [
                "I see. Tell me more about that.",
                "Interesting. What else would you like to discuss?",
                "I understand. Please continue."
            ],
            'farewell': [
                "Thank you for chatting with me! Take care!",
                "Goodbye! Have a great day!",
                "See you later! Feel free to come back anytime."
            ],
            'default': [
                "I'm listening. Please go on.",
                "Tell me more about that.",
                "I appreciate you sharing this with me.",
                "That's interesting. What else?"
            ]
        }
    
    def generate_response(self, user_input, sentiment_label=None):
        """
        Generate appropriate response based on input and sentiment.
        
        Args:
            user_input (str): User's message
            sentiment_label (str, optional): Sentiment of user's message
            
        Returns:
            str: Bot's response
        """
        user_input_lower = user_input.lower()
        
        # Check for farewells (specific responses)
        if 'goodbye' in user_input_lower:
            return "See you later! Feel free to come back anytime."
        if 'bye' in user_input_lower and 'goodbye' not in user_input_lower:
            return "Goodbye! Have a great day!"
        if 'see you' in user_input_lower:
            return "See you later! Feel free to come back anytime."
        
        # Check for greetings (always return same response)
        if any(word in user_input_lower for word in ['hello', 'hi', 'hey', 'greetings']):
            return "Hi there! What's on your mind?"
        
        # Sentiment-based responses (specific responses)
        if sentiment_label:
            if sentiment_label == 'Positive':
                return "Great! I'm happy for you."
            elif sentiment_label == 'Negative':
                return "I understand your concern. I'll make sure it's addressed."
            elif sentiment_label == 'Neutral':
                return "I see. Tell me more about that."
        
        # Default response
        return "Tell me more about that."
    
    def get_welcome_message(self):
        """Get welcome message for chatbot."""
        return f"""
╔══════════════════════════════════════════════╗
║   Welcome to {self.name}!                   ║
║   I'm here to chat and understand your mood  ║ 
║   Type 'quit' or 'exit' to end conversation  ║ 
╚══════════════════════════════════════════════╝
"""

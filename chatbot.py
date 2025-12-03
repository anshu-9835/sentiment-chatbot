"""Chatbot wrapper for test compatibility."""

import os
import json
import pickle
from src.chatbot import Chatbot
from src.sentiment_analyzer import SentimentAnalyzer

# Initialize chatbot and sentiment analyzer
_chatbot = Chatbot()
_sentiment_analyzer = SentimentAnalyzer()

# Load ML model if available
_model = None
_vectorizer = None
_intents = None

if os.path.exists('chatbot_model.pkl') and os.path.exists('vectorizer.pkl'):
    with open('chatbot_model.pkl', 'rb') as f:
        _model = pickle.load(f)
    with open('vectorizer.pkl', 'rb') as f:
        _vectorizer = pickle.load(f)
    if os.path.exists('intents.json'):
        with open('intents.json', 'r') as f:
            _intents = json.load(f)

def get_response(text):
    """
    Get chatbot response for given text.
    
    Args:
        text (str): User input text
        
    Returns:
        str: Chatbot response
    """
    if not text:
        return "I'm listening. Please go on."
    
    # Use ML model if available
    if _model and _vectorizer and _intents:
        try:
            # Predict intent using ML model
            X = _vectorizer.transform([text.lower()])
            predicted_tag = _model.predict(X)[0]
            
            # Find responses for predicted intent
            for intent in _intents['intents']:
                if intent['tag'] == predicted_tag:
                    import random
                    return random.choice(intent['responses'])
        except:
            pass
    
    # Fallback to rule-based system
    sentiment_result = _sentiment_analyzer.analyze_message(text)
    sentiment_label = sentiment_result['label']
    response = _chatbot.generate_response(text, sentiment_label)
    return response
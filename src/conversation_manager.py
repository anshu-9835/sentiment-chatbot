"""Manages conversation history and message tracking."""

from datetime import datetime
import json


class ConversationManager:
    """Handles storage and retrieval of conversation history."""
    
    def __init__(self):
        """Initialize conversation manager."""
        self.messages = []
        self.start_time = datetime.now()
    
    def add_message(self, sender, text, sentiment=None):
        """
        Add a message to conversation history.
        
        Args:
            sender (str): 'user' or 'bot'
            text (str): Message content
            sentiment (dict, optional): Sentiment analysis results
        """
        message = {
            'sender': sender,
            'text': text,
            'timestamp': datetime.now().isoformat(),
            'sentiment': sentiment
        }
        self.messages.append(message)
    
    def get_user_messages(self):
        """Get only user messages."""
        return [msg['text'] for msg in self.messages if msg['sender'] == 'user']
    
    def get_all_messages(self):
        """Get all messages in conversation."""
        return self.messages
    
    def get_conversation_duration(self):
        """Calculate conversation duration."""
        if not self.messages:
            return 0
        return (datetime.now() - self.start_time).total_seconds()
    
    def save_to_file(self, filename='data/conversation_history.json'):
        """Save conversation to JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump({
                    'messages': self.messages,
                    'start_time': self.start_time.isoformat(),
                    'duration_seconds': self.get_conversation_duration()
                }, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving conversation: {e}")
            return False
    
    def clear(self):
        """Clear conversation history."""
        self.messages = []
        self.start_time = datetime.now()

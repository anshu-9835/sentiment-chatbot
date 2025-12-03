"""Sentiment analysis wrapper for test compatibility."""

from src.sentiment_analyzer import SentimentAnalyzer

# Initialize the sentiment analyzer
_analyzer = SentimentAnalyzer()

def get_sentiment(text):
    """
    Get sentiment analysis for a text.
    
    Args:
        text (str): Text to analyze
        
    Returns:
        dict: Contains 'sentiment' key with label
    """
    if not text:
        return {'sentiment': 'Neutral'}
    
    result = _analyzer.analyze_message(text)
    return {'sentiment': result['label']}

def analyze_conversation(messages):
    """
    Analyze overall conversation sentiment.
    
    Args:
        messages (list): List of messages
        
    Returns:
        dict or None: Contains 'sentiment' key or None if empty
    """
    if not messages:
        return None
    
    result = _analyzer.analyze_conversation(messages)
    return {'sentiment': result['label']}
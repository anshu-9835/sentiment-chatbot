"""Sentiment analysis module using VADER and TextBlob."""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from config import POSITIVE_THRESHOLD, NEGATIVE_THRESHOLD


class SentimentAnalyzer:
    """Handles sentiment analysis for text messages."""
    
    def __init__(self, method='vader'):
        """
        Initialize sentiment analyzer.
        
        Args:
            method (str): 'vader' or 'textblob'
        """
        self.method = method
        if method == 'vader':
            self.analyzer = SentimentIntensityAnalyzer()
    
    def analyze_message(self, text):
        """
        Analyze sentiment of a single message.
        
        Args:
            text (str): The message to analyze
            
        Returns:
            dict: Contains score, label, and detailed scores
        """
        if self.method == 'vader':
            return self._analyze_vader(text)
        else:
            return self._analyze_textblob(text)
    
    def _analyze_vader(self, text):
        """Analyze using VADER sentiment."""
        scores = self.analyzer.polarity_scores(text)
        compound = scores['compound']
        
        # Determine sentiment label
        if compound >= POSITIVE_THRESHOLD:
            label = 'Positive'
        elif compound <= NEGATIVE_THRESHOLD:
            label = 'Negative'
        else:
            label = 'Neutral'
        
        return {
            'score': compound,
            'label': label,
            'detailed_scores': {
                'positive': scores['pos'],
                'negative': scores['neg'],
                'neutral': scores['neu']
            }
        }
    
    def _analyze_textblob(self, text):
        """Analyze using TextBlob sentiment."""
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        
        # Determine sentiment label
        if polarity >= POSITIVE_THRESHOLD:
            label = 'Positive'
        elif polarity <= NEGATIVE_THRESHOLD:
            label = 'Negative'
        else:
            label = 'Neutral'
        
        return {
            'score': polarity,
            'label': label,
            'detailed_scores': {
                'polarity': polarity,
                'subjectivity': blob.sentiment.subjectivity
            }
        }
    
    def analyze_conversation(self, messages):
        """
        Analyze overall sentiment of entire conversation.
        
        Args:
            messages (list): List of user messages
            
        Returns:
            dict: Overall sentiment analysis
        """
        if not messages:
            return {'score': 0, 'label': 'Neutral', 'message_count': 0, 'description': 'No messages', 'trend': 'stable'}
        
        scores = [self.analyze_message(msg)['score'] for msg in messages]
        avg_score = sum(scores) / len(scores)
        
        # Determine overall label
        if avg_score >= POSITIVE_THRESHOLD:
            label = 'Positive'
            description = 'general satisfaction'
        elif avg_score <= NEGATIVE_THRESHOLD:
            label = 'Negative'
            description = 'general dissatisfaction'
        else:
            label = 'Neutral'
            description = 'balanced sentiment'
        
        return {
            'score': avg_score,
            'label': label,
            'description': description,
            'message_count': len(messages),
            'trend': self._calculate_trend(scores)
        }
    
    def _calculate_trend(self, scores):
        """Calculate sentiment trend across conversation."""
        if len(scores) < 2:
            return 'stable'
        
        # Compare first half vs second half
        mid = len(scores) // 2
        first_half_avg = sum(scores[:mid]) / mid
        second_half_avg = sum(scores[mid:]) / (len(scores) - mid)
        
        diff = second_half_avg - first_half_avg
        
        if diff > 0.1:
            return 'improving'
        elif diff < -0.1:
            return 'declining'
        else:
            return 'stable'

"""Configuration settings for the chatbot."""

import logging

# Logging configuration
LOG_LEVEL = logging.INFO
LOG_FILE = "chatbot.log"
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


# Sentiment thresholds
POSITIVE_THRESHOLD = 0.3
NEGATIVE_THRESHOLD = -0.3
SENTIMENT_METHOD = 'vader'

# Chatbot settings
BOT_NAME = "SentimentBot"
EXIT_COMMANDS = ['quit', 'exit', 'bye', 'goodbye']

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

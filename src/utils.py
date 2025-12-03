"""Utility functions for the chatbot application."""

from config import Colors


def print_colored(text, color):
    """Print colored text to terminal."""
    print(f"{color}{text}{Colors.ENDC}")


def format_sentiment_output(message, sentiment):
    """Format sentiment analysis output for display."""
    score = sentiment['score']
    label = sentiment['label']
    
    # Choose color based on sentiment
    if label == 'Positive':
        color = Colors.OKGREEN
    elif label == 'Negative':
        color = Colors.FAIL
    else:
        color = Colors.WARNING
    
    return f"{color}→ Sentiment: {label} (score: {score:.3f}){Colors.ENDC}"


def display_conversation_summary(conversation_analysis, duration):
    """Display final conversation summary."""
    print("\n" + "="*60)
    print_colored("CONVERSATION SUMMARY", Colors.HEADER + Colors.BOLD)
    print("="*60)
    print(f"Duration: {duration:.1f} seconds")
    print(f"Total messages analyzed: {conversation_analysis['message_count']}")
    print(f"Overall sentiment: {conversation_analysis['label']}")
    print(f"Average score: {conversation_analysis['score']:.3f}")
    print(f"Sentiment description: {conversation_analysis['description']}")
    print(f"Mood trend: {conversation_analysis['trend']}")
    print("="*60 + "\n")


def display_tier2_message_analysis(messages):
    """Display individual message sentiments (Tier 2)."""
    print("\n" + "-"*60)
    print_colored("MESSAGE-LEVEL SENTIMENT ANALYSIS (Tier 2)", Colors.HEADER)
    print("-"*60)
    
    for msg in messages:
        if msg['sender'] == 'user' and msg['sentiment']:
            sentiment = msg['sentiment']
            print(f"\nUser: \"{msg['text']}\"")
            print(format_sentiment_output(msg['text'], sentiment))
    
    print("-"*60 + "\n")

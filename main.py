"""Main entry point for the sentiment analysis chatbot."""

import os
from src.chatbot import Chatbot
from src.sentiment_analyzer import SentimentAnalyzer
from src.conversation_manager import ConversationManager
from src.utils import (
    print_colored, 
    format_sentiment_output,
    display_conversation_summary,
    display_tier2_message_analysis
)
from config import Colors, EXIT_COMMANDS


def main():
    """Run the chatbot application."""
    # Initialize components
    chatbot = Chatbot()
    sentiment_analyzer = SentimentAnalyzer(method='vader')
    conversation = ConversationManager()
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Display welcome message
    print(chatbot.get_welcome_message())
    
    # Main conversation loop
    while True:
        # Get user input
        user_input = input(f"{Colors.OKBLUE}You: {Colors.ENDC}").strip()
        
        if not user_input:
            continue
        
        # Check for exit commands
        if user_input.lower() in EXIT_COMMANDS:
            print_colored(f"\n{chatbot.name}: Thank you for chatting! Analyzing conversation...\n", 
                         Colors.OKGREEN)
            break
        
        # TIER 2: Analyze sentiment of user message
        sentiment = sentiment_analyzer.analyze_message(user_input)
        
        # Store user message with sentiment
        conversation.add_message('user', user_input, sentiment)
        
        # TIER 2: Display sentiment for this message
        print(format_sentiment_output(user_input, sentiment))
        
        # Generate and display bot response
        bot_response = chatbot.generate_response(user_input, sentiment['label'])
        print_colored(f"{chatbot.name}: {bot_response}\n", Colors.OKGREEN)
        
        # Store bot response
        conversation.add_message('bot', bot_response)
    
    # TIER 2: Display all message-level sentiments
    display_tier2_message_analysis(conversation.get_all_messages())
    
    # TIER 1: Analyze overall conversation sentiment
    user_messages = conversation.get_user_messages()
    conversation_sentiment = sentiment_analyzer.analyze_conversation(user_messages)
    
    # Display conversation summary
    duration = conversation.get_conversation_duration()
    display_conversation_summary(conversation_sentiment, duration)
    
    # Save conversation to file
    if conversation.save_to_file():
        print_colored("✓ Conversation saved to data/conversation_history.json", Colors.OKGREEN)
    
    print_colored(f"Final Output: Overall conversation sentiment: {conversation_sentiment['label']} – {conversation_sentiment['description']}", 
                 Colors.BOLD)


if __name__ == "__main__":
    main()

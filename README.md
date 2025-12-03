# Sentiment Analysis Chatbot

This project is a command-line chatbot that analyzes the sentiment of user input in real-time. It uses VADER (Valence Aware Dictionary and sEntiment Reasoner) for sentiment analysis and provides a response based on the detected sentiment. The chatbot also tracks the conversation and provides a summary of the overall sentiment at the end of the session.

## Features

- **Real-time Sentiment Analysis:** Analyzes the sentiment of each user message (positive, negative, neutral).
- **Dynamic Responses:** The chatbot's responses are tailored to the sentiment of the user's message.
- **Conversation Summary:** At the end of the conversation, it provides an overall sentiment analysis, including a score, label, and trend (improving, declining, or stable).
- **Conversation History:** Saves the full conversation history to a JSON file.

## Project Structure

```
sentiment-chatbot/
│
├── .gitignore
├── chatbot.py
├── config.py
├── intents.json
├── main.py
├── README.md
├── requirements.txt
├── runtest.py
├── sentiment.py
│
├── data/
│   └── conversation_history.json
│
└── src/
    ├── __init__.py
    ├── chatbot.py
    ├── conversation_manager.py
    ├── sentiment_analyzer.py
    └── utils.py
```

### File Descriptions

- **`main.py`**: The main entry point to run the chatbot.
- **`config.py`**: Contains configuration variables such as bot name, sentiment thresholds, and exit commands.
- **`requirements.txt`**: A list of Python packages required to run the project.
- **`src/chatbot.py`**: Handles the chatbot's response logic.
- **`src/sentiment_analyzer.py`**: Performs sentiment analysis on user messages and conversations.
- **`src/conversation_manager.py`**: Manages the conversation history.
- **`src/utils.py`**: Contains utility functions for colored printing and formatting.
- **`data/`**: Directory where conversation history is stored.

## How to Run the Project

### Prerequisites

- Python 3.x
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/sentiment-chatbot.git
cd sentiment-chatbot
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Run the Chatbot

Execute the `main.py` script to start the chatbot:

```bash
python main.py
```

The chatbot will greet you, and you can start a conversation. To end the conversation, type `quit` or `exit`.

## Example Usage

```
Welcome to SentBot!
I'm here to chat and understand your mood
Type 'quit' or 'exit' to end conversation

You: I am very happy today!
Sentiment: Positive (Score: 0.61)
SentBot: Great! I'm happy for you.

You: This is a terrible experience.
Sentiment: Negative (Score: -0.52)
SentBot: I understand your concern. I'll make sure it's addressed.

You: quit
SentBot: Thank you for chatting! Analyzing conversation...

--- Conversation Analysis ---
Overall Sentiment: Neutral
Description: balanced sentiment
Duration: 30.5s
Trend: declining
✓ Conversation saved to data/conversation_history.json
Final Output: Overall conversation sentiment: Neutral – balanced sentiment
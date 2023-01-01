# Study Chatbot

A simple command-line study tutor/coach powered by the OpenAI API. Ask it
questions about whatever you're studying, or use the study-mode commands to get
explanations, quizzes, note summaries, and study plans.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Then open `.env` and put in your OpenAI API key:

```
OPENAI_API_KEY=sk-...
```

## Usage

```bash
python chatbot.py
```

Just type a question to chat with the tutor. The conversation keeps context as
you go. Available commands:

- `/explain <topic>` - explain a concept
- `/quiz <topic>` - make a short quiz
- `/summarize <notes>` - summarize notes into bullet points
- `/plan <topic>` - build a study plan
- `/help` - show the command list
- `/quit` - exit (saves the session to `chat_log.txt`)

import os
from datetime import datetime

from dotenv import load_dotenv
import openai

import topics

LOG_FILE = "chat_log.txt"

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

PREAMBLE = (
    "You are a helpful study tutor. Explain things clearly and simply, "
    "give examples, and help the student actually learn the material. "
    "Keep the conversation friendly and encouraging.\n\n"
)

HELP_TEXT = """Commands:
  /explain <topic>   - explain a concept
  /quiz <topic>      - make a short quiz
  /summarize <notes> - summarize notes into bullet points
  /plan <topic>      - build a study plan
  /help              - show this help
  /quit              - exit
"""


def get_answer(transcript):
    prompt = PREAMBLE + transcript + "Tutor:"
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=512,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return "Sorry, something went wrong talking to the API: %s" % e


def save_log(transcript):
    """Append the session transcript to the log file."""
    if not transcript:
        return
    try:
        with open(LOG_FILE, "a") as f:
            f.write("=== Session %s ===\n" % datetime.now().strftime("%Y-%m-%d %H:%M"))
            f.write(transcript)
            f.write("\n")
        print("Chat log saved to %s" % LOG_FILE)
    except Exception as e:
        print("Could not save chat log: %s" % e)


def handle_command(user_input):
    """Turn a study-mode command into a prompt string, or return None."""
    parts = user_input.split(" ", 1)
    command = parts[0]
    arg = parts[1].strip() if len(parts) > 1 else ""

    if command == "/explain" and arg:
        return topics.explain_concept(arg)
    if command == "/quiz" and arg:
        return topics.make_quiz(arg)
    if command == "/summarize" and arg:
        return topics.summarize_notes(arg)
    if command == "/plan" and arg:
        return topics.study_plan(arg)
    return None


def main():
    print("Study Tutor - ask me anything about what you're studying.")
    print(HELP_TEXT)

    transcript = ""
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input == "/quit":
            save_log(transcript)
            print("Happy studying! Bye.")
            break
        if user_input == "/help":
            print(HELP_TEXT)
            continue

        # Study-mode commands get turned into a tailored prompt,
        # otherwise we treat the input as a plain question.
        if user_input.startswith("/"):
            built = handle_command(user_input)
            if built is None:
                print("Unknown command. Type /help to see the options.\n")
                continue
            message = built
        else:
            message = user_input

        transcript += "Student: " + message + "\n"
        answer = get_answer(transcript)
        transcript += "Tutor: " + answer + "\n"
        print("\nTutor: " + answer + "\n")


if __name__ == "__main__":
    main()

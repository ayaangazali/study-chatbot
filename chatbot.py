import os

from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

PREAMBLE = (
    "You are a helpful study tutor. Explain things clearly and simply, "
    "give examples, and help the student actually learn the material. "
    "Keep the conversation friendly and encouraging.\n\n"
)


def get_answer(transcript):
    prompt = PREAMBLE + transcript + "Tutor:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=512,
        temperature=0.7,
    )
    return response.choices[0].text.strip()


def main():
    print("Study Tutor - ask me anything about what you're studying.")

    transcript = ""
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue

        transcript += "Student: " + user_input + "\n"
        answer = get_answer(transcript)
        transcript += "Tutor: " + answer + "\n"
        print("\nTutor: " + answer + "\n")


if __name__ == "__main__":
    main()

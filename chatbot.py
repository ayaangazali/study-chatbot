import os

from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_answer(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=512,
        temperature=0.7,
    )
    return response.choices[0].text.strip()


def main():
    user_input = input("You: ").strip()
    answer = get_answer(user_input)
    print("\nTutor: " + answer + "\n")


if __name__ == "__main__":
    main()

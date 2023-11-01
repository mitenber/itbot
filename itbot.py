import os
import openai
from dotenv import load_dotenv
import argparse

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key

def generate_itbot_response(user_issue, chat_history):
    messages= [{"role":"system", "content":"You are a helpful IT support assitant fixing all issues"}]
    messages.extend(chat_history)
    messages.append({"role":"user", "content":user_issue})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    assistant_reply = response.choices[0].message["content"]
    return assistant_reply

def main():
    print("Welcome to the IT Support Chatbot!")
    print("Type iny our issue or 'exit' to quit.")

    chat_history = []

    while True:
        user_message = input("YOU: ")

        if user_message.lower() == "exit":
            print("Goodbye!")
            break

        response = generate_itbot_response(user_message, chat_history)
        print("IT Support Bot: ", response)

        chat_history.append({"role":"user", "content":user_message})
        chat_history.append({"role": "assistant", "content": user_message})


if __name__ == "__main__":
    main()
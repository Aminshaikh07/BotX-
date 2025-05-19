import os
from dotenv import load_dotenv
import openai

# Load API key
load_dotenv('key.env')
openai.api_key = os.getenv('OPENAI_API_KEY')

# Load system prompt
with open('prompt/academic_prompt.txt', 'r') as f:
    SYSTEM_PROMPT = f.read()

def ask_gpt(message):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": message}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message["content"].strip()

if __name__ == "__main__":
    print("Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            break
        reply = ask_gpt(user_input)
        print("Bot:", reply)

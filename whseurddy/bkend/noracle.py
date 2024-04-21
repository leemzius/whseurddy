from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def get_chat_completion(question, outcome):
    user_message = f"{question} The outcome of the coin flip is {outcome}."
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "you are a humble yet encouraging assistant, your tasks are to generate sarcastic motivational quote based on the outcome of the coin flip for the question the user gives with a creative flair. A tails indicates a yes to the user's question and heads is a no to the question."},
            {"role": "user", "content": user_message}
        ]
    )
    return completion.choices[0].message.content # Return the string response from the openai



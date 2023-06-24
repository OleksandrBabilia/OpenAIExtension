import openai
from dotenv import load_dotenv
import os

openai.api_key = os.environ['API_KEY']

def generate_response(question):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=question,
        max_tokens=5 
    )
    return response.choices[0].text.strip()

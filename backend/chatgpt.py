import openai
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

openai.api_key = os.environ['API_KEY']

def generate_response(question: str):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=question,
        max_tokens=40 
    )
    
    return response.choices[0].text.strip()

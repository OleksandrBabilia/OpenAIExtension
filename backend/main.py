from fastapi import FastAPI

from data_parser import parse
from chatgpt import generate_response

app = FastAPI()


@app.get("/api/get_openai_summary/")
async def root(username: str, password: str, page_url: str) :
    
    result = []
    questions = parse(username, password, page_url)
    if questions is None:
        return {
            'success': False,
        }
        
    for i, question in enumerate(questions):
        formatted_question = question.replace('\n', '').replace('\r', '')
        response = generate_response(formatted_question)
        result.append(f"{i+1}. {response}")
        
    return {
            'success': True,
            'data': result
        }

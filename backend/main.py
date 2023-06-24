from fastapi import FastAPI

from data_parser import parse
from chatgpt import generate_response

app = FastAPI()


@app.get("/api/get_openai_summary/")
async def root(username: str, password: str, page_url: str) -> list[str]:
    result = []
    questions = parse(username, password, page_url)
    
    if questions is None:
        return {
            'success': False,
        }
        
    for i, question in enumerate(questions):
        response = generate_response(question)
        result.append(f"{i+1}. {response}")
        
    return {
            'success': False,
            'data': result
        }
    
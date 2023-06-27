import requests
from bs4 import BeautifulSoup as BS

from authentication import authenticate

def parse(username: str, password:str, page_url: str):
    login_url = 'https://vns.lpnu.ua/login/index.php'

    session = authenticate(username, password, login_url)

    if session is None:
        return None

    response = session.get(page_url)

    if response.status_code != 200:
        print('Failed to retrieve page for parsing.')
        return None
        
    result = []
    
    soup = BS(response.content, 'html.parser')
    question_divs = soup.find_all(class_="qtext")
    answer_divs = soup.find_all(class_="answer")
        
    if not(question_divs or answer_divs):
        print('Failed to retrieve questions or answers.')
        return None
        
    for question_div, answer_div in zip(question_divs, answer_divs):
        result.append(f"Питання: {question_div.text.strip()}\n Відповіді: {answer_div.text.strip()}")

    return result
        

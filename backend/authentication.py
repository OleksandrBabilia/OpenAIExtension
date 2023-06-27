import requests
from bs4 import BeautifulSoup as BS

def authenticate(username: str, password: str, login_url: str):
    session = requests.Session()

    response = session.get(login_url)
    soup = BS(response.content, 'html.parser')
    logintoken = soup.find('input', {'name': 'logintoken'}).get('value')

    login_data = {
        'logintoken': logintoken,
        'username': username,
        'password': password
    }

    response = session.post(login_url, data=login_data)

    if response.status_code == 200:
        print('Authentication successful.')
        return session
    
    print('Authentication failed.')
    return None

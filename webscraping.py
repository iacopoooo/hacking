
import requests
from bs4 import BeautifulSoup

url = "https://it.wikipedia.org/wiki/Firenze"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    # Rimuove tutti i tag <img> dalla soup
    for img_tag in soup.find_all('img'):
        img_tag.decompose()

    # Estrai il testo da tutti gli altri elementi
    text_content = soup.get_text(separator='\n', strip=True)

    print(text_content)
except requests.RequestException as e:
    print(f"Errore nella richiesta: {e}")

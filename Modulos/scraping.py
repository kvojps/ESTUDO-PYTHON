import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.question-summary'):
    titulo = pergunta.select_one('.question-hyperlink')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.vote-count-post strong')
    print(data.text, titulo.text,votos.text, sep='--> ')
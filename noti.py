import requests
from lxml import html
from bs4 import BeautifulSoup
import re

header = {
	'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75"
}


URL = "https://globoesporte.globo.com/futebol/"

response = requests.get(URL, headers=header)
content = response.content

site = BeautifulSoup(content, 'html.parser')
num = 1
num2 = 0
links = []
arq = open('noticias.txt', 'w')
for noti in site.find_all('a', attrs={'class': "feed-post-link gui-color-primary gui-color-hover"}):
	links.append(noti.get('href'))
	for no in noti:
		arq.write(f'NOTÍCIA {num}:\n{no}\n\nVEJA EM:\n{links[num2]}\n\n\n')
		num = num + 1
		num2 = num2 + 1

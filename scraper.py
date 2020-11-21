import requests
from bs4 import BeautifulSoup
import requests

page = requests.get('https://liraltd.com/semconf-2018', verify=False) # get-запрос

soup = BeautifulSoup(page.text, 'html.parser')

raw = soup.find('div', class_='blogpost').text

print (raw)
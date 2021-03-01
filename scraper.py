import requests
from bs4 import BeautifulSoup
import requests

page = requests.get('https://liraltd.com/semconf-2018', verify=False) # get-запрос

soup = BeautifulSoup(page.text, 'html.parser')

raw = soup.find('div', class_='blogpost').text

print (raw)



/////////thins for creating array with ncs

from cssutils import parseStyle


f = open('arrayforconwertor.txt', 'w')


soup = BeautifulSoup(page, features="lxml")


for i in soup.select("option"):
	#style = parseStyle(soup.option['style'])
	
    #print(i.text)
    f.write(i.text)
    style = parseStyle(i['style'],'...................')
    #print(style['background-color'])
    f.write(style['background-color'] + '\n')

style = parseStyle(soup.option['style'])



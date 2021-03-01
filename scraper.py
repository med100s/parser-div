import requests
from bs4 import BeautifulSoup
import requests

page = requests.get('https://liraltd.com/semconf-2018', verify=False) # get-запрос

soup = BeautifulSoup(page.text, 'html.parser')

raw = soup.find('div', class_='blogpost').text

print (raw)





#addition to parse colors
#
#from cssutils import parseStyle
#
#
#
#soup = BeautifulSoup(page, features="lxml")
##
#
#for i in soup.select("option"):
#style = parseStyle(soup.option['style'])
#	
#    print(i.text)
#    style = parseStyle(i['style'])
#    print(style['background-color'])
#
#
#style = parseStyle(soup.option['style'])

import requests
import pprint
import inflection
from bs4 import BeautifulSoup

r = requests.get('http://www.dailysmarty.com/topics/python/posts')
text_html = r.text
soup = BeautifulSoup(text_html,features="html.parser")
soup.prettify()
#print(html_ordenado)
#post = 'post-link-title'
 
#print(soup.prettify())








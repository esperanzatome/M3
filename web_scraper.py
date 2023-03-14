import requests
import inflection
from bs4 import BeautifulSoup
r = requests.get('http://www.dailysmarty.com/topics/python')
pagina= BeautifulSoup(r.text,features="html")
posts= pagina.find_all('h2')
lista_posts=list(posts)[:]
def web_scraper():
  for post in lista_posts:
    post.get_text()
    print(post.get_text())
web_scraper()    
    


  

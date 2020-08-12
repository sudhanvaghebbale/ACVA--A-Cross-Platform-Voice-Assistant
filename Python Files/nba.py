import requests
from bs4 import BeautifulSoup 
URL = "https://www.basketball-reference.com/boxscores/"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html5lib') 
table = soup.find('div', attrs = {'id':'game_summaries'})
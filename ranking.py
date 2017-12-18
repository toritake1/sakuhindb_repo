import codecs
from urllib.request import urlopen
import sys
import re
from bs4 import BeautifulSoup

url = "http://sakuhindb.com/anime-ranking/2017/"
html = urlopen(url).read().decode('utf-8', 'ignore')
soup = BeautifulSoup(html, "html.parser")
links = [a.get("href") for a in soup.find_all("a", href=re.compile("^/janime/"))]

for l in links: 
  print ("http://sakuhindb.com/" + l)



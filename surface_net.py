import requests
from bs4 import BeautifulSoup
import os
import sys
import urllib

URL = "http://hcmaslov.d-real.sci-nnov.ru/public/texts/%d0%97%d0%b0%d0%b4%d0%b0%d1%87%d0%b0%20%d0%bd%d0%b0%20%d1%81%d0%be%d0%be%d0%b1%d1%80%d0%b0%d0%b7%d0%b8%d1%82%d0%b5%d0%bb%d1%8c%d0%bd%d0%be%d1%81%d1%82%d1%8c/%d0%91%d1%83%d1%80%d0%b0%d1%82%d0%b8%d0%bd%d0%be%20%d0%b8%20%d1%8f%d0%b1%d0%bb%d0%be%d0%ba%d0%b8/"

root = requests.get(URL)
soup = BeautifulSoup(root.content,'lxml')

for img in soup.find_all('img',{'src':True}):
    if img['src'] == '/icons/blank.gif':
        
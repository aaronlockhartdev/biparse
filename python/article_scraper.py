import requests
import csv
import time
from bs4 import BeautifulSoup
import urllib

def scrape_article(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    p = soup.find_all('p')
    cleantext = BeautifulSoup(str(p), 'html.parser').text
    return(cleantext)

def scrape_article_headline(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    h1 = soup.find_all('h1')
    cleantext = BeautifulSoup(str(h1), 'html.parser').text
    return(cleantext)




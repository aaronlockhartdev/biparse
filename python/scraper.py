from requests_html import HTMLSession
import requests
import csv
import time
from bs4 import BeautifulSoup
import urllib

def check_google(inp):
    bad = False
    for i in range(len(inp)):
        if inp[i:i+10] == 'google.com':
            bad = True
    return bad

def parse_links(inp):
    search = inp.replace(" ","+")
    googleurl = 'https://www.google.com/search?q='+search+'&rlz=1C1CHBF_enUS850US850&tbm=nws&source=lnt&tbs=qdr:m&sa=X&ved=0ahUKEwjQ3e2horniAhUKxVkKHS_AC34QpwUIIQ&biw=1536&bih=754&dpr=2.5'

    session = HTMLSession()

    r = session.get(googleurl)

    r1 = [i for i in list(r.html.links) if i[0] != '/' and not check_google(i)]

    return r1

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

def get_links(url):

    threshold = 0.7

    cons = None
    lib = None
    mid = None

    for p in parse_links(scrape_article_headline(url)):
        data = get_data(str(p))
        if data[0] > threshold and lib is None:
            lib = str(p)
        elif data[1] > threshold and cons is None:
            cons = str(p)
        elif mid is None:
            mid = str(p)
        if lib is not None and cons is not None and mid is not None:
            break

    return cons, lib, mid



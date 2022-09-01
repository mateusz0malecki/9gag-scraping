from bs4 import BeautifulSoup
from requests import get


def scraping(link):
    page = get(link).content
    bs = BeautifulSoup(page, 'html.parser')
    return bs

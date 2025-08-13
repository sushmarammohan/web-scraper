from bs4 import BeautifulSoup
import requests

def scraplogs():
    pageToScrape = requests.get("https://www.tapaway.com.au/blog")
    soup = BeautifulSoup(pageToScrape.text, "html.parser")
    authors = soup.findAll('span', attrs= {'class':'tQ0Q1A'})
    titles = soup.findAll('h2', attrs= {'class':'bD0vt9 KNiaIk'})

    for author, title in zip(authors, titles):
        print(author.text + " - " + title.text)

scraplogs()

# To get details from website
# so here I would get all the classes with 'text' in it to the vaiable `quote`

from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("http://quotes.toscrape.com")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')


# print(soup.footer)
quotes = soup.findAll('span', attrs={'class':'text'})

print([quote.text for quote in quotes])
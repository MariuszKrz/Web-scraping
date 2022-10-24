from bs4 import BeautifulSoup
import requests

url = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/bydgoszcz?distanceRadius=50&market=ALL&locations=%5Bcities_6-184%5D&viewType=listing&lang=pl&searchingCriteria=sprzedaz&searchingCriteria=mieszkanie&searchingCriteria=cala-polska'
page = requests.get(url)

bs = BeautifulSoup(page.content, 'html.parser')

for offer in bs.find_all('li'):
    result = offer.get_text()
    print(result)

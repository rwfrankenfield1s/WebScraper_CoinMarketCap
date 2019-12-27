import requests
from bs4 import BeautifulSoup
import csv

##create
#f = csv.writer(open('crypt_sweep.csv', 'w'))
#f.writerow(['Crypto'])

#id
page = requests.get('https://coinmarketcap.com/')
soup = BeautifulSoup(page.text, 'html.parser')


cryptoList = soup.find_all("td")

for items in cryptoList:
    name = items.find_all("div", {"class": "cmc-table__column-name sc-1kxikfi-0 eTVhdN",})
    data = items.find_all("div", {"class": "",})
    print(data)

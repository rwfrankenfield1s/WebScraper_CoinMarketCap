import requests
from bs4 import BeautifulSoup
import csv

##create
f = csv.writer(open('crypt_sweep.csv', 'w'))
f.writerow(['Crypto'])

#id
page = requests.get('https://coinmarketcap.com/')
soup = BeautifulSoup(page.text, 'html.parser')

#clean
last_links1 = soup.find(class_='cmc-table__table-wrapper-outer')
last_links1.decompose()

##
scrape = soup.find( class_='cmc-table-row')
#print(scrape)

crypto_name_list_price = scrape.find_all('a')
#print(crypto_name_list_price)


for crypto_name in crypto_name_list_price:
    crypto = crypto_name.contents[0]
    print(crypto)
    f.writerow([crypto.encode("utf-8")])

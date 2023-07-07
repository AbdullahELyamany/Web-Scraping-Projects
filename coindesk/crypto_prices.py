# Scraping To #CoinDesk# WebSite From Page #CryptoPrices

# Created by Abdullah EL-Yamany


# Note => An error can occur if the site has been modified
#      => After running the code, you can go to the csv file.  to see the results

# ===============================

import requests as rq
from bs4 import BeautifulSoup as bs
import csv
from itertools import zip_longest


page = rq.get('https://www.coindesk.com/data/')



list_name = []
list_abbr = []
list_price = []
list_rate = []

def main(page):

    src = page.content    # == page.text
    
    soup = bs(src, 'lxml')



    name_coin = soup.find_all("span", {'class': 'typography__StyledTypography-owin6q-0 gtxndB'})


    for name in name_coin :

        list_name.append(name.text)

    abbreviation = soup.find_all("span", {'class': 'typography__StyledTypography-owin6q-0 fUOSEs'})


    for abb in abbreviation :

        if abb.text !='24H' :

            list_abbr.append(abb.text)


    prices = soup.find_all("h6", {'class': 'typography__StyledTypography-owin6q-0 brrRIQ'}) 

    for price in prices :

        list_price.append(price.text)


    rates = soup.find_all("div", {'class': 'percentage'})

    for rate in rates :

        list_rate.append(rate.text)


    file_list = [list_name, list_abbr, list_price, list_rate]

    exported = zip_longest(*file_list)


    with open('coin.csv', 'w') as csv_file :

        writer = csv.writer(csv_file)
        writer.writerow(["Coin Name", "abbreviation", "Price in relation to the dollar", "The rate high or low in last 24 hours"])
        writer.writerows(exported)
        print("All Done!")




main(page)

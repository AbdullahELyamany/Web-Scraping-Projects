
"""
 Web Scraping Project To find out the price of Bitcoin and Ethereum and send it to the Telegram bot
 
 Created by Abdullah EL-Yamany


 Note => An error can occur if the site has been modified
"""


######## You must first create a Telegram bot and find [api_key, bot_key, chat_id] ########


import requests
import time


    # global variables

api_key = 'a9466fa8-aa03-4122-8133-093dd0112354'
bot_key = '5807735834:AAEvi3igv1ffpIIIX5DfsgA99BVTxhzyqBo' # From  BotFather  in telegram
chat_id = '5895461811'    # From IDBot  in telegram

limit = 20000

time_interval = 60    # 60 second == 1 minute

def get_price():

    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    parameters = {
        'start' : '1',
        'limit' : '3'
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url, headers=headers, params=parameters).json()
    btc_price = response['data'] [0] ['quote'] ['USD'] ['price']
    ethu_price = response['data'] [1] ['quote'] ['USD'] ['price']

    return btc_price, ethu_price


def send_update(chat_id, msg):

    url = f'https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}'
    requests.get(url)


def main():

    while True :

        price = get_price()
        print(price[0], end=' & ')
        print(price[1])
        
        send_update(chat_id, f"Bitcoin_price : {price[0]} 💲")
        send_update(chat_id, f"Ethereum_price : {price[1]} 💲")

        time.sleep(time_interval)

main()


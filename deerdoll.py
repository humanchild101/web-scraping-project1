"""
Author: Nikhila
Date Created: December 28, 2024
Description: A Python program for web scraping item names, prices, and links from the deerdoll.com website.
"""
from bs4 import BeautifulSoup
import requests


def test(item):
    print("Link name: deerdoll \nItem is: " + item)

def scrape(item, num_result):
    deer_doll = requests.get(f'https://deerdoll.com/search?q={item}').text
    d_txt = BeautifulSoup(deer_doll, 'lxml')
    d_txt.prettify()

    d_names = []
    d_prices = []
    d_links = []

    d_each = d_txt.find_all('div', class_="grid__item medium--one-third large-up--one-quarter small--one-half")
    for e in d_each:
        if e != None:
            # for links (links)
            a_tag = e.find('a')
            d_link = "deerdoll.com" + a_tag.get('href')
            d_links.append(d_link)

            # for names (full names)
            n = e.find('div', class_="product-info")
            d_name = n.find('a').get('title')
            d_names.append(d_name)

            # for prices (floats)
            d_price = float(n.find('span', class_='money').text.split("$")[1])
            d_prices.append(d_price)

    price_list = []
    price_value = ""
    print("For deerdoll.com: ")
    for i in range(int(num_result)):
        price_value = f'{i + 1}. {d_names[i]} \n    Price: ${d_prices[i]}0 \n    Link: {d_links[i]}\n'
        price_list.append(price_value)

    return "\n".join(price_list)


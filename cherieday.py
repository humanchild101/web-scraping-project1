"""
Author: Nikhila
Date Created: December 31, 2024
Description: A Python program for web scraping item names, prices, and links from the cherieday.com website.
"""
from bs4 import BeautifulSoup
import requests


def test(item):
    print("Link name: cherieday \nItem is: " + item)

def scrape(item, num_result):
    cherie_day = requests.get(f'https://www.cherieday.com/catalogsearch/result/?q={item}').text
    c_txt = BeautifulSoup(cherie_day, 'lxml')
    c_txt.prettify()

    c_names = []
    c_prices = []
    c_links = []
    c_ratings = []

    c_list = c_txt.find('ul', class_='products-grid')
    c_each = []
    if c_list != None:
        c_each = c_list.find_all('li')

    for c in c_each:
        if c != None:
            # links
            cd = c.find('div', class_='item-img')
            c_link = cd.find('a').get('href')
            c_links.append(c_link)

            # descritptions/names
            li = c.find('div', class_='item-text')
            name = li.find('h3')
            c_name = name.find('a').text
            c_names.append(c_name)

            # prices
            pr = c.find('div', class_="price-box")
            price = pr.find('p', class_='special-price')
            c_price = float((price.find('span', class_='price').text).replace(" ", "").split("$")[1])
            c_prices.append(c_price)

            # ratings
            r = li.find('div', class_='list-rate-review')
            ra = r.find('div', class_='ratings')
            rat = ra.find('div', class_='rating-box')
            c_ra = rat.find('div', class_='rating')
            if c_ra != None:
                c_rat = c_ra.get('style')
                c_rating = c_rat.split(':')[1]
                c_ratings.append(int(c_rating.split("%")[0]))
            else:
                c_ratings.append(0)

    price_list = []
    price_value = ""
    print("For cherieday.com: ")

    for i in range(int(num_result)):
        price_value = f'{i + 1}. {c_names[i]} \n    Price: ${c_prices[i]}0 \n    Link: {c_links[i]}'
        price_list.append(price_value)

    return "\n".join(price_list)
"""
Author: Nikhila
Date Created: December 29, 2024
Description: A Python program for web scraping item names, prices, and links from the petallush.com website.
"""
from bs4 import BeautifulSoup
import requests

def test(item):
    print("Link name: petallush \nItem is: " + item)

def scrape(item, num_result):
    petal_lush = requests.get(f'https://www.petallush.com/catalogsearch/result/?q={item}').text
    p_txt = BeautifulSoup(petal_lush, 'lxml')
    p_txt.prettify()

    p_names = []
    p_prices = []
    p_links = []
    p_ratings = []

    p_list = p_txt.find('ul', class_='products-grid')
    p_each = []
    if p_list != None:
        p_each = p_list.find_all('li')
    for p in p_each:
        if p != None:
            # links
            ph = p.find('h3', class_='product-name')
            p_link = ph.find('a').get('href')
            p_links.append(p_link)

            # names
            name = ph.find('a').text
            p_names.append(name)

            # prices
            pr = p.find('div', class_='price-box')
            reg_p = pr.find('span', class_="regular-price")
            if reg_p != None:
                p_prices.append(float(reg_p.find('span', class_='price').text.split("$")[1]))
            else:
                pri = pr.find('p', class_='special-price')
                p_price = pri.find('span', class_='price').text
                np = p_price.replace(" ", "").split("\n")[1]
                p_prices.append(float(np.split("$")[1]))

            # ratings
            pa = p.find('div', class_='ratings')
            prat = pa.find('div', class_='rating-box')
            p_ra = prat.find('div', class_='rating')
            if p_ra != None:
                p_rat = p_ra.get('style')
                p_rating = p_rat.split(':')[1]
                p_ratings.append(int(p_rating.split("%")[0]))
            else:
                p_ratings.append(0)

    price_list = []
    price_value = ""
    print("For petallush.com: ")
    for i in range(int(num_result)):
        price_value = f'{i + 1}. {p_names[i]} \n    Price: ${p_prices[i]}0 \n    Link: {p_links[i]}'
        price_list.append(price_value)

    return "\n".join(price_list)
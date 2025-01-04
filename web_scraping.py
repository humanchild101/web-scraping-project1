"""
Author: Nikhila
Date Created: Jan 2, 2025
Description: A Python program for scraping item information from specific websites (deerdoll, petallush, cherieday).
"""
import deerdoll
import petallush
import cherieday


def scrape(website, item, num_result):
    scraped_info = ""
    if website == 'deerdoll':
        scraped_info = deerdoll.scrape(item, num_result)
    elif website == 'petallush':
        scraped_info = petallush.scrape(item, num_result)
    elif website == 'cherieday':
        scraped_info = cherieday.scrape(item, num_result)

    return scraped_info




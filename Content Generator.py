# Name: Josh Nguyen
# Date: 2/14/2021
# Class: CS361
# Description: This program generates text based off of inputted keywords

import requests as res
import bs4 as bs


def request_html(url):
    """Requests the HTML from the Wiki page"""
    request = res.get(url)
    wiki_html = bs.BeautifulSoup(request.text, "html.parser")
    return wiki_html


def create_url(keyword):
    """Attach keyword into URL format"""
    wiki_url = "https://en.wikipedia.org/wiki/"
    wiki_url += keyword
    return wiki_url


def parse_wiki_data(data, primary_keyword, secondary_keyword):
    """Parse through Wiki page for paragraphs containing the secondary keyword"""
    pass

# text = "https://en.wikipedia.org/wiki/Kobe_Bryant"
# req = res.get(text)
# type(req)
#
# test = bs.BeautifulSoup(req.text, "html.parser")
# para = test.select("p")

# for string in test.strings:
#     if "Lakers" in string:
#         print(repr(string))


url = create_url("Kobe_Bryant")
wiki_data = request_html(url)
print(dir(wiki_data))

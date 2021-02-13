# Name: Josh Nguyen
# Date: 2/14/2021
# Class: CS361
# Description: This program generates text based off of inputted keywords

import tkinter
import requests as res
import bs4 as bs

text = "https://en.wikipedia.org/wiki/Kobe_Bryant"
req = res.get(text)
type(req)

test = bs.BeautifulSoup(req.text, "html.parser")
para = test.select("p")

for string in test.strings:
    if "Lakers" in string:
        print(repr(string))

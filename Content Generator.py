# Name: Josh Nguyen
# Date: 2/14/2021
# Class: CS361
# Description: This program generates text based off of inputted keywords.

from tkinter import *
from tkinter import ttk
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
    for p in wiki_data.find_all("p", limit=5):
        print(p.contents[0])


url = create_url("Kobe_Bryant")
wiki_data = request_html(url)

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


root = Tk()
root.title("Content Generator")

mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

primary_keyword = StringVar()
primary_keyword_field = ttk.Entry(mainframe, width=20, textvariable=primary_keyword)
primary_keyword_field.grid(column=2, row=1, sticky=(W, E))

secondary_keyword = StringVar()
secondary_keyword_field = ttk.Entry(mainframe, width=20, textvariable=secondary_keyword)
secondary_keyword_field.grid(column=2, row=2, sticky=(W, E))



ttk.Button(mainframe, text="Generate", command=calculate).grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="Primary Keyword:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Secondary Keyword:").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

primary_keyword_field.focus()
root.bind("<Return>", calculate)

root.mainloop()

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 22:32:15 2018

@author: maiti
"""

# from Package.Module import Library as alias
from bs4 import BeautifulSoup as soup
import requests as uReq

url = 'https://www.newegg.com/Cell-Phones-Unlocked/SubCategory/ID-2961?Tid=167543'

result = uReq.get(url)
c = result.content

# html parsing
page_html = soup(c, 'html.parser')

#page_html

# Grabs each Product in the result 
items = page_html.findAll("div",{"class":"item-container"})

#len(items)

del items[0]

filename = "products.csv"
f = open(filename,"w")

headers = "Brand, Description\n"
f.write(headers)

try:
    for product in items:
        brand_none= product.findAll("a",{"class":"item-brand"})
        brand = brand_none[-1].img["title"]
        #brand = product.div.div.a.img["alt"]
        description = product.a.img["alt"]
        f.write(brand + "," + description.replace(",","|") + "\n" )
except IndexError:
    print('Warning: list index out of range')
    
f.close()






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

#page_html.prettify()

# Grabs each Product in the result 
items = page_html.findAll("div",{"class":"item-info"})

#len(items)

filename = "products.csv"
f = open(filename,"w")

headers = "Brand, Price, OperatingSystem, Description \n"
f.write(headers)

try:
    for product in items:
            
        brand = product.a.img['title']
        item_features = product.find_all("ul")
        
        item_features0_li = item_features[0].find_all('li') 
        operatingsys = item_features0_li[0]
        
        item_feature1_li = item_features[1].find_all('li')
        price = item_feature1_li[2].strong.string
        
        description = product.find(title ="View Details");description
        
        f.write(brand + ","+price.replace(",","")+","+str(operatingsys).replace(",","|")+","+str(description).replace(",","|")+"\n" )
except IndexError:
    print('Warning: list index out of range')
    
f.close()

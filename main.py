# Description: This is the main file for the project. It will be used to run the program.
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging

flipkart_base = "https://www.flipkart.com"
flipkart_url = "https://www.flipkart.com/search?q=" + "iphone"
uClient = urlopen(flipkart_url)
flipart_page = uClient.read()
flipcart_html = bs(flipart_page,'html.parser')
# print(flipcart_html)
bigbox = flipcart_html.findAll("div" , {"class":"_2kHMtA"})
del bigbox[0:3]

product_links = []
for i in range(len(bigbox)):
    l = flipkart_base + bigbox[i].a['href']
    product_links.append(l)

print(product_links)



# Description: This is the main file for the project. It will be used to run the program.
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from utils.page import page_parser
import logging

flipkart_base = "https://www.flipkart.com"
flipkart_url = "https://www.flipkart.com/search?q=" + "redmi"


flipcart_html = page_parser(flipkart_url)
bigbox = flipcart_html.findAll("div" , {"class":"_2kHMtA"})
del bigbox[0:3]

product_links = []
product_reviews_links = []


for i in range(len(bigbox)):
    print(i)
    l = flipkart_base + bigbox[i].a['href']
    product_links.append(l)


for i in product_links:
    print(i)
    flipcart_html = page_parser(i)
    bigbox = flipcart_html.findAll("div" , {"class":"col JOpGWq"})
    l = flipkart_base + bigbox[0].a['href']
    print(l)
    product_reviews_links.append(l)

range_ = []

for i in product_reviews_links:
    try:
        print(i)
        flipcart_html = page_parser(i)
        bigbox = flipcart_html.findAll("div" , {"class":"_2MImiq _1Qnn1K"})
        print(bigbox[0].span.text)
    except:
        pass



print(product_reviews_links)
print("done")






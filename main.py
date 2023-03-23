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
        split_ = bigbox[0].span.text.split(" ")[-1]
        range_.append(split_)
    except:
        range_.append("0")
        pass

product_dict = {}
final_dict = {"product_links":product_links, "product_reviews_links":product_reviews_links, "range":range_}
all_reviews_page_links = []
for i in product_reviews_links:
    try:
        for j in range(1, int(final_dict["range"][product_reviews_links.index(i)])+1):
            print(i + "&page=" + str(j))
            all_reviews_page_links.append(i + "&page=" + str(j))
        for k in all_reviews_page_links:
            flipcart_html = page_parser(k)
            bigbox = flipcart_html.findAll("div" , {"class":"_27M-vq _2hwual"})
            for i in range(len(bigbox)):
                comment = flipcart_html.findAll("div" , {"class":"t-ZTKy"})
                name = bigbox[i].div.div.p.text
                comment = comment[i].text[0:-9]
                #remove READ MORE from comment if present
                product_dict[name] = comment
                print(name, comment)
    except:
        pass

    all_reviews_page_links = []


print(all_reviews_page_links)








import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from utils.page import page_parser
import logging
import os
def review_scrapper(PN : str):
    """
    this function will take product then find all the products related to that product in first page and then it will find all the reviews
    of that product and then it will save it in a text file
    :param PN: Product Name
    :return:
    """

    flipkart_base = "https://www.flipkart.com"
    flipkart_url = "https://www.flipkart.com/search?q=" + PN

    flipcart_html = page_parser(flipkart_url)
    bigbox = flipcart_html.findAll("div", {"class": "_2kHMtA"})
    print(bigbox[0:3])
    del bigbox[0:3]

    product_links = []
    product_reviews_links = []

    for i in range(len(bigbox)):
        try:
            print(i)
            l = flipkart_base + bigbox[i].a['href']
            name_pro = bigbox[i].div.div.img['alt']
            # remove the special characters from the name of the product
            name_pro = name_pro.replace(" ", "_")
            name_pro = name_pro.replace("(", "")
            name_pro = name_pro.replace(")", "")
            name_pro = name_pro.replace(",", "")
            name_pro = name_pro.replace(".", "")
            name_pro = name_pro.replace(":", "")
            name_pro = name_pro.replace(";", "")
            name_pro = name_pro.replace("!", "")
            name_pro = name_pro.replace("?", "")
            name_pro = name_pro.replace("/", "")
            name_pro = name_pro.replace("\\", "")
            name_pro = name_pro.replace("'", "")
            name_pro = name_pro.replace('"', "")
            name_pro = name_pro.replace("’", "")
            print(name_pro)
            print(l)
            flipcart_html = page_parser(l)
            links = flipcart_html.findAll("div", {"class": "col JOpGWq"})
            j = flipkart_base + links[0].a['href']
            product_html = page_parser(j)
            range_ = product_html.findAll("div", {"class": "_2MImiq _1Qnn1K"})
            split_ = int(range_[0].span.text.split(" ")[-1])
            for k in range(1, split_ + 1):
                page_ = j + "&page=" + str(k)
                print(page_)
                page_html = page_parser(page_)
                comments = page_html.findAll("div", {"class": "_27M-vq _2hwual"})
                for i in range(len(comments)):
                    name = comments[i].div.div.p.text
                    comment = page_html.findAll("div", {"class": "t-ZTKy"})
                    comment = comment[i].text[0:-9]
                    print(name, comment)
                    with open("data/" + name_pro + ".txt", "a", encoding="utf-8") as f:
                        f.write(name + "  " + comment + "\n")
                        f.close()


        except Exception as e:
            print(e)
            pass

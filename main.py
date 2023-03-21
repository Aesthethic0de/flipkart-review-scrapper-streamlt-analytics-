# Description: This is the main file for the project. It will be used to run the program.
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging

flipkart_url = "https://www.flipkart.com/search?q=" + "iphone"
uClient = urlopen(flipkart_url)
flipart_page = uClient.read()
print(flipart_page)


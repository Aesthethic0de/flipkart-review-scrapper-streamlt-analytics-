from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
def page_parser(url):
    """
    This function will parse the page and return the html
    :param url: pass the url of the page we need to scrape it.
    :return:
    """
    uClient = urlopen(url)  # url goes in get you data
    flipart_page = uClient.read()
    flipcart_html = bs(flipart_page, 'html.parser')
    return flipcart_html
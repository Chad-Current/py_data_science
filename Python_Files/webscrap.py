from urllib.request import urlopen as uReq
import bs4
from bs4 import BeautifulSoup as soup




my_url = 'https://www.google.com'
read_page = uReq(my_Url)
page_html = read_page.read()
read_page.close()
page_soup = soup(page_html, "html.parser")
page.soup('div',{'class':'bold'})

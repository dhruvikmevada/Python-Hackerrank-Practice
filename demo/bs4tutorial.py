import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url = "https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/"
uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html, "html.parser")
container = page_soup.find_all("div", {"class":"discount_final_price"})
fileone = open("demopage.html", "w+")
discounted_price = ("<p>discounted GTA V price: </p>" + str(container[0]), "<p>Buy Grand Theft Auto V: Premium Online Edition: " + str(container[1]), "<p>Buy Grand Theft Auto V: Premium Online Edition & Megalodon Shark Card Bundle: </p>" + str(container[2]), "<p>Buy Grand Theft Auto V: Premium Online Edition & Great White Shark Card Bundle: </p>" + str(container[3]))
fileone.writelines(discounted_price)
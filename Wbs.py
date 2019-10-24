
import requests
from bs4 import *
from urllib.request import *

url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
r = urlopen(url)
bo = BeautifulSoup(r,'html.parser')

container = bo.find_all("div",{"class":"_3O0U0u"})

containers = container[0]
print(containers.div.img['alt'])
li = (container[0].text).split('|')
print("SPECIFICATION IS:{}".format(li[1]))


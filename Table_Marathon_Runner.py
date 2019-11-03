import requests
from bs4 import *
import pandas

url = requests.get('https://en.wikipedia.org/wiki/Marathon').text
bs = BeautifulSoup(url,'html.parser')
Table = bs.find('table',{'class':'wikitable sortable'})
link = Table.findAll('a')

Marathon_runner = []
for li in link:
    Marathon_runner.append(li.get('title'))


Marathon_name = Marathon_runner[1:len(Marathon_runner):2]
Runner = Marathon_runner[0:len(Marathon_runner):2]

data_frame = pandas.DataFrame(list(zip(Marathon_name,Runner)),columns=['Marathon-Name','Name'])
print(data_frame)

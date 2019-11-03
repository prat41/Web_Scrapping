import requests
from bs4 import *
import pandas



url = requests.get('https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area').text

bs = BeautifulSoup(url,'html.parser')

Table = bs.find('table',{'class':'wikitable sortable'})

link = Table.findAll('a')



countries = []

for li in link:
    countries.append(li.get('title'))

# print(countries)


data_frame = pandas.DataFrame()
data_frame['Country'] = countries
print(data_frame)





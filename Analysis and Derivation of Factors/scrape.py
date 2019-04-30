import bs4
import requests
res = requests.get('https://nfsm.gov.in/nfmis/rpt/calenderreport.aspx')
print(res)
#print(type(res))
soup = bs4.BeautifulSoup(res.text, 'lxml')
#print(soup)

data = ''



for i in soup.select('td'):
    data = data + i.text + ' '
#print(data)
data_list = data.split(' ')
x = data_list.index('Sowing')
limiter = x - 59
print(data_list[limiter:])
import pandas as pd


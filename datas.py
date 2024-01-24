from bs4 import BeautifulSoup
import requests
import pandas as pd
import plotly.graph_objects as go


# site url
url="https://merolagani.com/LatestMarket.aspx"

# make a get request to fetch the raw html data
con=requests.get(url)
soup=BeautifulSoup(con.text,"lxml")
table=soup.find('table',class_='table table-hover live-trading sortable')
headers=[i.text for i in table.find_all('th')]

data=[j for j in table.find_all('tr',{'class':["decrease-row","increase-row","nochange-row"]})]
# print(data)
result=[{headers[index]:cell.text for index,cell in enumerate(row.find_all('td'))} for row in data]
# fullname=[j.get('title') for j in table.find_all('a',{'target':'blank'})]

df=pd.DataFrame(result)
df
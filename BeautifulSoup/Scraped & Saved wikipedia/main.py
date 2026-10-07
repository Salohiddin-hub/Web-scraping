from bs4 import BeautifulSoup
import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd
url='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
page=requests.get(url, headers=header)
soup=BeautifulSoup(page.text, 'lxml')

table=soup.find('table', class_='wikitable')

world_titles=table.find_all('th')
title=[title.text.strip() for title in world_titles ]

df=pd.DataFrame(columns=title)
column_data=table.find_all('tr')

for row in column_data[1:]:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data ]

    if individual_row_data:
        length = len(df)
        df.loc[length] = individual_row_data

    
print(df)
df.to_csv(r"largest_companies.csv", index=False, encoding="utf-8-sig")

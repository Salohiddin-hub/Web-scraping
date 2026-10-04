from bs4 import BeautifulSoup
import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')

html_file=requests.get('http://quotes.toscrape.com/').text
soup=BeautifulSoup(html_file, 'lxml')
quotes=soup.find_all('div', class_="quote")
for quote in quotes:
    quote_text=quote.find('span', class_='text' ).text
    author=quote.find('small', class_='author').text
    keyword=quote.find('div', class_='tags').text.replace('Tags:', ' ').strip()    
    print(f'{quote_text} by \n{author}') 
    print(f'Tags: {keyword}\n')


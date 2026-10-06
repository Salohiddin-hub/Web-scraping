#Now let's step up to the exact pattern required for that client job: listing page extraction + deep detail page click-through.
# Target: books.toscrape.com
# Your Objective:
    # 1.Scrape the first books on the homepage.
    # 2.Extract top-level details from the catalog page: Title and Price.
    # 3.Extract the detail page URL (href), prepend the base URL ([http://books.toscrape.com/](http://books.toscrape.com/)), and make a second requests.get() call to open the book's individual page.
    # 4.Extract deep-level details from inside the detail page: UPC and Availability (e.g., "In stock (22 available)").
    # 5.Print all 4 data points per book. 
from bs4 import BeautifulSoup
import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')
from urllib.parse import urljoin

html_text=requests.get("https://books.toscrape.com/index.html").text
soup=BeautifulSoup(html_text,"lxml")
books=soup.find_all("article", class_="product_pod")[:5]

for index, book in enumerate(books):
    a_tag=book.h3.find('a')
    name=a_tag['title']
    price=book.find('p', 'price_color').text.replace('Â', "  ").strip()
    availability=book.find('p', 'instock availability').text.strip()
    
    print(f"{index}.Book name: {name}")
    print(f"Book price: {price}")
    
    details_link=book.find('a')
    details=details_link['href']
    base_url = "https://books.toscrape.com/"
    relative_url = details
    full_url = urljoin(base_url, relative_url)

    html_text_2=requests.get(full_url).text
    soup_2=BeautifulSoup(html_text_2, 'lxml')

    rows = soup_2.find_all('tr')
    upc = rows[0].find('td').text.strip()
    availability = rows[5].find('td').text.strip()

    print(f"UPC: {upc}")
    print(f"Availability: {availability}\n")

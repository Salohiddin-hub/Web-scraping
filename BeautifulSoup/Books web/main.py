from bs4 import BeautifulSoup
import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')

#Now let's step up to the exact pattern required for that client job: listing page extraction + deep detail page click-through.

# Target: books.toscrape.com

# Your Objective:

    # 1.Scrape the first books on the homepage.

    # 2.Extract top-level details from the catalog page: Title and Price.

    # 3.Extract the detail page URL (href), prepend the base URL ([http://books.toscrape.com/](http://books.toscrape.com/)), and make a second requests.get() call to open the book's individual page.

    # 4.Extract deep-level details from inside the detail page: UPC and Availability (e.g., "In stock (22 available)").

    # 5.Print all 4 data points per book. 

html_text=requests.get("https://books.toscrape.com/index.html").text
soup=BeautifulSoup(html_text,"lxml")
books=soup.find_all("ol", class_="row")

for book in books:
    a_tag=book.h3.find('a')
    name=a_tag['title']
    price=book.find('p', 'price_color').text.replace('Â', "  ").strip()
    availability=book.find('p', 'instock availability').text.strip()
    upc=book.find()
    print(name)
    print(price)
    print(availability)




  
    # print(name)

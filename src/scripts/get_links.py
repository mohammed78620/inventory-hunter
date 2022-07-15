import requests
from bs4 import BeautifulSoup

def filter_not_products():
    pass

url = 'https://www.scan.co.uk/search?q=3080'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101Firefox/50.0'}
source=requests.get(url, headers=headers).text
soup = BeautifulSoup(source, 'html.parser')

urls = []
unique_links = set()
for link in soup.find_all('a'):
    if all(i in link.get('href')for i in ["/products/","rtx"]):
        unique_links.add(f"https://www.scan.co.uk{link.get('href')}")

        # print(f"https://www.scan.co.uk{link.get('href')}")

for i in unique_links:
    print(i)






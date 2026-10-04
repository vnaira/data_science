import pandas as ps
import requests
from bs4 import BeautifulSoup

url='https://webscraper.io/web-scraper-extension'

response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")

table=soup.find('table')
print(table)
table_row = soup.find_all('tr')
data = []
for i,row in enumerate(table_row):
    cells = row.find_all('td')
    if cells:
        data.append({
            "Title": cells[0].text.strip(),
            "Price": cells[1].text.strip(),
            "Rating": cells[2].text.strip(),
            "Link": cells[3].text.strip(),
        })


df = ps.DataFrame(data)

print(df.head())
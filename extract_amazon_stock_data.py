import pandas as pd
from bs4 import BeautifulSoup
import requests

url=" https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"

response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")

tables = soup.find_all("table")
data =[]
for row in soup.find('tbody').find_all('tr'):
    cell = row.find_all('td')
    if cell:
        data.append({"Date":cell[0].text,"Open": cell[1].text, "High":cell[2].text, "Close":cell[4].text})

netflix_data = pd.DataFrame(data)
netflix_data.reset_index(inplace=True)
print(netflix_data.head())
netflix_data.to_csv("netflix_data.csv")

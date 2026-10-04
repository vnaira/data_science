import pandas as pd

url='https://webscraper.io/web-scraper-extension'

page = pd.read_html(url)
print(page)
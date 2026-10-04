import yfinance as yf
import requests
import pandas as pd
from bs4 import BeautifulSoup
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore", category=FutureWarning)

def make_graph(stock_data, revenue_data, stock):
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']

    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Stock price
    axes[0].plot(pd.to_datetime(stock_data_specific.Date), stock_data_specific.Close.astype("float"), label="Share Price", color="blue")
    axes[0].set_ylabel("Price ($US)")
    axes[0].set_title(f"{stock} - Historical Share Price")

    # Revenue
    axes[1].plot(pd.to_datetime(revenue_data_specific.Date), revenue_data_specific.Revenue.astype("float"), label="Revenue", color="green")
    axes[1].set_ylabel("Revenue ($US Millions)")
    axes[1].set_xlabel("Date")
    axes[1].set_title(f"{stock} - Historical Revenue")

    plt.tight_layout()
    plt.show()

# --------------Tesla---------------
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
print(tesla_data.head())

url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'

response = requests.get(url).text
tesla_soup = BeautifulSoup(response, "html.parser")
tesla_revenue = pd.DataFrame(columns= ["Date","Revenue"])

for row in tesla_soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    if col:
        date = col[0].text
        revenue = col[1].text

        tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame(
            {"Date": [date], "Revenue": [revenue]})], ignore_index=True)

tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(r',|\$',"",regex=True)
tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
print(tesla_revenue.tail())
make_graph(tesla_data, tesla_revenue, 'Tesla')

# ---------------GME--------------

gme= yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)
print(gme_data.head())

url2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

html_data_2 = requests.get(url2).text
gme_soup = BeautifulSoup(html_data_2, "html.parser")

gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in gme_soup.find_all("tbody")[1].find_all("tr"):
    cols = row.find_all("td")
    if cols:
        date = cols[0].text
        revenue = cols[1].text

        gme_revenue = pd.concat([gme_revenue, pd.DataFrame(
            {"Date": [date], "Revenue": [revenue]})], ignore_index=True)

gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(r',|\$',"",regex=True)

print(gme_revenue.tail())
make_graph(gme_data, gme_revenue, 'GameStop')









import yfinance
import pandas as pd
import bs4 as BeautifulSoup
import requests
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore",category =FutureWarning)

def make_graph(stock_data, revenue_data, stock):
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    # Stock price
    axes[0].plot(pd.to_datetime(stock_data_specific.Date), stock_data_specific.Close.astype("float"),
                 label="Share Price", color="blue")
    axes[0].set_ylabel("Price ($US)")
    axes[0].set_title(f"{stock} - Historical Share Price")

    # Revenue
    axes[1].plot(pd.to_datetime(revenue_data_specific.Date), revenue_data_specific.Revenue.astype("float"),
                 label="Revenue", color="green")
    axes[1].set_ylabel("Revenue ($US Millions)")
    axes[1].set_xlabel("Date")
    axes[1].set_title(f"{stock} - Historical Revenue")

    plt.tight_layout()
    plt.show()

# 1. Create an Empty DataFrame
# 2. Find the Relevant Table
# 3. Check for the Tesla Quarterly Revenue Table
# 4. Iterate Through Rows in the Table Body
# 5. Extract Data from Columns
# 6. Append Data to the DataFrame

tesla = yfinance.Ticker("TSLA")
tesla_data = tesla.history(period="max")
# Reset the index so "Date" becomes a regular column instead of the index
tesla_data.reset_index(inplace=True)
print(tesla_data.head())

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

# html_data = requests.get(url).text
# soup = BeautifulSoup(html_data, "html.parser")

# Create an empty DataFrame with the required columns
# tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
# for table in soup.find_all("table"):
#     if "Tesla Quarterly Revenue" in str(table):
#         for row in table.find("tbody").find_all("tr"):
#             cols = row.find_all("td")
#             if len(cols) >= 2:
#                 date = cols[0].text
#                 revenue = cols[1].text
#                 new_row = pd.DataFrame({"Date": [date], "Revenue": [revenue]})
#                 tesla_revenue = pd.concat([tesla_revenue, new_row], ignore_index=True)



# Alternative
tables = pd.read_html(url)
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for table in tables:
    if "Tesla Quarterly Revenue" in table.to_string():
        tesla_revenue = table
        break

tesla_revenue.columns = ["Date", "Revenue"]
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(r'[\$,]', "", regex=True)
tesla_revenue.dropna(inplace=True)

print(tesla_revenue.tail())
make_graph(tesla_data, tesla_revenue, 'Tesla')


# ------------------GME----------------

# gme= yfinance.Ticker("GME")
# gme_data = gme.history(period="max")
# # Reset the index so "Date" becomes a regular column instead of the index
# gme_data.reset_index(inplace=True)
# html_data_2= pd.read_html(' https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html')
# soup_2 = BeautifulSoup(html_data_2, "html.parser")

# gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"",regex=True)


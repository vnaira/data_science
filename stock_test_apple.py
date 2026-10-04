import requests
import json
import yfinance as yf
from matplotlib import pyplot as plt

# url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json"
#
# response = requests.get(url)

# with open("apple.json", "wb") as f:
#     f.write(response.content)


apple = yf.Ticker("AAPL")
with open("apple.json", "r") as json_file:
    apple_info = json.load(json_file)

apple_share_price_data = apple.history(period="max")
apple_share_price_data.reset_index(inplace=True)
apple_share_price_data.plot(x="Date", y="Open", kind="line")
# plt.show()
apple.dividends.plot()
plt.show()
# print(apple_info['country'])
print(apple_share_price_data.head())


import yfinance as yf
import requests
import json

amd = yf.Ticker("AMD")
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json"

response = requests.get(url)
#
# with open('amd.json', "wb") as f:
#     f.write(response.content)

with open("amd.json", "r") as f:
    amd_info = json.load(f)

print(amd_info['country'])
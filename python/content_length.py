import requests

url = "http://stock.gtimg.cn/data/index.php?appn=detail&action=data&c=sh600000&p=99"

payload = {}
headers = {
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
  'Sec-Fetch-User': '?1',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Sec-Fetch-Site': 'none',
  'Sec-Fetch-Mode': 'navigate',
  "Range": "bytes=0-1"
}

# response = requests.head(url, headers=headers, data = payload)
response = requests.request("GET",url, headers=headers, data = payload)

if response.text[0]:
    print(True)
else:
    print(False)
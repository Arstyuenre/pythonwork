import requests
url = "https://item.jd.com/100016558780.html"
try:
    p = requests.get(url)
    p.raise_for_status()
    p.encoding = p.apparent_encoding
    print(len(p.text))
    print(p.text)
except:
    print("爬取页面失败！")
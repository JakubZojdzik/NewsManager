import requests
from bs4 import BeautifulSoup

page_url = "https://www.polsatnews.pl/"
userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
headers = {'User-Agent': userAgent}
page = requests.get(page_url, headers=headers)
effect = BeautifulSoup(page.content, 'html.parser')
h1 = effect.find("h1")
h2 = effect.find_all("h2", {"class": "news__title"})
print(h1.get_text())
print()
i = 1
for h in h2:
    if i > 10:
        break
    print(h.get_text())
    i += 1

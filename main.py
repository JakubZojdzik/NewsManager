import requests
from bs4 import BeautifulSoup as bs

userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
headers = {'User-Agent': userAgent}

page_url = "https://www.polsatnews.pl/"
page = requests.get(page_url, headers=headers)
effect = bs(page.content, 'html.parser')
main1 = effect.find("h1", {"class": "news__title"}).get_text()
commons = effect.find_all("h2", {"class": "news__title"})


page_url = "https://tvn24.pl/polska/"
page = requests.get(page_url, headers=headers)
effect = bs(page.content, "html.parser")
main2 = effect.find("h2", {"class": "heading article-title"}).get_text()


print("BREAKING NEWS:\nPolsat News:\t", main1, "\nTVN24:\t\t\t", main2)
print()
print("Common news:")
for i in range(3):
    print(commons[i].get_text())

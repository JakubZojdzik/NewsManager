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
odp = -1
position = 0  # 0 - menu, 1 - details
content = ""

while True:
    print("\033c", end="")
    if not position:
        print("(A) BREAKING NEWS:\n1.\t", main1, "\n2.\t", main2)
        print()
        print("(B) Common news:")
        for i in range(3):
            print(str(i + 1) + ".\t", commons[i].get_text())
        print()
        print("To see more details of breaking news type A and 1 or 2, depends which one you want to read.")
        print("In order to read more about common newses type B, and 1, 2, or 3.")
        odp = input()

        if odp == "A1" or odp == "a1" or odp == "A 1" or odp == "a 1":
            position = 1
            html = bs(requests.get("https://www.polsatnews.pl/", headers=headers).content, 'html.parser').find("a", {"class": "news__link"})
            html = str(html)[28:]
            link = ""
            for i in range(len(html)):
                if html[i] != '"':
                    link += html[i]
                else:
                    break
            content = bs(requests.get(link, headers=headers).content, 'html.parser').find("div", {"class": "news__preview"}).get_text()

        if odp == "A2" or odp == "a2" or odp == "A 2" or odp == "a 2":
            position = 1
            html = bs(requests.get("https://tvn24.pl/polska/", headers=headers).content, 'html.parser').find_all("a", {"role": "presentation"}, {"target": "_self"})
            html = str(html[64])[39:]

            link = ""
            for i in range(len(html)):
                if html[i] != '"':
                    link += html[i]
                else:
                    break

            content = bs(requests.get(link, headers=headers).content, 'html.parser').find("p", {"class": "lead-text"}).get_text()
        if odp == "B1" or odp == "b1" or odp == "B 1" or odp == "b 1":
            position = 1
            html = bs(requests.get("https://www.polsatnews.pl/", headers=headers).content, 'html.parser').find_all("a", {"class": "news__link"})
            html = str(html[1])[28:]

            link = ""
            for i in range(len(html)):
                if html[i] != '"':
                    link += html[i]
                else:
                    break
            content = bs(requests.get(link, headers=headers).content, 'html.parser').find("div", {"class": "news__preview"}).get_text()

        if odp == "B2" or odp == "b2" or odp == "B 2" or odp == "b 2":
            position = 1
            html = bs(requests.get("https://www.polsatnews.pl/", headers=headers).content, 'html.parser').find_all("a", {"class": "news__link"})
            html = str(html[2])[28:]

            link = ""
            for i in range(len(html)):
                if html[i] != '"':
                    link += html[i]
                else:
                    break
            content = bs(requests.get(link, headers=headers).content, 'html.parser').find("div", {"class": "news__preview"}).get_text()
        if odp == "B3" or odp == "b3" or odp == "B 3" or odp == "b 3":
            position = 1
            html = bs(requests.get("https://www.polsatnews.pl/", headers=headers).content, 'html.parser').find_all("a", {"class": "news__link"})
            html = str(html[3])[28:]

            link = ""
            for i in range(len(html)):
                if html[i] != '"':
                    link += html[i]
                else:
                    break
            content = bs(requests.get(link, headers=headers).content, 'html.parser').find("div", {"class": "news__preview"}).get_text()
    else:
        print(content)
        print()
        print("In order to get back to main menu, type any character")
        odp = input()
        position = 0


































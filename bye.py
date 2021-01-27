import requests
import bs4
baseurl=" http://quotes.toscrape.com/page/{}/"
# res=requests.get(baseurl)
# soup=bs4.BeautifulSoup(res.text,"lxml")
# author=soup.select(".author")
# for item in author:
#     print(item.text)
#
# quote=soup.select(".text")
# lis=[]
# for each in quote:
#     lis.append(each.text)
#
# print(*lis,sep="\n")
# tagitem=soup.select(".tag-item")
# letag=len(tagitem)
# for item in range(len(tagitem)):
#     print(tagitem[item].text)
uniauthors=[]
for n in range(1,11):
    page=baseurl.format(n)
    res=requests.get(page)

    soup=bs4.BeautifulSoup(res.text,"lxml")
    author=soup.select(".author")
    for every in author:
        if every.text not in uniauthors:
            uniauthors.append(every.text)
            uniauthors.sort()
        else:
            pass
print(uniauthors,sep="\n")

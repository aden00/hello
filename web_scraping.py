import requests
import bs4
baseurl="http://books.toscrape.com/catalogue/page-{}.html"
res=requests.get(baseurl.format(1))
lxmlread=bs4.BeautifulSoup(res.text,"lxml")


all_product_pod=lxmlread.select(".product_pod")
example=all_product_pod[0]
# test=example.select(".star-rating.Three")

two_star_titles=[]
for n in range(1,51):

    scrapeurl=baseurl.format(n)
    res2=requests.get(scrapeurl)

    soup=bs4.BeautifulSoup(res2.text,"lxml")
    all_product=soup.select(".product_pod")
    for book in all_product:
        if len(book.select(".star-rating.Five")) != 0:
            book_title=book.select('a')[1]["title"]
            two_star_titles.append(book_title)
print(*two_star_titles,sep="\n")















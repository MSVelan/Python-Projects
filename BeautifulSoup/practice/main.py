from bs4 import BeautifulSoup

import requests
response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

articles = [i.a for i in soup.find_all(name="span", class_="titleline")]
titles = [a.getText() for a in articles]
links = [a.get("href") for a in articles]
article_upvotes = [a.getText() for a in soup.find_all(name="span", class_="score")]
scores = [int(upvote.split()[0]) for upvote in article_upvotes]
# print(scores)

zipped = list(zip(scores, titles, links))
result = sorted(zipped, key=lambda x: x[0], reverse=True)
scores, titles, links = zip(*result)
print(scores)
print("\n")
print(titles)
print("\n")
print(links)
print("\n")



'''
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname,'./website.html')
file1 = open(file=filename, mode='r', encoding='utf-8')
s = file1.read()
soup = BeautifulSoup(s,'html.parser')
# print(soup.title.string)
# print(soup.prettify())
all_anchor_texts = [a.getText() for a in soup.find_all(name="a")]
all_anchor_links = [a.get("href") for a in soup.find_all(name="a")]
# print(all_anchor_links)

heading = soup.find(name="h1",id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

company_url = soup.select_one(selector="p a")
# print(company_url)

name = soup.select_one(selector="#name")
# print(name)

headings = soup.select(".heading")
print(headings)
file1.close()
'''
import requests
from bs4 import BeautifulSoup
import json
data = {}
postIndex = 1

firstpost = "https://www.commitstrip.com/en/2012/09/03/best-of-les-codeurs-au-cinema-avatar/"
r = requests.get(firstpost)
soup = BeautifulSoup(r.content, features="html.parser")
title = soup.find("h1", class_="entry-title").text
datetime = soup.find("time", class_="entry-date")
imageDiv = soup.find("div", class_="entry-content")
if(imageDiv.find("img")):
    imgSrc =  imageDiv.find("img")['src']
elif(soup.find("img", class_="size-full")):
    imgSrc = soup.find("img", class_="size-full")['src']
else:
    imgSrc=""
postData = {"title":title, "datetime":datetime['datetime'], "date":datetime.text, "imageLink":imgSrc, "postLink":firstpost}
data[str(postIndex)] = postData
spanNext = soup.find("span", class_="nav-next")
if(spanNext.find("a")):
    print(spanNext.find("a")['href'])
else:
    print("done")
print(postData)

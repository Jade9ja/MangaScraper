from bs4 import BeautifulSoup as bs
from helper import *
import requests
print("Enter manga name:")
query = input()
print("Enter Chapter number: (press enter to skip)")
chap = int(input())
url = manga_url(query,chap)
print(url)
stat = status(url)
if stat:
    print('Chapter not available yet..')
    exit()

print("Do you want to download all chapters after the selected one? (1 = Yes,0 = No)")
allchaps = int(input())
def redloader(name,chap):
    currentpage = 1
    dlpath = download_loc(name,chap)

    if status(url):
        print('Chapter not available yet..')
        return None
    print(f"Downloading chapter #{chap}.. ")
    while True:
        pageurl = url + '/' + str(currentpage)
        request = req(pageurl)
        raw = request.text

        if request.status_code != 200 or not len(raw):
            print("Does not exist!" if not len(raw) else "Operation Complete!")
            break
        
        parsed = bs(raw,"html.parser")
        img_url = parsed.find("img",{"id":"img"}).get("src")
        dload_pages(img_url,dlpath,currentpage)

        currentpage += 1
redloader(query.lower().replace(" ","-"),chap)







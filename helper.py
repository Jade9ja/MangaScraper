import requests
import shutil
import os
from config import *
def download_loc(seriesname,chapter):
    return DLOAD_PATH + seriesname + '/Chapter' + str(chapter) + '/'

def manga_url(query,chapter = 1):
    print('Select a provider: (input the corresponding number!)')
    cnt = 1
    for i in PROVIDERS:
        print(str(cnt) + ')' + i + '\n')
        cnt += 1
    sel = input()
    return PROVIDERS[int(sel) - 1] + query.lower().replace(" ","-") + '/' + str(chapter)

def req(url, binary = False):
    try:
        request = requests.get(url, stream = binary)
    except:
        print("Interrupt (HTTP error or force stop) \n exiting..")
        exit()
    return request

def status(url):
    resp = req(url, True).text
    return OHO in resp

def dload_pages(url,dloadpath,current_page):
    if not os.path.exists(dloadpath):
        os.makedirs(dloadpath)
    
    img_ren = str(current_page) + '.jpg'
    img_path = dloadpath + img_ren
    request = req(url, True)
    with open(img_path,'wb') as file_path:
        request.raw.decode_content = True
        shutil.copyfileobj(request.raw,file_path)
    print('Downloaded page #' + str(current_page))



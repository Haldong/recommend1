from bs4 import BeautifulSoup
import urllib.request
import os
import re
from random import randint
from time import sleep
path = "c:/python/S2McH/booklist"
if os.path.exists(path) == False:
    os.makedirs(path)
    os.chdir(path)
    print(path)
else:
    os.chdir(path)

html = "http://www.gutenberg.org/browse/scores/top"
data = urllib.request.urlopen(html) ####################
soup = BeautifulSoup(data)
txt_part = soup.find("ol")
tag_list = txt_part.findAll("li")

url_num_list = []
number = ["%.3d" % i for i in range(1,len(tag_list)+1)]
tag = zip(tag_list, number)
for url, num in tag :
    url_num = re.search("[0-9]+",url.find("a")["href"]).group(0)
    final_url = "http://www.gutenberg.org/ebooks/"+url_num+".txt.utf-8"
    url_num_list.append([num, url_num, url.text, final_url])


for book in url_num_list[29:100]:
    try:
        data = urllib.request.urlopen(book[3]).read() ####################
    except:
        html = "http://www.gutenberg.org/files/" + str(book[1]) +"/" +str(book[1])+"-0.txt"
        data = urllib.request.urlopen(html).read() ####################
    f = open(str(book[0])+"_"+book[2].replace(":","-").replace(".",",")+".txt", "wb")
    f.write(data)
    f.close()
    print("[", book[0], "/", len(url_num_list), "]" , book[2])
    sleep(randint(20, 50))




import requests
import time
from bs4 import BeautifulSoup
import urllib.request
import re
import json
start_time = time.time()
link_3 = []
link_4 = []
link_5 = []
link_6 = []
links = []

g = ""
b = ""
d = ""
y = ""
ya = ""
ask = ""
domain = ""
emails = []
new_emails = []
mails = []


def crawl(request_url):
    try:
        response = requests.get(request_url)
        new_emails = re.findall(r"[a-z0-9\.\-+_]+@" + domain, response.text)
        if new_emails:
            emails.append(new_emails)
    except:
        pass
    return emails

   
if __name__ == '__main__':
    
    domain = input("enter the domain:")
    d = domain
    url = 'https://duckduckgo.com/?q=email+"%40"+++'+d+'+++""&ia=web&count=50&first=51'
    
    requestd = urllib.request.Request(url)
    responsed = urllib.request.urlopen(requestd)
    html_paged = responsed.read()
    soupd = BeautifulSoup(html_paged, "lxml")
    for link in soupd.findAll('a'):
        link_d = link.get('href')
        d1 = link_d
        link_3.append(d1)

    y = domain
    url = 'https://in.search.yahoo.com/search?p=%5B%40"%20+%20'+y+'%20+%20"%5D&pz=100'
    
    request_y = urllib.request.Request(url)
    response_y = urllib.request.urlopen(request_y)
    html_page_y = response_y.read()
    soupy = BeautifulSoup(html_page_y, "lxml")
    for link in soupy.findAll('a'):
        link_y = link.get('href')
        y1 = link_y
        link_4.append(y1)

    ya = domain
    url = 'https://yandex.com/search/?text="%40"%20%20%20'+ya+'%20%20%20""&lr=20983'
    
    request_ya = urllib.request.Request(url)
    response_ya = urllib.request.urlopen(request_ya)
    html_page_ya = response_ya.read()
    soup_ya = BeautifulSoup(html_page_ya, "lxml")
    for link in soup_ya.findAll('a'):
        link_ya = link.get('href')
        ya1 = link_ya
        link_5.append(ya1)

    ask = domain
    url = "https://www.ask.com/web?q=email+"+ask+"&o=0&qo=homepageSearchBox"
    
    request_ask = urllib.request.Request(url)
    response_ask = urllib.request.urlopen(request_ask)
    html_page_ask = response_ask.read()
    soup_ask = BeautifulSoup(html_page_ask, "lxml")
    for link in soup_ask.findAll('a'):
        link_ask = link.get('href')
        ask1 = link_ask
        link_6.append(ask1)

    links = link_3 + link_4 + link_5 + link_6
    nodup_link = list(set(links))
    filtered_links = [i for i in nodup_link if re.search("http", i)]
    final_links = list(set(filtered_links))
    mails = [crawl(f) for f in final_links]
    flat_lists = mails

    final_emails = []
    for flat_list in flat_lists:
        item_list = list(set(flat_list))
        for item in item_list:
            if item not in final_emails:
                final_emails.append(item)
    print(final_emails)
    data = {}
    data.update({
        'domain': domain,
        'mails': seen
    })
    with open('data1.json', 'w') as outfile:
        json.dump(data, outfile)
    print("--- %s seconds ---" % (time.time() - start_time))
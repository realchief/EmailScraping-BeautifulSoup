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


def get_links(url):
    link_result = []
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    html_page = response.read()
    soup = BeautifulSoup(html_page, "lxml")
    for link in soup.findAll('a'):
        d = link.get('href')
        link_result.append(d)
    return link_result

   
if __name__ == '__main__':
    
    domain = input("enter the domain:")

    url_d = 'https://duckduckgo.com/?q=email+"%40"+++'+domain+'+++""&ia=web&count=50&first=51'
    link_3 = get_links(url_d)

    url_y = 'https://in.search.yahoo.com/search?p=%5B%40"%20+%20'+domain+'%20+%20"%5D&pz=100'
    link_4 = get_links(url_y)

    url_ya = 'https://yandex.com/search/?text="%40"%20%20%20'+domain+'%20%20%20""&lr=20983'
    link_5 = get_links(url_ya)

    url_ask = "https://www.ask.com/web?q=email+"+domain+"&o=0&qo=homepageSearchBox"
    link_6 = get_links(url_ask)

    links = link_3 + link_4 + link_5 + link_6
    nodup_link = list(set(links))
    filtered_links = [i for i in nodup_link if re.search("http", i)]
    final_links = list(set(filtered_links))
    mails = [crawl(f) for f in final_links]

    final_emails = []
    for flat_lists in mails:
        for flat_list in flat_lists:
            item_list = list(set(flat_list))
            for item in item_list:
                if item not in final_emails:
                    final_emails.append(item)
    print(final_emails)
    data = {}
    data.update({
        'domain': domain,
        'mails': final_emails
    })
    print(data)
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
    # print("--- %s seconds ---" % (time.time() - start_time))

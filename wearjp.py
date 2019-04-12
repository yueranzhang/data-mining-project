import requests
from bs4 import BeautifulSoup
import time
import random
import re

time1 = time.time()
set_link_list = []


# basic crawling function
def crawling(link):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        r = requests.get(link, headers=headers, timeout=20)
        html = r.text
        html_data = BeautifulSoup(html, 'html.parser')
        return html, html_data
    except Exception as e:
        print('该地址下载失败: ', link)
        print(e)


# crawling first n pages
def get_sets(pages):
    for i in range(1, pages):
        main_site_link = 'https://wear.jp/coordinate/?pageno=' + str(i)
        main_site_data = crawling(main_site_link)[1]

        # get individual links from shopping guides
        set_divs = main_site_data.find_all(name="div", attrs={"class": "image"})
        for set_div in set_divs:
            set_link_text = set_div.find_all(name="a")
            set_links = [l['href'] for l in set_link_text]
            for set_link1 in set_links:
                set_link = "https://wear.jp" + set_link1
                set_link_list.append(set_link)

        # sleep
        sleep_time = random.randint(0, 1)
        time.sleep(sleep_time)


# get pics from web pages and save
def get_pic(link):
    img_set = []
    set_data = crawling(link)[1]
    section = set_data.find(name="section", attrs={"id": "item", "class": "content_bg"})
    img = section.find_all(name="img")
    for i in img:
        img_address = i['src']
        img_set.append(img_address)
    return img_set


get_sets(2)
time2 = time.time()
total_time = time2 - time1
print(total_time)
pic_set = {}
i = 0
for set_link in set_link_list:
    pic_set[i] = get_pic(set_link)
    i += 1
print(pic_set)

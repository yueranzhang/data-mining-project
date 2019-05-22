import os
import random
import time

import requests
from bs4 import BeautifulSoup


# basic crawling function
def crawling(link):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        r = requests.get(link, headers=headers, timeout=20)
        html = r.text
        html_content = r.content
        html_data = BeautifulSoup(html, 'lxml')
        return html_content, html_data
    except Exception as e:
        print('filed to download: ', link)
        print(e)


# crawling first n pages, 生成set link list
def get_sets(page_num):
    set_link_list = []
    for i in range(1, page_num + 1):
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
        sleep_time = random.randint(0, 1) + random.random()
        time.sleep(sleep_time)
        return set_link_list


#  pic address,
def get_pic(link):
    img_set = []
    set_data = crawling(link)[1]
    section = set_data.find(name="section", attrs={"id": "item", "class": "content_bg"})
    img = section.find_all(name="img")
    for i in img:
        img_address = 'http:' + i['src']
        img_set.append(img_address)

    return img_set


def save_pic(link):
    for each in link:
        filename = each.split('/')[-1]

        img = crawling(each)[0]
        with open(filename, 'wb')as f:
            f.write(img)


def download_pic(link, page_num):
    page = str(page_num)
    folder = page
    os.mkdir(folder)
    os.chdir(folder)

    save_pic(link)
    os.chdir('..')


def get_shopadd(link):
    shop_set = []
    set_data = crawling(link)[1]
    section = set_data.find(name="section", attrs={"id": "item", "class": "content_bg"})
    section = section.find_all(name='div', attrs={'class': 'sub'})
    for i in section:
        shop_web = i.find(name='a')
        shop_address = 'http://wear.jp' + shop_web['href']
        shop_set.append(shop_address)

    return shop_set

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
def get_sets(n):
    for i in range(1, n):
        main_site_link = 'https://wear.jp/coordinate/?pageno=' + str(i)
        main_site_data = crawling(main_site_link)[1]

        # get individual links from shopping guides
        set_divs = main_site_data.find_all(name="div", attrs={"class": "image"})
        for set_div in set_divs:
            set_link_text = set_div.find_all(name="a")
            set_links = [l['href'] for l in set_link_text]
            set_link_list.append(["https://wear.jp" + set_link for set_link in set_links])

        # sleep
        sleep_time = random.randint(0, 1)
        time.sleep(sleep_time)


get_sets(2)
time2 = time.time()
total_time = time2 - time1
print(set_link_list)
print(total_time)

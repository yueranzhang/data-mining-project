import requests
from bs4 import BeautifulSoup
import time
import random
import re

time1 = time.time()
set_name_list = []
set_link_list = []
# basic crawling function
def crawling(link):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        r = requests.get(link, headers=headers, timeout=20)
        html = r.text
        html_data = BeautifulSoup(html, 'lxml')
        return html, html_data
    except Exception as e:
        print('该地址下载失败: ', link)
        print(e)


# crawling first n pages
def get_sets(n):
    for i in range(1, n):
        main_site_link = 'https://keikolynn.com/category/style/shopping-guides/page/' + str(i) + '/'
        main_site_data = crawling(main_site_link)[1]

        # get individual names from shopping guides
        setting_names = main_site_data.find_all("h2", class_="page-title")
        for i in range(len(setting_names)):
            set_name = setting_names[i].a
            set_name_list.append(set_name)

        # get individual links from shopping guides
        html = crawling(main_site_link)[0]
        set_link = re.findall('<h2 class="page-title"><a href="(https://keikolynn.com/[^:#=<>]*?)".*?</a></h2>',
                                   html)
        set_link_list.append(set_link)
        # crawling each links in the link list

        #sleep
        sleep_time = random.randint(0, 2) + random.random()
        time.sleep(sleep_time)


get_sets(5)
print(set_name_list)
print(set_link_list)

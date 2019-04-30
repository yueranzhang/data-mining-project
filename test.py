import requests
from bs4 import BeautifulSoup
import time
import random
import os



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
        print('该地址下载失败: ', link)
        print(e)


# crawling first n pages
def get_sets(n):
    set_link_list = []
    for i in range(1, n+1):
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
#  pic address and purchasing address
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
    section = section.find_all(name = 'div', attrs={'class':'sub'})
    for i in section:
        shop_web = i.find(name = 'a')
        shop_address = 'http://wear.jp' + shop_web['href']
        shop_set.append(shop_address)

    return shop_set

if __name__ == "__main__":
    pic_list = []
    shop_list = []

    set_link_list = get_sets(1)
    print(set_link_list)

    page_num = 0
    for count in set_link_list:
        page_num += 1
        i = get_pic(count)
        download_pic(i, page_num)
        for each in i:
            name = each.split('/')[-1]
            print(name, '\n')
            pic_list.append(name)

    for count in set_link_list:
        i = get_shopadd(count)
        print(i,'\n')
        shop_list.extend(i)

    info = {}.fromkeys(pic_list)
    i = 0
    for key, value in info.items():
        info[key] = shop_list[i]
        i += 1

    print(info)
#   page_num = 0
#   for add in set_link_list:
#       page_num += 1
#       i = get_pic(add)
#       download_pic(i, page_num)



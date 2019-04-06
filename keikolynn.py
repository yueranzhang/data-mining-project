import requests
from bs4 import BeautifulSoup
import time

time1 = time.time()

#basic crawling function
def crawling(link):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        r = requests.get(link, headers=headers, timeout=20)
        html_data = BeautifulSoup(r.text, 'lxml')
        return html_data
    except Exception as e:
        print('该地址下载失败: ', url)
        print(e)
for i in range(1,10):
    main_site_links='https://keikolynn.com/category/style/shopping-guides/page/'+str(i)+'/'
    main_site_data = crawling(main_site_links)
    print(main_site_data)

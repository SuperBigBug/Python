import requests
import bs4
import re
import os

def getList():
    root = "http://qilingbaluo.com/pw/thread.php?fid=114"
    req = requests.get(root)
    req.encoding = 'gb2312'

    html = req.text

    bs = bs4.BeautifulSoup(html, 'html.parser')

    target = bs.find_all("tr", {"class": {"tr3 t_one"}})
    # print(target)

    prefix = "http://qilingbaluo.com/pw/"

    a = []
    for each in target:
        # print(each.find('a').get('href'))
        url = prefix + each.find('a').get('href')
        if len(url) < 56:
            continue

        a.append(prefix + each.find('a').get('href'))
    return a



# url = "http://qilingbaluo.com/pw/html_data/14/2008/4925219.html"
#
# req = requests.get(url)
# req.encoding = 'gb2312'
#
# html = req.text
#
# #http://qilingbaluo.com/pw/html_data/14/2008/4925219.html
# #https://www.cnblogs.com/MingGyGy-Castle/p/11962188.html
#
# bs = bs4.BeautifulSoup(html, 'html.parser')
#
# target_rl = bs.find_all('img')
#
# imgUrl = []
# for a in target_rl:
#     if re.match(r'^https?:/{2}\w.+$', a.get('src')):
#         #imgUrl.append(a.get('src'))
#         # 图片地址
#         url = a.get('src')
#         # print(a.get('src'))
#         with open("E:\\pic\\"+os.path.basename(url), 'wb') as f:
#             f.write(requests.get(url).content)
#         print("save success")
#

def getAndSave(url):
    req = requests.get(url)
    req.encoding = 'gb2312'

    html = req.text

    #http://qilingbaluo.com/pw/html_data/14/2008/4925219.html
    #https://www.cnblogs.com/MingGyGy-Castle/p/11962188.html

    bs = bs4.BeautifulSoup(html, 'html.parser')

    target_rl = bs.find_all('img')

    imgUrl = []
    for a in target_rl:
        if re.match(r'^https?:/{2}\w.+$', a.get('src')):
            #imgUrl.append(a.get('src'))
            # 图片地址
            url = a.get('src')
            # print(a.get('src'))
            with open("D:\\pic\\"+os.path.basename(url), 'wb') as f:
                f.write(requests.get(url).content)
            print("save success")

list = getList()
for page in list:
    print(page)
    getAndSave(page)
#getAndSave("http://qilingbaluo.com/pw/html_data/14/2008/4925219.html")
import requests
import bs4
import re

def getLinks():
    url ="http://qilingbaluo.com/pw/thread.php?fid=3"

    req = requests.get(url)
    req.encoding = 'utf-8'

    html = req.text

    bs = bs4.BeautifulSoup(html, 'html.parser')

    target = bs.find_all("tr", {"class": {"tr3 t_one"}})
    # print(target)
    prefix = "http://qilingbaluo.com/pw/"

    links = []
    for list in target:
        url = prefix + list.find('a').get('href')
        if len(url) < 55 or url == "http://qilingbaluo.com/pw/html_data/3/1903/3940867.html":
            continue
        links.append(url)
    return links

def getTargetUrl(url):
    # res = getLinks()
    #print(res)

    # url = "http://qilingbaluo.com/pw/html_data/3/2008/4925918.html"

    req = requests.get(url)
    req.encoding = 'gb2312'

    html = req.text

    bs = bs4.BeautifulSoup(html, 'html.parser')
    target = bs.find("div", {"class": {"tpc_content"}}).find_all('a')
    list = []
    for each in target:
        #cprint(each.get('href'))
        #print(len(each.get('href')))
        if len(each.get('href')) < 70:
            continue
        #print(each.get('href'))
        list.append(each.get('href'))

    return list

def start():
    print("start...")

    # 保存所有磁力链链接页面
    destination = []

    urls = getLinks()
    for url in urls:
        a = getTargetUrl(url)
        for d in a:
            if "jpg" in d:
                continue
            #print(d)
            ma = getManage(d)
            print(ma)

            with open("D:\\test.txt", 'w', encoding='utf-8') as file:

                file.write('\n'+ma)

                file.write('\n' + '=' * 50 + '\n')
            destination.append(ma)



def getManage(url):

    req = requests.get(url)
    req.encoding = 'gb2312'
    html = req.text

    bs = bs4.BeautifulSoup(html, 'html.parser')
    res = bs.find("a",{"class":{"uk-button"}}).get('href')
    return res

start()
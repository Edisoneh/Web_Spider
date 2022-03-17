import json
import re
import requests
import datetime
from bs4 import BeautifulSoup
import os

##目的是爬取豆瓣书评Top250的数据 In order to requests douban top 250 books datas
def Crawl_douban_booktop250_data():
    headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    url='https://book.douban.com/top250'

    try:

        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        #print(soup)
        tables = soup.find_all('table')
        #print(tables)
        books=[]
        #print(len(tables))
        for table in tables:
            book = {}
            bs = BeautifulSoup(str(table),'lxml')
            all_trs=bs.find_all('tr')
            #print(all_trs)
            #print(all_trs)

            for tr in all_trs:
                all_tds=tr.find_all('td')
                for td in all_tds:

                    if td.find_next('div',class_="star clearfix"):
                        #print(td.find_next('div',class_="star clearfix").find_previous('p',class_="pl").text.split('/')[0].replace("著",""))
                        book["writer"]=td.find_next('div',class_="star clearfix").find_previous('p',class_="pl").text.split('/')[0].replace("著","")

                    if td.find('a',class_="nbg"):
                        book["img_link"]=td.find('a',class_="nbg").find('img').get('src')
                    if td.find('div',class_="pl2"):
                        book_name=td.find('div',class_="pl2").find('a').text.replace("\n","")
                        book_name=book_name.replace(" ","")
                        book["book_name"]=book_name
                    if td.find('div',class_="pl2"):
                        book["book_link"]=td.find('div',class_="pl2").find('a').get('href')
                        #print(td.find('div',class_="pl2").find('a').get('href'))
                    if td.find('div',class_='star clearfix'):
                        #print(td.find('div',class_='star clearfix').find('span',class_="rating_nums").text)
                        book["grade"]=td.find('div',class_='star clearfix').find('span',class_="rating_nums").text
                        ev_number=td.find('div',class_='star clearfix').find('span',class_="pl").text
                        ev_number=ev_number.replace("\n","")
                        book["ev_number"]=ev_number.replace(" ", "").replace("(", "").replace(")", "").replace("人评论","")
                        #print(book["ev_number"])
                        represent_ev= td.find('p',class_='quote').find('span',class_="inq").text
                        book["quote"]=represent_ev
                    #print(book)
            books.append(book)

        #print(books)
        #print(len(books))
        json_data = json.loads(str(books).replace("\'","\""))
        with open('work/'+'books.json','w',encoding='UTF-8') as f:
            json.dump(json_data,f,ensure_ascii=False)

                        #print(td.find('div',class_='star clearfix').find('span',class_="pl").text)
    except Exception as e:
        print(e)
def Crawl_everytopbook_data():
    with open('work/' + 'books.json', 'r', encoding='UTF-8') as file:
        json_array = json.loads(file.read())

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    book_infos = []
    for book in json_array:
        book_info = {}
        name = book['book_name']
        book_info["book_name"]=book['book_name']
        book_info["writer"]=book['writer']
        book_info["grade"]=book['grade']
        book_info["ev_number"]=book['ev_number']
        book_info["quote"]=book['quote']

        #print(name)
        link = book['book_link']
        #print(link)

        response = requests.get(link,headers=headers)

        bs=BeautifulSoup(response.text,'lxml')
        #print(bs.find_all('div',class_='subject clearfix'))
        divs_subject_clearfix=bs.find('div',class_="subject clearfix")
        divs_info=divs_subject_clearfix.find('div',id="info")

        lis=[]
        for span in divs_info:
            #print(span)
            #print(111)

            lis.append("".join(str(span.text).split()))

        lis=[x for x in lis if x!='']
        # print(len(lis))
        # print(lis)

        for i in range(0,len(lis)):
            if("出版社:" == lis[i]):
                #print(lis[i])
                book_info["publisher"]=lis[i+1]
                #print(lis[i+1])
            if("出版年" in lis[i]):
                #print(lis[i])
                book_info["imp"]=lis[i+1]
                #print(lis[i+1])
            if("页数" in lis[i]):
                #print(lis[i])
                book_info["number_of_pages"]=lis[i+1]
                #print(lis[i+1])
            if("定价" in lis[i]):
                #print(lis[i])
                book_info["cost"]=lis[i+1]
                #print(lis[i+1])
            if("丛书:" == lis[i]):
                #print(lis[i])
                book_info["seris"]=lis[i+1]
                #print(lis[i+1])
            if("ISBN" in lis[i]):
                book_info["ISBN"]=lis[i+1]
        #
        book_infos.append(book_info)
        pic_url=book["img_link"]
        #down_save_pic(book['book_name'],pic_url)
        print(str(book["book_name"])+"image down load")


    json_data = json.loads(str(book_infos).replace("\'", "\""))
    with open('work/' + 'every_book.json', 'w', encoding='UTF-8') as f:
        json.dump(json_data, f, ensure_ascii=False)

            #print(span)
            #print(111)




            #print(111)
            #total.join(str(span.text).split())


            #print(author)


            # if chinese_author in author:
            #     print(author)
            #     print(author.replace("作者:",""))
            # if("".join(str(span.text).split()).find('作者')):
            #     print("".join(str(span.text).split()))
        # print(total)
        #print(spans)
        # spans=divs.find('div',id_="info")
        # print(spans)
        # for span in spans:
        #     #print(span.text)
        #     if(span.text=="页数"):
        #         print('yeshu')
        #     print("".join(str(span.text).split()))
        # spans=divs.find_all('span')
        # for span in spans:
        #     print(span.text)
def down_save_pic(name,pic_urls):
    print(pic_urls)
    '''
    根据图片链接列表pic_urls, 下载所有图片，保存在以name命名的文件夹中,
    '''
    path = 'work/'+'pics/'+name+'/'
    if not os.path.exists(path):
      os.makedirs(path)

    try:
        pic = requests.get(pic_urls, timeout=15)
        string = str(1) + '.jpg'
        with open(path+string, 'wb') as f:
            f.write(pic.content)
    except Exception as e:
        print(e)


Crawl_douban_booktop250_data()
Crawl_everytopbook_data()

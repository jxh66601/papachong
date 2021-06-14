import requests
from bs4 import BeautifulSoup
import openpyxl
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
list=[['编号','电影名','电影评论','电影评分','链接地址']]
for i in range(10):

    url ='https://movie.douban.com/top250?start='+str(i*25)+'&filter='

    resp=requests.get(url,headers=headers)
    #print(resp)
    bs=BeautifulSoup(resp.text,'html.parser')
    #print(bs)
    grid_view=bs.find('ol',class_='grid_view')
    all_li=grid_view.find_all('li')
    for item in all_li:
        no=item.find('em').text #电影序号
        title=item.find('span',class_='title').text #电影名
        inq=item.find('span',class_='inq')  #电影评论
        rat=item.find('span',class_='rating_num').text #电影评分
        url_films=item.find('a')['href']
        #print(no,title,inq,rat,url_films)
        list.append([no,title,inq.text if inq!=None else '',rat,url_films])

wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='我的电影'
for item in list:
    sheet.append(item)
wb.save('豆瓣.xlsx')
print('ok')
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit  # BS 内置库，猜测文档编码
import urllib.request
url = 'http://www.weather.com.cn/weather/101300501.shtml'
try:
    headers = {'User-Agent':'Mozilla/5.0(Windows;U;Windows NT 6.0 x64;en-US;rv:1.9pre)Gecko/20191008 Minefield/3.0.2pre'}
    req = urllib.request.Request(url,headers = headers)
    data = urllib.request.urlopen(req)
    data = data.read()
    dammint = UnicodeDammit(data,['utf-8','gbk']) #鉴别编码，做一个包装-markup
    data = dammint.unicode_markup
    soup = BeautifulSoup(data,'lxml')
    lis = soup.select("ul[class='t clearfix'] li") # 找到ul下的所有li
    for li in lis:
        try:
            data = li.select('h1')[0].text  # h1的第一个元素的text文本
            weather = li.select("p[class='wea']")[0].text
            temp = li.findAll('span')[0].text + '/' + li.findAll('i')[0].text
            print(data,weather,temp)
        except Exception as err:
            print(err)
except Exception as err:
    print(err)
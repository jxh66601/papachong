import requests
import  re

url = 'https://www.qiushibaike.com/video/page/3/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
resp = requests.get(url, headers=headers)


vi = re.findall('<source src="(.*)" type=\'video/mp4\' />',resp.text)
list = []
for item in vi:
    list.append('http:'+item)
count = 0
for item in list:

    resp=requests.get(item,headers=headers)
    count+=1
    with open('糗事video/'+str(count)+'.mp4','wb')as f:
        f.write(resp.content)
print("ok")


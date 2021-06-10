import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def get_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
    resp = requests.get(url, headers=headers)
    resp.encodings = 'utf-8'
    return resp.text

def parse_html(html):
    bs = BeautifulSoup(html,"lxml")
    images = bs.select(".ui.image.bqppsearch.lazy")
    for image in images:
        image_url = image['data-original']
        image_name = image_url[image_url.rfind("/")+1:]
        #print(image_url)
        save_image(image_url,image_name)

def save_image(image_url,image_name):
    with open("date/"+image_name,"wb") as f:
        resp = requests.get(image_url)
        f.write(resp.content)


if __name__ == '__main__':

    key_word = input("输入爬取的类型：")
    number = int(input("输入爬取几页："))
    for i in range(number):
        url = "https://fabiaoqing.com/search/bqb/keyword/{0}/type/bq/page/{1}.html".format(quote(key_word),i+1)
        html = get_html(url)
        parse_html(html)
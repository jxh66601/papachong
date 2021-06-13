import json
import time
import requests
import openpyxl
def get_comments(productId,page):
    url='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10030463476229&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    resp=requests.get(url,headers=headers)
    #print(resp.text)
    s=resp.text.replace('fetchJSON_comment98(','')
    s=s.replace(');','')
    json_data=json.loads(s)
    return json_data

def get_max_page(productId):
    dic_date=get_comments(productId,0)
    return dic_date['maxPage']

def get_info(productId):
    max_page=4
    list=[]
    for page in range(1,max_page+1):
        comments=get_comments(productId,page)
        comm_list=comments['comments']
        for item in comm_list:
            content=item['content']
            color=item['productColor']
            size=item['productSize']
            list.append([content,color,size])
        time.sleep(3)
        save(list)

def save(list):
    wk=openpyxl.Workbook()
    sheet=wk.active

    for item in list:
        sheet.append(item)
    wk.save('数据1.xlsx')



if __name__ == '__main__':
    productId='10030463476229'
    #print(get_max_page(productId))
    get_info(productId)
    print('ok')
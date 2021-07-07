import requests
import json
import re
import openpyxl
def send_request():
    url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2021-06-25&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
             'Cookie': '_uab_collina=162365880952000731295007; JSESSIONID=548301EC12F1D31FDAD98EF36FFE32F0; BIGipServerotn=4007067914.50210.0000; RAIL_EXPIRATION=1623992874990; RAIL_DEVICEID=TAvcVl4TUC6WmZ-WlIktH4DHc4AL8OrOSkbec5827ugo4Spx8_NsZNJtuUdC24sDS5hLhHZ4ZVSWNy4Ykd-ngHNIGyWCgwasK1791T6BU9g4fMAFsyMJXB1btvwkncFCumtzf3zGKJc_c4K_jhIBWX8pJjosr97k; BIGipServerpassport=904397066.50215.0000; route=495c805987d0f5c8c84b14f60212447d; _jc_save_toDate=2021-06-14; _jc_save_wfdc_flag=dc; _jc_save_fromDate=2021-06-25; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u4E0A%u6D77%2CSHH; BIGipServerportal=3134456074.17695.0000'}
    resp=requests.get(url,headers=headers)
    resp.encoding = 'utf-8'
    #print(resp.text)
    return resp

def parse_json(resp,city):
    json_ticket=resp.json()
    date_list=json_ticket["data"]["result"]
    list=[]
    for item in date_list:
        d=item.split('|')
        list.append([d[3],city[d[6]],city[d[7]],d[31],d[30],d[13]])
    return list
#3 车次
#6 出发地
#7 目的地
#30 二等座
#31 一等座
#13 出行时间


def save(list):
    wk=openpyxl.Workbook()
    sheet=wk.active
    for item in list:
        sheet.append(item)
    wk.save('车次.xlsx')
        
    

def start():
    lst=parse_json(send_request(),get_city())
    save(lst)

def get_city():
    url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9192'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    resp=requests.get(url,headers=headers)
    resp.encoding = 'utf-8'
    #print(resp.text)
    stations=re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)',resp.text)
    stations_data=dict(stations)
    station_d={}
    for item in stations_data:
        station_d[stations_data[item]]=item
    return station_d


if __name__ == '__main__':
    start()
    print('ok')
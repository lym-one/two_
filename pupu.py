import json
from time import strftime, sleep

import requests


def request_url():
    url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/35db30ff-d3f2-4793-aa08-1c1419fc80a2'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
    }
    res = requests.get(url, headers=head)
    dict1 = json.loads(res.text)
    name = dict1["data"]["name"]  # 商品名字
    spec = dict1["data"]["spec"]  # 规格
    price = str(int(dict1["data"]["price"]) / 100)  # 折扣价
    market_price = str(int(dict1["data"]["market_price"]) / 100)  # 原价
    share_content = dict1["data"]["share_content"]  # 详细内容
    print("-------------商品：" + name + "-------------")
    print("规格：" + spec)
    print("原价：" + price)
    print("原价/折扣价：" + price + "/" + market_price)
    print("详细内容：" + share_content)


def time():  # 获取时间
    url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/35db30ff-d3f2-4793-aa08-1c1419fc80a2'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
    }
    res = requests.get(url, headers=head)
    dict1 = json.loads(res.text)
    name = dict1["data"]["name"]  # 商品名字
    price = str(int(dict1["data"]["price"]) / 100)  # 折扣价
    print("-------------" + name + "-------------")
    try:  #终止程序时，不会报错
        while (True):
            nowTimeAndPrint = strftime('%Y' + '-' + '%m' + '-' + '%d' + ' %H:%M:%S,价格为' + price)
            print(nowTimeAndPrint)
            sleep(5)
    except:
        print("程序结束")


if __name__ == '__main__':
    request_url()
    print("\n")
    time()

# -*- coding: utf-8 -*-

import requests
import csv

"""
爬取网站数据，并获取'data'中array列表中的数据存入csv表中
"""
with open("./spider.csv","w",encoding='utf-8') as f:
    writer = csv.writer(f)
    key_array = ['userId','userNum','name','sex','address','certificate','nationId','nationName','phone','email','schoolName','faculty','grade','class','profession','sysStuDetailId','sourceId','sourceName','feature','type','suspId']
    writer.writerow(key_array)

    # for a in range(21757,21762):
    for a in range(2,53645):
        url = 'http://www.example.com/UserInfo?userId={}'.format(a)
        json_data =requests.get(url).json()['data']
        print(type(json_data))
        if not isinstance(json_data, dict):
            break
        value_array = []
        for k in key_array:
            if k in json_data:
                value_array.append(json_data[k])
            else:
                value_array.append('null')
        # print(value_array)
        writer.writerow(value_array)
        print('第{}条数据写入完成'.format(a-1))

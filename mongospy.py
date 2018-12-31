import pymongo
import requests
import time

"""
爬取json数据，并存储返回json中的'data'到mongodb
添加循环防止访问次数过多网站返回异常功能
添加对data数据类型的检查，防止造成空指针异常
"""
client = pymongo.MongoClient(host='localhost', port=27017)  # 连接mongoDB
db = client.DB_Name                     # 设置插入的数据库名DB_Name
for a in range(1,50000):                # 设置爬取数据的userId区间
    print('userId={}'.format(a))
    url = 'http://www.example.cn/getUserInfo?userId={}'.format(a)

    err_count = 0                               # 错误次数计数
    json_data = None
    while True:                                 # 如果出现错误则进行重试
        try:
            data = requests.get(url)            # 请求资源
            json_data = data.json()             # 获取json数据
            json_data = json_data['data']       # 取data中的子字典
            break
        except:
            err_count += 1
            print('Error!retry({})...'.format(err_count))
            time.sleep(1)                       # 程序暂停1s
            if err_count == 5:                  # 尝试5次后放弃该数据
                break
            pass
    if json_data is None:               # 如果data内容为null，则放弃该记录
        continue
    # print(json_data)
    print(type(json_data))
    db.Collection_Name.insert_one(json_data)        # 设置存入的集合名Collection_Name

client.close()                          # 程序结束，关闭数据库连接

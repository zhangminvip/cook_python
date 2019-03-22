# coding:utf-8

import json
import os
from prettytable import PrettyTable

adr_book = {}

if os.path.exists('adr_book.json'):
    load = input('本地存在历史通讯录，是否导入,输入 y 导入, 任意键 不导入\n')
    if load == 'y':
        f = open("adr_book.json", "r")
        for line in f:
            adr_book = json.loads(line)
        f.close()
        print('加载成功')
    else:
        print('跳过导入')

while True:
    name = input('请输入朋友姓名, 空字符或者#将会结束输入\n').strip()
    if name == '' or name == '#':
        break
    phone = input('请输入电话号码\n')
    email = input('请输入email\n')
    adr_book[name] = [phone, email]

with open('adr_book.json', 'w') as outfile:
    json.dump(adr_book, outfile, ensure_ascii=False)
    outfile.write('\n')



table = PrettyTable(['姓名','电话号码','email'])
for k in adr_book.keys():
    # print(k.ljust(50,' '), adr_book[k][0].ljust(15,' '), adr_book[k][1].ljust(20, ' '))
    table.add_row([k, adr_book[k][0], adr_book[k][1]])
table.align = 'l'
print(table)



while True:
    query_name = input('请输入要查询的姓名\n').strip()
    if query_name == 'n':
        print('退出查询,欢迎再次使用')
        break
    elif query_name == '':
        print('您的输入为空\n')
    elif query_name in adr_book.keys():
        print('查询结果: ',query_name, adr_book[query_name][0], adr_book[query_name][1])
    else:
        print('抱歉，没有查到\n')








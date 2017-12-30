#!/usr/bin/python
#coding:utf-8
# encoding=utf8
import urllib, json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = "http://open.iciba.com/dsapi/" # http://open.iciba.com/dsapi/?date=2018-01-01
response = urllib.urlopen(url)
data = json.loads(response.read())

english = data['content']
chinese = data['note']
date = data['dateline']
pic_small = data['picture']
pic_big = data['picture2']
tags = '每日一句'

filename = date + '.md'

# start md file
file = open(filename, "w")
file.write('---\n')
file.write('title: "' + chinese + '"\n')
file.write('date: ' + date + '\n')
file.write('tags: ["每日一句"]\n')
file.write('cover: "' + pic_small + '"\n')
file.write('---\n')

file.write('## 英文短句：\n' + english + '\n\n')
file.write('<!--more-->\n\n')
file.write('## 中文翻译：\n' + chinese + '\n')
file.close()
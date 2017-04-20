# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
from random import Random
import re
import urllib


# 字符串写出到文件
# 参数字符串  文件路径全名
def dumpfile(str, filefullname):
    f = open(filefullname, 'w')
    f.writelines(str)
    f.close()


# 随机字符串
def randomstr(randomlength=4):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


# 获取网站的域名
def getdomain(url):
    proto, rest = urllib.splittype(url)
    res, rest = urllib.splithost(rest)
    return proto + "://" + res


# 过滤标签
def killtags(shtml):
    soup = BeautifulSoup(shtml, "lxml")
    [script.extract() for script in soup.findAll('script')]
    [style.extract() for style in soup.findAll('style')]
    reg = re.compile("<[^>]*>")
    content = reg.sub(' ', soup.text).decode('utf-8')
    temp = content.replace("\n", " ")
    cont = temp.replace(" ", "")
    return cont
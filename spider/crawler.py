# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from util import utils
from bs4 import BeautifulSoup
import urllib2
import socket
import re


# 获取网页内容
# 将网页内容存在对象中保存
# 提取网页标题
# 网页更新时间记作当前
def fetchlinks(link):
    content = _get(link)
    urls = _fetchurls(content, link)
    return content, urls


# 构造链接
def _fetchurls(shtml, link):
    domain = utils.getdomain(link)
    content = BeautifulSoup(shtml, "lxml").findAll('a')
    pat = re.compile(r'href="([^"]*)"')
    pat2 = re.compile(r'http')
    links = list()
    for item in content:
        try:
            temp = pat.search(str(item))
            href = temp.group(1)
            ans = None
            if pat2.search(href):
                ans = href
            else:
                ans = domain + "/" + href
            links.append(ans)
        except:
            continue
    return links


# 采集开始
def _get(url):
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req, timeout=120)
        return response.read()
    except urllib2.HTTPError, e:
        return e.read()
    except socket.timeout, e:
        return ''
    except socket.error, e:
        return ''
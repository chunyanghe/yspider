# -*- coding: UTF-8 -*-

from spider import build
from spider import crawler
from spider import parser
from config import fulllinks
from config import usedlinks
from util import utils
import config
import traceback
import time
import base64
import datetime
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def _builddict(atc, link):
    usermap = dict()
    usermap["no"] = base64.encodestring(link)
    usermap["title"] = atc.title
    usermap["lastupdate"] = datetime.datetime.now().strftime("%Y-%m-%d")
    usermap["detail"] = atc.cleaned_text[:1000]
    temp = usermap["detail"]
    usermap["resume"] = temp[:min(50, len(temp))]
    usermap["remark"] = ""
    usermap["type"] = 0
    usermap["score"] = 0.0
    usermap["comments"] = 0
    usermap["views"] = 0
    return usermap


def _puturl(urls):
    for link in urls:
        fulllinks.add(link)


def _filepath():
    return config.SAVE_PATH + "/" + str(utils.randomstr(6))


# 流程
def flow():
    fulllinks.add(config.START_LINK)
    seq = 0
    while config.START_SWITCH == "ON":
        seq = seq + 1
        url = fulllinks.pop()
        print "_____________第 %s 次任务开始___________当前链接为%s" % (str(seq), url)
        if url in usedlinks:
            continue
        try:
            data, urls = crawler.fetchlinks(url)
            _puturl(urls)
            art = parser.parsepage(data, url)
            temp = build.buildjson(_builddict(art, url))
            utils.dumpfile(temp, _filepath())
            usedlinks.add(url)
        except Exception, e:
            traceback.print_exc()
        finally:
            print "总链接量", fulllinks
            print "已经抓取链接量", usedlinks
            time.sleep(5)
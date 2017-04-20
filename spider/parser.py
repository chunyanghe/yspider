# -*- coding: UTF-8 -*-

from goose import Goose
from goose.text import StopWordsChinese
import traceback


# 解析页面
def parsepage(data, link):
    try:
        goo = Goose({'stopwords_class': StopWordsChinese})
        article = goo.extract(raw_html=data)
        return article
    except:
        traceback.print_exc()



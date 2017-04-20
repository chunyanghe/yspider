# -*- coding: utf-8 -*-
import sys
from json import JSONEncoder
import json
reload(sys)
sys.setdefaultencoding('utf-8')
a = list()
a.append(1)
a.append("xxx")
s = set()
s.add("cc")
b = dict()
b["w"] = "刘大"


def abc(kwargs):
    print kwargs
    print json.dumps(kwargs,ensure_ascii=False)


abc(b)
# -*- coding: UTF-8 -*-

import json
import dicttoxml



# build a json str
# return json
def buildjson(*args):
    return json.dumps(args, ensure_ascii=False)


# build xml str return xml
def buildxml(rootname=None, *args):
    return dicttoxml.dicttoxml(args, custom_root=rootname)


# build a sql and you can give a tbname
# eg insert into dbname values()
def buildsql(tbname=None, *args):
    vals = ', '.join(['%s'] * len(args))
    columns = ', '.join(args.keys())
    sql = "INSERT INTO %s (%s) VALUES (%s)" % (tbname, columns, vals)
    return sql;


def buildjsonstr(*args):
    pass

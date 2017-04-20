from goose import Goose
from goose.text import StopWordsChinese
import urllib2

send_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'
   # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   # 'Connection': 'keep-alive',
    #'Accept-encoding': 'gzip'
}
# url = "http://news.qq.com"
# req = urllib2.Request(url, headers=send_headers)
# response = urllib2.urlopen(req, timeout=120)
# html = response.read()
# g = Goose({'stopwords_class': StopWordsChinese})
# article = g.extract(raw_html=html)
# print article.links
# print article.cleaned_text[:10000]

url ='http://news.qq.com/a/20170420/000679.htm'
g = Goose({'stopwords_class': StopWordsChinese})
article = g.extract(url=url)
print article.canonical_link
print article.links
print article.cleaned_text[:150]


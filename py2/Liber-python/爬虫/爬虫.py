#!/usr/bin/env python
# -*- coding : utf-8 -*-
# @Date      : 2017-02-17 18:10:34
# @Author  : Liber (haitao.lan@longsys.com)
# @Link       : http://.com

import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
html = getHtml("http://www.baidu.com/")
print html



# if __name__ == '__main__':




#!/usr/bin/env python
# -*- coding : utf-8 -*-
# @Date      : 2017-02-22 13:53:08
# @Author  : Liber (haitao.lan@longsys.com)
# @Link       : http://.com

import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Date:2017-06-01 12:49:04
# @Author:Liber (haitao.lan@longsys.com)
# @Link:http://.com

import select
import socket
import threading

HOST = '127.0.0.1'
PORT = 30321
timeout = 60 * 1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.setblocking(0)
#-*- encoding: gb2312 -*-

def thread_main():
    ready = select.select([s], [], [], timeout)
    if ready[0]:
        data = s.recv(1024)
        if len(data) > 0:
            print data

def main():
    t = threading.Thread(target=thread_main)
    t.start()


if __name__ == '__main__':
    main()


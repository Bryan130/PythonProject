#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Date    : 2017-05-11 10:38:11
# @Author  : Sniper  (haitao.lan@longsys.com)

import unittest,time
from testThread import *


class Devicestatus(unittest.TestCase):
    def setUp(self):
        devcmd= hex_data(1,"string","123")
        print "devcmd: ", devcmd
        data = "AT+TESTMODE\r\n"
        data, ADDR = send_udp(HOST,data)
        print data
        self.access_Token = login_email("test_3.6@qq.com", "test123")
        # print access_Token


    def tearDown(self):
        pass

    # 类里每一个test开头的方法对应一个测试用例
    def test_devcmd(self):

        t = threading.Thread(target=thread_main)
        t.start()
        res = updateDeviceStatus(self.access_Token, "kykbFpFgbmrV", 123)
        print "res",res

    def thread_main():
        PORT = 30321
        timeout = 60 * 1
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((HOST, PORT))
        s.setblocking(0)
        ready = select.select([s], [], [], timeout)
        if ready[0]:
            data = s.recv(1024)
            print data


if __name__ == '__main__':
    a= 29.7+ 55.7+40.4+29.7+40+50
    print a

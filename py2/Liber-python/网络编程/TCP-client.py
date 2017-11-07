#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Date:2017-05-18 11:51:20
# @Author:Liber (haitao.lan@longsys.com)
# @Link:http://.com

import socket
def check_tcp_status(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    print 'Connecting to %s:%s.' % server_address
    sock.connect(server_address)
    # message = "I'm TCP client"
    print 'Sending "%s".' % message
    sock.sendall(message)
    print 'Closing socket.'
    sock.close()
if __name__ == "__main__":
    print check_tcp_status("127.0.0.1", 12345,'hahaha')


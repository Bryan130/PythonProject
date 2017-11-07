#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Date:2017-06-13 18:09:19
# @Author:Liber (haitao.lan@longsys.com)
# @Link:http://.com

import socket

def send_udp(host, port, data):
    BUFSIZE = 1024              #缓冲区大小1K
    ADDR = (host,port)
    print "create UDPclisock"
    udpCliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpCliSock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

    while True:                 #无限循环等待连接到来
        try:
            print 'Connecting to %s:%s.' % ADDR
            print 'Sending "%s".' % data
            udpCliSock.sendto(data, ADDR)            #发送数据
            #time.sleep(1)
            data,ADDR = udpCliSock.recvfrom(BUFSIZE)  #接受数据
            #关闭客户端
            print 'Closing socket.'
            udpCliSock.close()
            return data, ADDR
        except Exception,e:
            return 'Error: ',e

if __name__ == '__main__':
    host = "255.255.255.255"
    port = 30319
    data = "AT+FIND\r\n"
    data1,ADDR1 = send_udp(host, port, data)
    print "data1",data1
    print "ADDR1",ADDR1

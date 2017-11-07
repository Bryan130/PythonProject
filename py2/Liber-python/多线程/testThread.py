#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Date    : 2017-05-11 10:38:11
# @Author  : Sniper  (haitao.lan@longsys.com)

import urllib
import urllib2
import json
import unittest
import select
import struct
import sys
import threading
from socket import *

def login_email(email, password):
    url = 'http://192.168.3.6:80/v1/account/login'
    rebody = {'email':email, 'password':password }
    headers = { 'Content-Type':"application/json" }
    jdata = json.dumps(rebody)
    req = urllib2.Request(url, jdata, headers)
    response = urllib2.urlopen(req)
    res = response.read()
    res = json.loads(res)
    access_Token=res["accessToken"]
    return access_Token

def updateDeviceStatus(access_Token,did,intvalue):
    url = 'http://192.168.3.6:80/v1/device/'+did+'/status'
    rebody = {'integer':intvalue }
    headers = { 'Content-Type':"application/json", "authorization":access_Token }
    jdata = json.dumps(rebody)
    req = urllib2.Request(url, jdata, headers)
    req.get_method = lambda:"PUT"
    response = urllib2.urlopen(req)
    res = response.code
    return res

def send_udp(HOST,data):
    PORT =  30319               #端口号 与服务器一致
    BUFSIZE = 1024              #缓冲区大小1K
    ADDR = (HOST,PORT)
    udpCliSock = socket(AF_INET, SOCK_DGRAM)
    udpCliSock.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

    while True:                 #无限循环等待连接到来
        try:
            if not data:
                break
            print 'Connecting to %s:%s.' % ADDR
            print 'Sending "%s".' % data
            udpCliSock.sendto(data, ADDR)            #发送数据
            data,ADDR = udpCliSock.recvfrom(BUFSIZE)  #接受数据
            if not data:
                break
            return data, ADDR
        except Exception,e:
            return 'Error: ',e
    print 'Closing socket.'
    udpCliSock.close()          #关闭客户端


TYPE_BOOL = 0x01
TYPE_INT  = 0x02
TYPE_FLOAT = 0x03
TYPE_STR = 0x04

def tlv(index,dptype,value):
    if dptype == 'string':
        pkt_bytes = put_string(index, value)
        return pkt_bytes
    elif dptype == 'integer' or dptype == 'int':
        pkt_bytes = put_integer(index, value)
        return pkt_bytes
    elif dptype == 'boolean' or dptype == 'bool':
        pkt_bytes = put_boolean(index, value)
        return pkt_bytes
    elif dptype == 'float':
        pkt_bytes = put_float(index, value)
        return pkt_bytes
    else:
        print TypeError


def put_boolean(index, value):
    if value == 'False' or value == 'false':
        value = False
    else:
        value = True
    pkt_bytes = []
    #byte0 & byte1: tag
    pkt_bytes += [ord(b) for b in struct.pack("<H", index)]
    #byte3 & byte4: type & 0x0
    pkt_bytes += [TYPE_BOOL, 0x00]
    #len
    pkt_bytes += [0x01, 0x00]
    #value
    pkt_bytes += [int(value)]
    return pkt_bytes


def put_integer(index, value):
    value=int(value)
    pkt_bytes = []
    #byte0 & byte1: tag
    pkt_bytes += [ord(b) for b in struct.pack("<H", index)]
    #byte3 & byte4: type & 0x0
    pkt_bytes += [TYPE_INT, 0x00]
    _v = struct.pack("<i", value)
    #len
    pkt_bytes += [len(_v), 0x00]
    #value
    pkt_bytes += [ord(b) for b in _v]
    return pkt_bytes


def put_float(index, value):
    value=float(value)
    pkt_bytes = []
    #byte0 & byte1: tag
    pkt_bytes += [ord(b) for b in struct.pack("<H", index)]
    #byte3 & byte4: type & 0x0
    pkt_bytes += [0x03, 0x00]
    _v = struct.pack("<f", value)
    #len
    pkt_bytes += [len(_v), 0x00]
    #value
    pkt_bytes += [ord(b) for b in _v]
    return pkt_bytes


def put_string(index, value):
    value=str(value)
    pkt_bytes = []
    #byte0 & byte1: tag
    pkt_bytes += [ord(b) for b in struct.pack("<H", index)]
    #byte3 & byte4: type & 0x0
    pkt_bytes += [0x04, 0x00]
    #len
    pkt_bytes += [ord(b) for b in struct.pack("<H", len(value))]
    #value
    pkt_bytes += value
    return pkt_bytes

def hex_data(index,dptype,value):
    index = int(index)
    from time import sleep
    pkt_bytes = tlv(index, dptype, value)
    # print pkt_bytes
    pkt_str = ""
    for x in pkt_bytes:
        if type(x) == int:
            pkt_str += myhex(x)
        elif type(x) == str:
            pkt_str += x.encode('hex')
            # print "x.encode",x.encode('hex')
        else:
            break
    pkt_str = pkt_str.replace("0x", "0")
    return pkt_str

def create_data(index,dptype,value):
    pkt_str = hex_data(index, dptype, value)
    data = 'AT+RAW=' + pkt_str + '\r\n'
    return data

def myhex(num):
    return '%02x' % num

HOST = "192.168.3.2"


# def thread_main():
#     global rdata
#     PORT = 30321
#     timeout = 60 * 1
#     s = socket(AF_INET, SOCK_STREAM)
#     s.connect((HOST, PORT))
#     s.setblocking(0)
#     ready = select.select([s], [], [], timeout)
#     if ready[0]:
#         data = s.recv(1024)
#         data = data +1
#         print data
#         self.assertEqual(devcmd, data, "Faild")


        # devcmd= hex_data(1,"string","123")
        # print devcmd
        # if (data == devcmd):
        #     print "assert equal."
        # else:
        #     print "Failed"

# def main():
#     t = threading.Thread(target=thread_main)
#     t.start()


# if __name__ == '__main__':
#     data = "AT+TESTMODE\r\n"
#     data, ADDR = send_udp(HOST,data)
#     print data
#     main()
#     access_Token = login_email("test_3.6@qq.com", "test123")
#     res = updateDeviceStatus(access_Token, "kykbFpFgbmrV", 123)
#     print "res",res


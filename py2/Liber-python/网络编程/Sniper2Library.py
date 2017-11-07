#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Date    : 2017-05-11 10:38:11
# @Author  : Liber (haitao.lan@longsys.com)
# @Link    : http://.com


import socket
import struct
import sys


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

def create_data(index,dptype,value):
    index = int(index)
    from time import sleep
    pkt_bytes = tlv(index, dptype, value)
    print pkt_bytes

    pkt_str = ""
    for x in pkt_bytes:
        # print myhex(x)
        # pkt_str += myhex(x)
        print x
        print type(x)
        if type(x) == int:
            pkt_str += myhex(x)
        elif type(x) == str:
            pkt_str += x.encode('hex')
            print "x.encode",x.encode('hex')
        else:
            break

    print "spkt_bytes",pkt_str
    pkt_str = pkt_str.replace("0x", "0")
    print "pkt_str",pkt_str

    data = 'AT+RAW=' + pkt_str + '\r\n'
    return data

def myhex(num):
    return '%02x' % num



def sendUDP(HOST,data):
    from socket import *

    PORT =  30319               #端口号 与服务器一致
    BUFSIZE = 1024              #缓冲区大小1K
    ADDR = (HOST,PORT)

    udpCliSock = socket(AF_INET, SOCK_DGRAM)
    udpCliSock.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

    while True:                 #无限循环等待连接到来
        try:
            if not data:
                break
            udpCliSock.sendto(data, ADDR)            #发送数据
            data,ADDR = udpCliSock.recvfrom(BUFSIZE)  #接受数据
            if not data:
                break
            return 'Server : ', data
        except Exception,e:
            return 'Error: ',e
    udpCliSock.close()          #关闭客户端


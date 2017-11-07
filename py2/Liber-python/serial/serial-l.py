#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-10
# @Author  : ${author} (${email})
# @Link    : ${link}
# @Version : $Id$
import struct
import serial


TYPE_BOOL = 0x01
TYPE_INT  = 0x02
TYPE_FLOAT = 0x03
TYPE_STR = 0x04

def tlv(index,type,value):
    if type == 'string':
        pkt_bytes = put_string(index, value)
        return pkt_bytes
    elif type == 'integer':
        pkt_bytes = put_integer(index, value)
        return pkt_bytes
    elif type == 'boolean':
        pkt_bytes = put_boolean(index, value)
        return pkt_bytes
    elif type == 'float':
        pkt_bytes = put_float(index, value)
        return pkt_bytes
    else:
        print TypeError


def put_boolean(index, value):
    pkt_bytes = []
    #byte0 & byte1: tag
    pkt_bytes += [ord(b) for b in struct.pack("<H", index)]
    #byte3 & byte4: type & 0x0
    pkt_bytes += [TYPE_BOOL, 0x00]
    print pkt_bytes
    #len
    pkt_bytes += [0x01, 0x00]
    print pkt_bytes
    #value
    print value
    pkt_bytes += [int(value)]
    print pkt_bytes
    return pkt_bytes


def put_integer(index, value):
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


def openSer1(COM,index,type,value):
    from time import sleep
    ser = serial.Serial(COM,115200)
    pkt_bytes = tlv(index, type, value)
    bdata = []
    bde = []
    data = 'AT+RAW='
    bdata += bytes(data)
    de = '\r\n'
    bde += bytes(de)
    pkt_bytes = bdata+ pkt_bytes+bde
    ser.write(pkt_bytes)
    sleep(1)
    ser.flush()
    print 11
    ser.close()


if __name__ == '__main__':
    openSer1('COM3',1,'integer',1213)


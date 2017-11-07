#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-10
# @Author  : ${author} (${email})
# @Link    : ${link}
# @Version : $Id$

import serial

# def openSer1():
ser = serial.Serial('COM1',9600)
print ser.portstr
ser.write('0xff 0xee 0xaa 0xbb')

print '111'

ser.close()

# if __name__ == '__main__':
#     openSer1()

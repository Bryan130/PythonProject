#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author:Bryan.Lan (bryan.lan@vengasz.com)
# @Link:https://github.com/Bryan130

promt = "\nTell me something"
promt += "\nEnter 'quit' to end the program."
message = ''
active = True
while active:
    message = input(promt)

    if message == 'quit':
        active = False
    else:
        print(message)

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Date:2017-06-21 19:52:12
# @Author:Bryan (bryan.lan@vengasz.com)
# @Link:https://github.com/Bryan130

import sys


def print_lol(the_list, indent=False, level=0, file=sys.stdout):
    """这是“nester.py”模块，提供了一个名为
    print_lol()的函数，这个函数的作用是打印列表，
    其中有可能包含（也可能不包含）嵌套列表。
    第二个参数（名为level）用例再遇到嵌套列表是插入制表符"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level + 1, file)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=file)
            print(each_item)

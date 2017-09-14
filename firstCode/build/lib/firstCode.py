#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Date:2017-06-21 19:52:12
# @Author:Bryan (bryan.lan@vengasz.com)
# @Link:https://github.com/Bryan130


def print_lol(the_list, level):
    """这是“firstCode.py”模块，提供了一个名为
    print_lol()的函数，这个函数的作用是打印列表，
    其中有可能包含（也可能不包含）嵌套列表。
    第二个参数（名为level）用例再遇到嵌套列表是插入制表符"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level+1)
        else:
            for tab_stop in range(level):
                print("\t", end='')
            print(each_item)

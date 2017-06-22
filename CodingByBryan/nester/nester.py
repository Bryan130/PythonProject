#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Date:2017-06-21 19:52:12
# @Author:Bryan (bryan.lan@vengasz.com)
# @Link:http://.com

def print_lol(the_list):
    """这是“nester.py”模块，提供了一个名为print_lol()的函数，这个函数的作用是打印列表，其中有可能包含（也可能不包含）嵌套列表。"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print each_item


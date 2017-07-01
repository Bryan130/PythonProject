#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Date:2017-06-21 19:52:12
# @Author:Bryan.Lan (bryan.lan@vengasz.com)
# @Link:https://github.com/Bryan130

import sys
import pickle


def print_lol(the_list, indent=False, level=0, fh=sys.stdout):
    """这是“nester.py”模块，提供了一个名为
    print_lol()的函数，这个函数的作用是打印列表，
    其中有可能包含（也可能不包含）嵌套列表。
    第二个参数（名为level）用例再遇到嵌套列表是插入制表符"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level + 1, fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=fh)
            print(each_item, file=fh)


file_name = "data.txt"
bryan = []
sniper = []
try:
    print("open data.txt")
    with open(file_name) as data:
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(":", 1)
                line_spoken = line_spoken.strip()
                if role == 'bryan':
                    bryan.append(line_spoken)
                elif role == 'sniper':
                    sniper.append(line_spoken)
            except ValueError:
                pass
except FileNotFoundError:
    print("The datafile is missing!")

try:
    print("open txt")
    with open("bryan.txt", "wb") as bryanData:
        pickle.dump(bryan, bryanData)
except IOError as err:
    print("File error: " + err)
except pickle.PickleError as perr:
    print("Pickling error: " + str(perr))

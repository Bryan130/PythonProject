#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Date:2017-06-21 19:52:12
# @Author:Bryan.Lan (bryan.lan@vengasz.com)
# @Link:https://github.com/Bryan130

import os
file_name = "data.txt"
print(os.getcwd())
os.chdir("E:/Python36/PythonProject/CodingByBryan/test")
print(os.getcwd())
with open(file_name) as file_object:
    for each_line in file_object:
        try:
            (role, line_spoken) = each_line.split(":", 1)
            print(role, end='')
            print(" said: ", end='')
            print(line_spoken, end='')
        except:
            print(each_line, end='')

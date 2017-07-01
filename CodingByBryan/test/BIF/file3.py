#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Date:2017-06-21 19:52:12
# @Author:Bryan.Lan (bryan.lan@vengasz.com)
# @Link:https://github.com/Bryan130

file_name = "data.txt"
bryan = []
sniper = []
try:
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
print(bryan)
print(sniper)

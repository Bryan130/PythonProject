# -*- coding:utf-8 -*-
'''
Created on 2016年11月24日

@author: User
'''

while True:
    print "请输入所要查询的年月日："
    year = input("请输入年份（xxxx）：")
    month = input("请输入月份（xx）：")
    day = input("请输入日（xx）：")
    #判断平润年
    if year % 4 == 0 and year % 100 != 0 or year % 400 ==0: #闰年
        if month == 01:
            if day <= 31:          
                print "今天是%d年的第%d天！" % (year, day)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 02:
            if day <= 29:          
                sum = 31 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 03:
            if day <= 31:          
                sum = 31 + 29 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 04:
            if day <= 30:          
                sum = 31 + 29 + 31 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 05:
            if day <= 31:          
                sum = 31 + 29 + 31 + 30 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 06:
            if day <= 30:          
                sum = 31 + 29 + 31 + 30 + 31 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 07:
            if day <= 31:          
                sum = 31 + 29 + 31 + 30 + 31 + 30 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 08:
            if day <= 31:          
                sum = 31 + 29 + 31 + 30 + 31 + 30 + 31 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 09:
            if day <= 30:          
                sum = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 10:
            if day <= 31:          
                sum = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 11:
            if day <= 30:          
                sum = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 12:
            if day <= 31:          
                sum = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        else:
            print "你输入的月份不正确，每个年只有12个月！"
    else:
        if month == 01:
            if day <= 31:          
                print "今天是%d年的第%d天！" % (year, day)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 02:
            if day <= 28:          
                sum = 31 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 03:
            if day <= 31:          
                sum = 31 + 28 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 04:
            if day <= 30:          
                sum = 31 + 28 + 31 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 05:
            if day <= 31:          
                sum = 31 + 28 + 31 + 30 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 06:
            if day <= 30:          
                sum = 31 + 28 + 31 + 30 + 31 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 07:
            if day <= 31:          
                sum = 31 + 28 + 31 + 30 + 31 + 30 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 08:
            if day <= 31:          
                sum = 31 + 28 + 31 + 30 + 31 + 30 + 31 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 09:
            if day <= 30:          
                sum = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 10:
            if day <= 31:          
                sum = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 11:
            if day <= 30:          
                sum = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        elif month == 12:
            if day <= 31:          
                sum = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + day
                print "今天是%d年的第%d天！" % (year, sum)
            else:
                print "您输入的day不正确，%d年%d月只有31天哦！" % (year, month)
        else:
            print "你输入的月份不正确，每个年只有12个月！"
                    
                
                
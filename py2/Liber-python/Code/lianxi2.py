# -*- coding:utf-8 -*-
'''
Created on 2016年11月30日

@author: v_tjietang
'''
from nt import remove
passfile = 'user.txt'
def regist(file):               #注册
    name = raw_input("请输入帐号:")
    password = raw_input("请输入密码:")
    user_info = name + ' ' + password + '\n'
    print isexist(name)
    if isexist(name) == True:
        file.write(user_info)
        print "注册成功"
        file.close()
    else:
        print '帐号已存在' 
    
    return
def isexist(name):
    file = open(passfile,'r')              #判断帐号是否存在
    file_list = file.readlines()
    for l in file_list:
        s = l.strip().split(' ')
        if s[0] == name:
            
            return False
    else:    
        return True
    file.close()
def user_login(file):  #登录  
                    
    return
def admin_login():
    return

def main():
    while True:
        print "1.注册"
        print "2.登录"
        print "3.离开"
        luru=raw_input("请选择要进行的操作:")
        if luru == '1':
           
            file = open('user.txt','a')
            regist(file)
#             file1 = open('user.txt','r')
#             file_list = file1.readlines()
#             for l in file_list:
#                 print l.strip().split(' ')
            
        elif luru == '2':
            name = raw_input("请输入帐号:")
            password = raw_input("请输入密码:")
            file = open(passfile,'r')
            file_list=file.readlines()
            file.close()
            for list in file_list:
                l = list.strip().split()
#                 print l          
                if name == 'admin' and password == l[1] and name == l[0]:
                    print "1.添加用户"
                    print "2.删除用户"
                    print "3.修改用户"
                    admin_type=raw_input("管理员请选择操作方式:")
                    if admin_type == '1':
                        file = open(passfile,'a')
                        regist(file)
                        file.close()
                    elif admin_type == '2':
                        rm_name = raw_input("请输入要删除的用户名:")
                        file1 = open(passfile,'r')
                        file_list1 = file1.readlines()
                        file1.close()
                        for l1 in file_list1:
                            l2 = l1.strip().split()
                            if l2[0] == rm_name:
                                l2.remove(l2[0])
                                l2.remove(l2[0])
                                continue
#                                 print l2
#                             if l2[0] == None:
#                                 continue
                            
                            userinfo = l2[0] + ' ' + l2[1] + '\n'
                            print userinfo
                            f1 = open(passfile,'a')
                            f1.write(userinfo)
                            f1.close()
                            print l2
                    elif admin_type == '3':
                        updat_name = raw_input("请输入需要修改的账户名称:")
                        updat_pwd = raw_input("请输入修改后的密码:")
                        file = open(passfile,'a+')
                        fi_lt = file.readlines()
                        for flt in fi_lt:
                            f = flt.strip().split()
#                         print f
                            if f[0] == updat_name:
                                f[1] = updat_pwd
#                             print f
                                break
                        else:
                            print "用户名不存在" 
                            break   
                        
                           
                    else:
                        print '请输入正确的操作方式'
                        break
                elif name == l[0] and password == l[1]:
                    print '登录成功!'
                    break
            else:
                print '帐号或密码错误'
        elif luru == '3':
            break
        else:
            print "输入的操作不正确"
            break
if __name__ == '__main__':
     main()   
    
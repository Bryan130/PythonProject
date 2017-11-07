#coding=gbk
import os
FileName='user.txt'
UserName='zz'
def isexist(FileName,UserName):
    f=open(FileName,'r')
    for i in [i.split(':')[0] for i in f if i.strip()!='']:
        if i==UserName:
            return False
    else:
        return True


def Add():
    while True:
        username=raw_input('请输入用户名：').strip()
        if isexist(FileName,username):
            pw=raw_input('请输入密码：')
            f=open(FileName,'a')
            f.write('%s:%s\n'%(username,pw))
            f.close()
            print '成功添加用户：%s'%username
            break
        else:
            print '用户名已存在'
            continue
    return
def login():
    f=open(FileName,'r')
    UserName=raw_input('请输入用户名：').strip()
    for i in [i.strip().split(':') for i in f if i.strip()!='']:
        if i[0]==UserName:
            pw=raw_input('请输入用户密码：')
            if pw==i[1]:
                print'登录成功，欢迎%s'%UserName
                break
            else:
                print '密码错误'
                break
    else:
        print '用户名不存在'
    f.close()
    
def menu():
    '''菜单程序'''
    while True:
        while True:
            menu='''

菜单：
a:注册
l:登录
请输入字母选择功能：'''
            try:
                choice=raw_input(menu).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,TypeError,ValueError),e:
                choice='q'
            if choice not in 'alq':
                print '菜单选项输入有误，请重新输入"alq"进行菜单选择'
                continue
            break
        if choice=='q':break
        if choice=='a':Add()
        if choice=='l':login()
        if choice=='u':Upd()
        if choice=='s':delt()

if __name__=="__main__":
    f=open(FileName,'a')
    f.close()
    menu()


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
        username=raw_input('�������û�����').strip()
        if isexist(FileName,username):
            pw=raw_input('���������룺')
            f=open(FileName,'a')
            f.write('%s:%s\n'%(username,pw))
            f.close()
            print '�ɹ�����û���%s'%username
            break
        else:
            print '�û����Ѵ���'
            continue
    return
def login():
    f=open(FileName,'r')
    UserName=raw_input('�������û�����').strip()
    for i in [i.strip().split(':') for i in f if i.strip()!='']:
        if i[0]==UserName:
            pw=raw_input('�������û����룺')
            if pw==i[1]:
                print'��¼�ɹ�����ӭ%s'%UserName
                break
            else:
                print '�������'
                break
    else:
        print '�û���������'
    f.close()
    
def menu():
    '''�˵�����'''
    while True:
        while True:
            menu='''

�˵���
a:ע��
l:��¼
��������ĸѡ���ܣ�'''
            try:
                choice=raw_input(menu).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,TypeError,ValueError),e:
                choice='q'
            if choice not in 'alq':
                print '�˵�ѡ��������������������"alq"���в˵�ѡ��'
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


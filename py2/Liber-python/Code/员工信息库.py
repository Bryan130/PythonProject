#coding=gbk
import os
from sys import stderr


'''
*************Ա����Ϣ��ϵͳ********************
�˵���
a:����Ա��
d:ɾ��Ա��
u:������Ϣ
s:��ѯ��Ϣ
'''

def Add():
    os.chdir(code_path+os.sep+'Ա����Ϣ��')  #�л���'Ա����Ϣ��'Ŀ¼��
    user_list=os.listdir('.')   #��ȡ'Ա����Ϣ��'�������ļ���
    while True:
        try:
            ID=raw_input('�������û���ţ�').strip()
        except (EOFError,KeyboardInterrupt,NameError,TypeError),e:
            print >>stderr,'%s:�����ԣ�'%e.__class__.__name__
            continue
        else:
            if ID in [i.split('_')[0] for i in user_list]:  #��ȡ�ļ����еı�ţ����ж�������û�����ǲ����Ѿ�����
                print >>stderr,'Ա���Ѵ��ڣ��뻻һ���������'
                continue
            break
    while True:
        try:
            name=raw_input('����������:')
        except(EOFError,KeyboardInterrupt,NameError,TypeError),e:
            print e
            continue
        if '_' in name:
            print '�����в��ܰ���"_"'
            continue
        break
    while True:
        try:
            phone=raw_input('������绰���룺')
        except(EOFError,KeyboardInterrupt,NameError,TypeError),e:
            print e
            continue
        break
    while True:
        try:
            adderss=raw_input('���������ļ��᣺')
        except(EOFError,KeyboardInterrupt,NameError,TypeError),e:
            print e
            continue
        break
    file_name='%s_%s.txt'%(ID,name)
    f=open(file_name,'w')
    f.write('���:%s%s'%(ID,os.linesep))
    f.write('����:%s%s'%(name,os.linesep))
    f.write('�绰:%s%s'%(phone,os.linesep))
    f.write('��ַ:%s%s'%(adderss,os.linesep))
    f.close()
    print  '****************�ɹ�����û���%s*************'%name
def Del():
    flag=0
    os.chdir(code_path+os.sep+'Ա����Ϣ��')  #�л���'Ա����Ϣ��'Ŀ¼��
    user_list=os.listdir('.')   #��ȡ'Ա����Ϣ��'�������ļ���
    while True:    
        try:
            user_id=raw_input('������Ҫɾ����Ա����ţ�')
        except BaseException,e:
            print e
            continue
        else:
            for i in user_list:
                if user_id==i.split('_')[0]:
                    os.remove(i)
                    print '�ɹ�ɾ��Ա��:%s'%i.split('_')[0]
                    flag=1
                    break
            break
    if flag==0:
        print >>stderr,'Ա����Ų�����'
     
def Upd():
    flag=0
    os.chdir(code_path+os.sep+'Ա����Ϣ��')  #�л���'Ա����Ϣ��'Ŀ¼��
    user_list=os.listdir('.')   #��ȡ'Ա����Ϣ��'�������ļ���
    while True:
        try:
            user_id=raw_input('������Ҫ�޸ĵ�Ա����ţ�')
        except BaseException,e:
            print e
            continue
        else:
            for i in user_list:
                if user_id==i.split('_')[0]:
                    try:
                        f1=open(i,'r')
                        filename=i
                        user_list=f1.readlines()
                    except(IOError,WindowsError),e:
                        print e
                        break
                    else:
                        f1.close()
                        flag=1
                    break
        break
    if flag==1:
        menu='''

���
����
�绰
��ַ
��������������ĵ��ֶΣ�'''
        while True:
            try:
                update=raw_input(menu).strip()
            except(EOFError,KeyboardInterrupt,ValueError,TypeError),e:
                print e
                continue
            break
        list1=[i.strip().split(":") for i in user_list if i.strip()!='']
        for i in list1:
            if i[0]==update:
                flag=0
                update_value=raw_input('�������޸ĺ��ֵ��')
                i[1]=update_value
                break
        if flag==1:
            print >>stderr,'�ֶ��������'
        else:
            f2=open(filename,'w')
            for i,j in list1:
                f2.write('%s:%s'%(i,j+os.linesep))
            f2.close()
            print '�޸ĳɹ���'
    else:
        print >>stderr,'Ա���Ų�����'

def Sel():
    flag=0
    os.chdir(code_path+os.sep+'Ա����Ϣ��')  #�л���'Ա����Ϣ��'Ŀ¼��
    user_list=os.listdir('.')   #��ȡ'Ա����Ϣ��'�������ļ���
    while True:
        try:
            user_id=raw_input('������Ҫ��ѯ��Ա����ţ�')
        except BaseException,e:
            print e
            continue
        else:
            break
    for i in user_list:
        if user_id==i.split('_')[0]:
            flag=1
            filename=i
            break
    if flag==1:
        for i in [i.strip() for i in open(filename,'r')]:
            print i 
    else:
        print >>stderr,'Ա���Ų�����'


def menu():
    '''�˵�����'''
    while True:
        while True:
            menu='''

�˵���
a:����Ա��
d:ɾ��Ա��
u:������Ϣ
s:��ѯ��Ϣ
q:�˳��˵�
��������ĸѡ���ܣ�'''
            try:
                choice=raw_input(menu).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,TypeError,ValueError),e:
                choice='q'
            if choice not in 'adusq':
                print >>stderr,'�˵�ѡ��������������������"adus"���в˵�ѡ��'
                continue
            break
        if choice=='q':break
        if choice=='a':Add()
        if choice=='d':Del()
        if choice=='u':Upd()
        if choice=='s':Sel()
if __name__=='__main__':
    flag=1
    if not os.path.exists('Ա����Ϣ��'):  #�жϽű�����Ŀ¼���Ƿ���'Ա����Ϣ��'����ļ���
        try:
            os.mkdir('Ա����Ϣ��') #������ʱ�������ļ���
        except Exception,e:
            print e
            flag=0
    if flag==1:  #�ļ��д���ʱִ�в˵�����
        code_path=os.getcwd()  #��ȡ�ű����ڵľ���·��
        menu()  #���ò˵�����

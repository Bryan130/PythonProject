#coding=gbk
import os
from sys import stderr


'''
*************员工信息子系统********************
菜单：
a:新增员工
d:删除员工
u:更改信息
s:查询信息
'''

def Add():
    os.chdir(code_path+os.sep+'员工信息库')  #切换到'员工信息库'目录下
    user_list=os.listdir('.')   #获取'员工信息库'下所以文件名
    while True:
        try:
            ID=raw_input('请输入用户编号：').strip()
        except (EOFError,KeyboardInterrupt,NameError,TypeError),e:
            print >>stderr,'%s:请重试！'%e.__class__.__name__
            continue
        else:
            if ID in [i.split('_')[0] for i in user_list]:  #获取文件名中的编号，并判断输入的用户编号是不是已经存在
                print >>stderr,'员工已存在，请换一个编号重试'
                continue
            break
    while True:
        try:
            name=raw_input('请输入姓名:')
        except(EOFError,KeyboardInterrupt,NameError,TypeError),e:
            print e
            continue
        if '_' in name:
            print '名字中不能包含"_"'
            continue
        break
    while True:
        try:
            phone=raw_input('请输入电话号码：')
        except(EOFError,KeyboardInterrupt,NameError,TypeError),e:
            print e
            continue
        break
    while True:
        try:
            adderss=raw_input('请输入您的籍贯：')
        except(EOFError,KeyboardInterrupt,NameError,TypeError),e:
            print e
            continue
        break
    file_name='%s_%s.txt'%(ID,name)
    f=open(file_name,'w')
    f.write('编号:%s%s'%(ID,os.linesep))
    f.write('姓名:%s%s'%(name,os.linesep))
    f.write('电话:%s%s'%(phone,os.linesep))
    f.write('地址:%s%s'%(adderss,os.linesep))
    f.close()
    print  '****************成功添加用户：%s*************'%name
def Del():
    flag=0
    os.chdir(code_path+os.sep+'员工信息库')  #切换到'员工信息库'目录下
    user_list=os.listdir('.')   #获取'员工信息库'下所以文件名
    while True:    
        try:
            user_id=raw_input('请输入要删除的员工编号：')
        except BaseException,e:
            print e
            continue
        else:
            for i in user_list:
                if user_id==i.split('_')[0]:
                    os.remove(i)
                    print '成功删除员工:%s'%i.split('_')[0]
                    flag=1
                    break
            break
    if flag==0:
        print >>stderr,'员工编号不存在'
     
def Upd():
    flag=0
    os.chdir(code_path+os.sep+'员工信息库')  #切换到'员工信息库'目录下
    user_list=os.listdir('.')   #获取'员工信息库'下所以文件名
    while True:
        try:
            user_id=raw_input('请输入要修改的员工编号：')
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

编号
姓名
电话
地址
请输入上述需更改的字段：'''
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
                update_value=raw_input('请输入修改后的值：')
                i[1]=update_value
                break
        if flag==1:
            print >>stderr,'字段输入错误'
        else:
            f2=open(filename,'w')
            for i,j in list1:
                f2.write('%s:%s'%(i,j+os.linesep))
            f2.close()
            print '修改成功！'
    else:
        print >>stderr,'员工号不存在'

def Sel():
    flag=0
    os.chdir(code_path+os.sep+'员工信息库')  #切换到'员工信息库'目录下
    user_list=os.listdir('.')   #获取'员工信息库'下所以文件名
    while True:
        try:
            user_id=raw_input('请输入要查询的员工编号：')
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
        print >>stderr,'员工号不存在'


def menu():
    '''菜单程序'''
    while True:
        while True:
            menu='''

菜单：
a:新增员工
d:删除员工
u:更改信息
s:查询信息
q:退出菜单
请输入字母选择功能：'''
            try:
                choice=raw_input(menu).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,TypeError,ValueError),e:
                choice='q'
            if choice not in 'adusq':
                print >>stderr,'菜单选项输入有误，请重新输入"adus"进行菜单选择'
                continue
            break
        if choice=='q':break
        if choice=='a':Add()
        if choice=='d':Del()
        if choice=='u':Upd()
        if choice=='s':Sel()
if __name__=='__main__':
    flag=1
    if not os.path.exists('员工信息库'):  #判断脚本所在目录下是否有'员工信息库'这个文件夹
        try:
            os.mkdir('员工信息库') #不存在时创建该文件夹
        except Exception,e:
            print e
            flag=0
    if flag==1:  #文件夹存在时执行菜单程序
        code_path=os.getcwd()  #获取脚本所在的绝对路径
        menu()  #调用菜单程序

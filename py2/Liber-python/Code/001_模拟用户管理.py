#coding=utf-8

"""    使用user.txt文件保存用户信息，缺省超级管理员用户root,密码：'123456'   """
import sys,os
filename='user.txt'

def New_user():
    '''注册新用户'''
    with open(filename,'r') as f:
        userlist=f.readlines()
    username=raw_input('请输入用户名：').strip()
    for i in userlist:
        if i.strip().split(':')[0]==username:
            print '用户名已存在！'
            break
    else:
        password=raw_input('请输入用户密码：').strip()
        f=open(filename,'a')
        f.write('%s:%s%s'%(username,password,os.linesep))
        f.close()
        print '成功添加用户：%s'%username
    
def Old_user():
    '''用户登录'''
    choices='''
a:add user 
d:del user
u:update passwd
pick your chioce in 'adu':'''
    with open(filename,'r') as f:
        userlist=f.readlines()
    username=raw_input('请输入用户名：').strip()
    password=raw_input('请输入用户密码:').strip()
    for i in userlist:
        if username=='root':
            if 'root'==i.strip().split(':')[0] and password==i.strip().split(':')[1]:
                choice=raw_input(choices).lower()
                if choice not in 'adu':
                    print '菜单选项错误！'
                    break
                if choice=='a':
                    New_user()
                    break
                if choice=='d':
                    delt()
                    break
                if choice=='u':
                    upd()
                    break
            else:
                print 'root管理员密码错误'
                break
        elif username==i.strip().split(':')[0] and password==i.strip().split(':')[1]:
            print '登录成功'
            break
    else:
        print '用户名或密码错误'
def delt():
    '''删除用户'''
    indexs=0
    with open(filename,'r') as f:
        userlist=f.readlines()
    username=raw_input('请输入要删除的用户名：').strip()
    if 'root'==username:
        print 'root用户不能被删除'
        return
    for i in userlist:
        if i.strip().split(':')[0]==username: 
            userlist[indexs]=''
            break
        indexs+=1
    else:
        print '用户名不存在！'
        return
    user_list=[i for i in userlist if i.strip()!='']
    f=open(filename,'w')
    f.writelines(user_list)
    f.close()
    print '成功删除用户：%s'%username
def upd():
    '''更改用户密码'''
    indexs=0
    with open(filename,'r') as f:
        userlist=f.readlines()
    username=raw_input('用户名用户名进行密码修改：').strip()
    for i in userlist:
        if i.strip().split(':')[0]==username:
            password=raw_input('请输入新的密码：').strip()
            userlist[indexs]='%s:%s%s'%(username,password,os.linesep)
            break
        indexs+=1
    else:
        print '用户名不存在！'
        return
    f=open(filename,'w')
    f.writelines(userlist)
    f.close()
    print '用户%s已成功修改密码'%username
def showmenu():
    '''菜单，提示用户进行注册、登录或退出'''
    prompt='''
n:注册用户
e:用户登录
q:退出
choice "neq":'''
    done=False
    while not done:
        chosen=False
        while not chosen:
            try:
                choice=raw_input(prompt).strip()[0].lower()
            except (EOFError,KeyboardInterrupt):
                choice='q'
            if choice not in 'neq':
                print >>sys.stderr,'invalid option,try again'
            else:
                chosen=True
        if choice=='q':done=True
        if choice=='n':New_user()
        if choice=='e':Old_user()
if __name__=='__main__':
    flag=1
    if not os.path.exists(filename):  #判断脚本所在目录下是否有'员工信息库'这个文件夹
        try:
            f=open(filename,'w') #不存在时创建该文件夹
            f.write('%s:%s%s'%('root','123456',os.linesep))
        except IOError,e:
            print e
            flag=0
        finally:
            f.close()
    if flag==1:  #文件夹存在时执行菜单程序
        print ''' 
        ********************************************
        *友情提示：root为管理员，初始密码为：'123456'*
        ******************************************** '''
        showmenu()

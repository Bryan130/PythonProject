#coding=gbk
import os,time
def ListFile(dirs):
    if os.path.isfile(os.path.abspath(dirs)):
        print '%s���ļ�����Ŀ¼'%os.path.abspath(dirs)
    else:
        print '%sĿ¼�µ��ļ���'%dirs
        for i in os.listdir(dirs):
            tup=os.stat(os.path.abspath(dirs)+os.sep+i)
            #��ӡ�ļ�������С��ʱ��
            print '%-50s %-10s %-30s'%(i,tup.st_size,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(tup.st_mtime)))
        print '************************************************************************************************'
        for i in os.listdir(dirs):
            try:
                if os.path.isdir(os.path.abspath(dirs)+os.sep+i):
                    ListFile(os.path.abspath(dirs)+os.sep+i)
            except WindowsError,diag:
                print '****************',diag,'*******************'
                continue

if __name__=='__main__':
    dirs=raw_input('��������ҵ�·����').strip()
    print "==========%s=========="%dirs
    ListFile(dirs)

            

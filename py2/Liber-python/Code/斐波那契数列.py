#coding=utf-8

# def feibo(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return feibo(n-1)+feibo(n-2)

def feibo(n):
    if 1 == n or 2 == n:
        return 1
    a = 1
    b = 1
    for x in range(1, n -1):
#         tmp = b
#         b = a + b
#         a = tmp
        b = a + b
        a = b - a
    return b
        
    
    
if __name__=='__main__':
    
    n=input('请输入一个整数：')
    #print '斐波那契数列弟%d项的值为：%d'%(n,feibo(n))
    for x in range(1, 11):
        print feibo(x),

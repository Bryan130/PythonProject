#coding=utf-8

def feibo(n):
    if n==1 or n==2:
        return 1
    else:
        return feibo(n-1)+feibo(n-2)
# def Sum(n):
#     Sum=0
#     for i in range(1,n+1):
#         Sum+=feibo(i)
#     return Sum
def Sum(n):
    if 1 == n:
        return feibo(1)
    return Sum(n - 1) + feibo(n)

if __name__=="__main__":
#     n=input('请输入一个整数：')
#     print '斐波纳列前%d项求和结果为：%d'%(n,Sum(n))
    for x in range(1, 11):
        print Sum(x),

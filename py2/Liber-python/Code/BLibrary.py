#coding=utf-8

import urllib2

def scanf_get(url):
    '''
	get接口
	'''
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    return res


def scanf_post(url,valuse):
    """
    post接口，需要传入参数
    """
    #data= (eval("("+''.join(valuse)+")"))
    opener = urllib2.build_opener()
    req = urllib2.Request(url, data=valuse,
                          headers={'Content-Type': 'application/json'})
    response = opener.open(req,None,600)
    d=response.read()
    opener.close()
    return d

def encode(self):
    return self.encode('utf-8')

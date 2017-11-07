#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Date:2017-07-18 11:19:17
# @Author:Bryan (bryan.lan@vengasz.com)
# @Link:http://.com
# @Use: This code uses python3

import redis

def conn_redis(host, port, db, password=None ):
    """
    redis
    |host     |port     |db  |password |

    """
    r = redis.Redis(host, port, db, password)
    return r


def flushdb(r):
    """
    |redis    |r       |
    """
    r.flushdb()



if __name__ == '__main__':
    host = "192.168.3.6"
    port = 6379
    db = 13
    redis_conn = conn_redis(host, port, db)
    print redis_conn

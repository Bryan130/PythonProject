#!/usr/bin/env python
# -*- coding : utf-8 -*-
# @Date      : 2017-03-28 10:24:37
# @Author  : Sniper
# @Email     : haitao.lan@longsys.com

"""
此模块用于解析命令行参数
"""

def xz(self, ass, men):
    print self**2
    print men**2
    print ass**2


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display a square of a given number",type=int)
    parser.add_argument("ass", help="display a square of a given number",type=int)
    parser.add_argument("men", help="display a square of a given number",type=int)
    args = parser.parse_args()
    a=args.square
    b=args.ass
    c=args.men
    xz(a,c,b)

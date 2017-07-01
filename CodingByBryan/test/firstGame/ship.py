# python3
# -*- coding:utf-8 -*-
# @Date:2017-06-29 23:37:48
# @Author:Bryan.Lan (bryan.lan@vengasz.com)
# @Link:https://github.com/Bryan130

import pygame


class Ship():
    def __init__(self, screen):
        '''
        初始化飞船并设置其初始位置
        '''
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('E:/Python36/PythonProject/CodingByBryan/test/firstGame/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''
        在指定位置绘制飞船
        '''
        self.screen.blit(self.image, self.rect)

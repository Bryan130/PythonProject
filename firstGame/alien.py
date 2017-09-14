#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Alien.py
# @Author : Bryan.Lan (18645555731@163.com)
# @Link   : https://github.com/Bryan130
# @Date   : 2017/8/22 下午5:10:46

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, srceen):
        """初始化外星人并设置其起始位置"""
        super(Alien, self).__init__()
        self.screen = srceen
        self.ai_settings = ai_settings

        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load(
            r'E:\PythonCode\py3\firstGame\images\alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕最上方附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

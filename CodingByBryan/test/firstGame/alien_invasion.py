# python3
# -*- coding:utf-8 -*-
# @Date:2017-06-29 23:01:12
# @Author:Bryan.Lan (bryan.lan@vengasz.com)
# @Link:https://github.com/Bryan130

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    '''
    初始化游戏并创建一个屏幕对象
    '''
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)


run_game()
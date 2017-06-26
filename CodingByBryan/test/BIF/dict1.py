#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Date:2017-06-21 19:52:12
# @Author:Bryan.Lan (bryan.lan@vengasz.com)
# @Link:https://github.com/Bryan130

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien["color"]=="":
        pass

for alien in aliens[:5]:
    print(alien)
print('...')

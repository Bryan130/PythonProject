#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Date:2017-06-21 19:52:12
# @Author:Bryan.Lan (bryan.lan@vengasz.com)
# @Link:https://github.com/Bryan130

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['C'],
    'eric': ['ruby', 'go'],
    'phil': ['python', 'JS']
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print('\n' + name.title() + "'s favorite languages is " +
              languages[0].title())
    else:
        print('\n' + name.title() + "'s favorite languages are:")
        for language in languages:
            print('\t' + language.title())

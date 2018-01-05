#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from db import sentence_frequency_query

def main():
    word = '曹操'
    frequency = sentence_frequency_query(word)

    print('查询：' + word + ' 获得以下结果：')
    print(frequency)

if __name__ == '__main__':
    main()

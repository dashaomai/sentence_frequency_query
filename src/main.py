#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from db import sentence_frequency_query

def main():
    _query('曹操')
    _query('耀C')
    _query('耀c')

def _query(word):
    frequency = sentence_frequency_query(word)

    print('查询：' + word + ' 获得以下结果：')
    print(frequency)

if __name__ == '__main__':
    main()

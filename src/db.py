# -*- coding: utf-8 -*-

import mysql.connector

# 数据库连接配置
db_config= {'user': 'root', 'password': 'docker', 'host': '192.168.137.1', 'database': 'hebangdata_sentences'}

# 从数据库内查询获得一个双字词语的出现频次
def sentence_frequency_query(word):
    return __db_template(__sentence_frequency_query, word=word)

def __sentence_frequency_query(conn, cursor, word):
    if (2 == len(word)):
        cursor.execute('SELECT count_0, count_1, count_2, count_3 FROM probability WHERE `initial`=%s AND `letter`=%s;', [word[0], word[1]])
        values = cursor.fetchall()

        if (0 < len(values)):
            # 查询到记录，返回查询结果
            return values[0]
        else:
            # 没查询到记录，则返回全 0 的频次结果
            return (0, 0, 0, 0)

        return values
    else:
        raise TypeError(word + ' was not the only 2 chars sentence.')

# 数据库连接和操作的模板函数
def __db_template(callback, **other):
    try:
        # 连接数据库
        conn = mysql.connector.connect(**db_config)
        conn.set_charset_collation('utf8mb4', 'utf8mb4_bin')
        cursor = conn.cursor()

        # 设置编码
        cursor.execute('SET NAMES utf8mb4')
        cursor.execute('SET CHARACTER SET utf8mb4')
        # cursor.execute('SET character_set_connection=utf8mb4_bin')

        # 进行函数回调，并返回回调计算的结果
        return callback(conn, cursor, **other)

    finally:
        cursor.close()
        conn.close()

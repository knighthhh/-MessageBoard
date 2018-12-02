#!/usr/bin/env python
# -*- coding:utf-8 -*-

from config import *
import pymysql

class MysqlClient(object):
    def __init__(self, host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DB,charset=MYSQL_CHARSET):
        self.client = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
        self.cursor = self.client.cursor()

    def save(self, sql):
        try:
            self.cursor.execute(sql)
            self.client.commit()
            print('存储成功')
            return True
        except:
            print('存储失败')
            self.client.rollback()
            return False

    def find_all(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except:
            return None

    def find_one(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchone()
            return results
        except:
            return None

    def delete(self,sql):
        try:
            self.cursor.execute(sql)
            self.client.commit()
            print('删除成功')
            return True
        except:
            print('删除失败')
            self.client.rollback()
            return False



#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import *
from tkinter.messagebox import *
from db import MysqlClient
import config
import time
import json

#主页面
class InputFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.word = StringVar()
        self.mean = StringVar()
        self.createPage()
        self.mysqlClient = MysqlClient()

    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='留言时间').grid(row=1, column=1, stick=W, pady=10)
        Label(self, text='留言内容').grid(row=1, column=2, stick=W, pady=10)
        results = self.get_all_message()

        row_num = 2
        for res in results:
            Label(self, text='      ').grid(row=row_num, column=1, stick=W, pady=10)
            Label(self, text='      ').grid(row=row_num, column=2, stick=W, pady=10)
            row_num += 1

        row_num = 2
        for res in results:
            time = res[2]
            word = res[3]
            Label(self, text=word).grid(row=row_num, column=1, stick=W, pady=10)
            Label(self, text=time).grid(row=row_num, column=2, stick=W, pady=10)
            row_num += 1

    def get_all_message(self):
        sql = "select * from content order by id DESC limit 15"
        mysqlClient = MysqlClient()
        find_res = mysqlClient.find_all(sql)
        return find_res


#查询留言
class QueryFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.mysqlClient = MysqlClient()
        # self.createPage()

    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)

        Label(self, text='留言时间').grid(row=1, column=3, stick=W, pady=10)
        Label(self, text='留言内容').grid(row=1, column=4, stick=W, pady=10)
        results = self.get_history()

        row_num = 2
        for res in results:
            Label(self, text='      ').grid(row=row_num, column=1, stick=W, pady=10)
            Label(self, text='      ').grid(row=row_num, column=2, stick=W, pady=10)
            Label(self, text='      ').grid(row=row_num, column=3, stick=W, pady=10)
            Label(self, text='      ').grid(row=row_num, column=4, stick=W, pady=10)
            row_num += 1

        row_num = 2
        for res in results:
            time = res[2]
            word = res[3]
            id = res[0]
            print(word,res[0])
            Button(self, text='修改', command=self.update).grid(row=row_num, column=1, stick=E, pady=10)
            Button(self, text='删除', command=lambda : self.delete(id=id)).grid(row=row_num, column=2, stick=E, pady=10)
            Label(self, text=time).grid(row=row_num, column=3, stick=W, pady=10)
            Label(self, text=word).grid(row=row_num, column=4, stick=W, pady=10)
            row_num +=1

    def get_history(self):
        name = config.USERNAME
        sql = "select * from content where(name='%s') order by id DESC limit 10"%(name)
        mysqlClient = MysqlClient()
        find_res = mysqlClient.find_all(sql)
        return find_res

    def update(self):
        pass

    def delete(self,id):
        print(id)
        sql = "delete from content where(id='%s') " % (id)
        del_res = self.mysqlClient.delete(sql)
        if del_res:
            showinfo(title='成功', message='删除成功')
            self.createPage()
        else:
            showinfo(title='失败', message='删除失败')


#发布新留言
class CountFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.mysqlClient = MysqlClient()
        self.message = StringVar()
        # self.createPage()


    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='请输入: ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.message, width=40).grid(row=2, stick=W)

        Button(self, text='发布', command=self.set_message).grid(row=10, column=2, stick=E, pady=10)


    def set_message(self):
        name = config.USERNAME
        message = self.message.get()
        publishDateStr = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        publishDate = int(time.time())
        sql = "insert into content(name,message,publishDateStr,publishDate) values ('%s','%s','%s','%s')" % (name,message,publishDateStr,publishDate)
        save_res = self.mysqlClient.save(sql)
        if save_res:
            showinfo(title='成功', message='发布成功')
        else:
            showinfo(title='失败', message='发布失败')

        return save_res


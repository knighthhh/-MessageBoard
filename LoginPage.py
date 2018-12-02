#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import *
from tkinter.messagebox import *
from MainPage import *
from RegPage import *
from db import MysqlClient
import config


class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (300, 180))  # 设置窗口大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()
        self.mysqlClient = MysqlClient()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='账户: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='登陆', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        # Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=E)
        Button(self.page, text='注册', command=self.register).grid(row=3, column=1, stick=E)

    def loginCheck(self):
        name = self.username.get()
        secret = self.password.get()
        sql = "select * from user where(name='%s' and password='%s')"%(name,secret)
        find_res = self.mysqlClient.find_one(sql)
        if find_res:
            self.page.destroy()
            MainPage(self.root)
            config.USERNAME = find_res[1]
        else:
            showinfo(title='错误', message='账号或密码错误！')

    def register(self):
        self.page.destroy()
        RegPage(self.root)

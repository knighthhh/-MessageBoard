#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import *
from tkinter.messagebox import *
from db import MysqlClient
import LoginPage

class RegPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (300, 200))  # 设置窗口大小
        self.username = StringVar()
        self.password = StringVar()
        self.repassword = StringVar()
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
        Label(self.page, text='确认密码: ').grid(row=3, stick=W, pady=10)
        Entry(self.page, textvariable=self.repassword, show='*').grid(row=3, column=1, stick=E)
        # Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=E)
        Button(self.page, text='注册', command=self.register).grid(row=4, column=1, stick=E)

    def register(self):
        name = self.username.get()
        password = self.password.get()
        repassword = self.repassword.get()
        if password==repassword:
            sql = "select * from user where(name='%s')" % (name)
            find_res = self.mysqlClient.find_one(sql)
            if find_res:
                showinfo(title='错误', message='该用户已存在')
            else:
                sql = "insert into user(name,password) values ('%s','%s')" % (name,password)
                add_res = self.mysqlClient.save(sql)
                if add_res:
                    showinfo(title='注册成功', message='注册成功')
                    self.page.destroy()

                    login = LoginPage.LoginPage(self.root)
                else:
                    showinfo(title='注册失败', message='注册失败')
        else:
            showinfo(title='错误', message='两次输入的密码不一致')
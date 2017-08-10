#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: e:\code\脚本\微信聊天机器人\test.py
# Project: e:\code\脚本
# Created Date: Thursday, August 10th 2017, 5:50:45 pm
# Author: JX
# -----
# Last Modified: Thu Aug 10 2017
# Modified By: JX
# -----
# Copyright (c) 2017 SYSU-SDCS-RJX
# 
# 学习使用
# github地址:https://github.com/jiaxin96
###

import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    itchat.send(msg.text, toUserName='filehelper')
    return msg.text

itchat.auto_login()
itchat.run()
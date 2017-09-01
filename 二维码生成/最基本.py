#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: e:\code\脚本\二维码生成\最基本.py
# Project: e:\code\脚本
# Created Date: Friday, September 1st 2017, 11:13:15 am
# Author: JX
# -----
# Last Modified: Fri Sep 01 2017
# Modified By: JX
# -----
# Copyright (c) 2017 SYSU-SDCS-RJX
# 
# 学习使用
# github地址:https://github.com/jiaxin96
###
import qrcode 
img = qrcode.make('https://www.baidu.com')
img.save('test.png')

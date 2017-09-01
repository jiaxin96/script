#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: e:\code\脚本\二维码生成\gen.py
# Project: e:\code\脚本
# Created Date: Friday, September 1st 2017, 10:50:29 am
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
 
 

'''
version表示大小取值[1,40]
最小尺寸 1 会生成 21 * 21 的二维码，
version 每增加 1，生成的二维码就会添加 4 尺寸，
例如 version 是 2，则生成 25 * 25 的二维码。

error_correction指定二维码的容错系数，分别有以下4个系数:
1.ERROR_CORRECT_L: 7%的字码可被容错
2.ERROR_CORRECT_M: 15%的字码可被容错
3.ERROR_CORRECT_Q: 25%的字码可被容错
4.ERROR_CORRECT_H: 30%的字码可被容错

参数 box_size 表示二维码里每个格子的像素大小。
参数 border 表示边框的格子厚度是多少（默认是4）。
'''
# 代码有问题　无法识别
import qrcode 
qr = qrcode.QRCode(   
  version=1,   
  error_correction=qrcode.constants.ERROR_CORRECT_L,   
  box_size=10,   
  border=4, 
) 
qr.add_data('https://www.baidu.com')
qr.make(fit=True)

img = qr.make_image()
img.save('test.png')

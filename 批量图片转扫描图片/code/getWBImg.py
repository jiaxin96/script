#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\Ren_J\Desktop\test\ch_img\code\getWBImg.py
# Project: c:\Users\Ren_J\Desktop\test\ch_img
# Created Date: Wednesday, August 16th 2017, 3:54:03 pm
# Author: JX
# -----
# Last Modified: Wed Aug 16 2017
# Modified By: JX
# -----
# Copyright (c) 2017 SYSU-SDCS-RJX
# 
# 学习使用
# github地址:https://github.com/jiaxin96
###
#-*- coding:utf8 -*-
from PIL import Image
import os
import os.path

for parent, dirnames, filenames in os.walk("../data/"):
    for filename in filenames:
        im = Image.open("../data/" + filename)
        im = im.convert("P")
        im2 = Image.new("P",im.size,255)


        for x in range(im.size[1]):
            for y in range(im.size[0]):
                pix = im.getpixel((y,x))
                if abs(pix)<116:
                    im2.putpixel((y,x),0)

        im2.convert('RGB').save('../ans/'+filename)
        im.close()
        im2.close()
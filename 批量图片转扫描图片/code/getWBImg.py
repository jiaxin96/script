#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\Ren_J\Desktop\test\ch_img\code\getWBImg.py
# Project: c:\Users\Ren_J\Desktop\test\ch_img
# Created Date: Wednesday, August 16th 2017, 3:54:03 pm
# Author: JX
# -----
# Last Modified: Tue Aug 22 2017
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

for parent, dirnames, filenames in os.walk("../data/test"):
    for filename in filenames:
        im = Image.open("../data/test/" + filename)
        im = im.convert("P")

        if (im.size[0] > im.size[1]):
            im = im.transpose(Image.ROTATE_270)
        im2 = Image.new("P",im.size,255)
        print(im.size[1])
        l = im.size[1] / 2;
        w = im.size[0] / 2;
        for x in range(im.size[1]):
            for y in range(im.size[0]):
                pix = im.getpixel((y,x))
                # if abs(pix)<105:
                #     im2.putpixel((y,x),0)
                if x > l:
                    if abs(pix)<120+(40/((2*w)**2))*y*(w*2-y):
                        im2.putpixel((y,x),0)
                else:
                    if abs(pix)<125:
                        im2.putpixel((y,x),0)

        im2.convert('RGB').save('../ans/'+filename)
        im.close()
        im2.close()
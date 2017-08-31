#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: e:\code\脚本\验证码生成\英文数字验证码\vcodegen.py
# Project: e:\code\脚本
# Created Date: Thursday, August 31st 2017, 12:12:45 am
# Author: JX
# -----
# Last Modified: Thu Aug 31 2017
# Modified By: JX
# -----
# Copyright (c) 2017 SYSU-SDCS-RJX
#
# 说明: 
#文字没有角度的变化和扭曲
#
# 学习使用
# github地址:https://github.com/jiaxin96
###

from PIL import Image,ImageFilter,ImageDraw,ImageFont
import random

#产生随机汉字、字母和数字
def rndChar():
     #产生0-9随机数字
     numChr = str(random.randint(0,9))
     #产生大写字母A-Z,对比ASK码
     letChr = chr(random.randint(65,90))
     #产生随机的一个汉字
     chChr =random.choice("我爱北京天安门")
     #随机返回三种类型之一
     return random.choice((numChr,chChr,letChr))

 #得到随机的颜色，0-255 RGB颜色表
def rndColor():
    return (random.randint(130,255),random.randint(120,255),random.randint(180,255))
def rndColor2():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))


#定义输出图片大小
width = 240
height = 60
#定义初始白色图片
image = Image.new('RGB',(width,height),(255,255,255))
#创建Font对象，字体
font = ImageFont.truetype('C:\Windows\Fonts\STLITI.TTF',40)

#创建Draw对象，即创建一个可以对Image操作的对象
draw = ImageDraw.Draw(image)
#在图片中填充随机像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())

#在图像中输出文字
for t in range(4):
    draw.multiline_text((60*t+10,10),rndChar(),font=font,fill=rndColor2())

#滤镜模糊
image = image.filter(ImageFilter.MinFilter)
image.save('code.jpeg','jpeg')
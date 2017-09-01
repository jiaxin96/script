#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: e:\code\脚本\网站图片获取\code\getImg.py
# Project: e:\code\脚本
# Created Date: Friday, September 1st 2017, 4:33:07 pm
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
import requests
import re
imgpath = "../img/"

url = "https://www.qiushibaike.com/imgrank/"

r = requests.get(url)
r.encoding = r.apparent_encoding

# print(str(r.text))

imgsSrc = re.findall(r'<img src="(.*(.gif|.jpg|.jpeg|.GIF|.JPG|.JPEG|.png)).*"' , r.text)
# print(imgsSrc)


for imgSrc in imgsSrc:
    name = imgSrc[0].split('/')[-1]
    r = requests.get('http:'+imgSrc[0])
    r.encoding = r.apparent_encoding
    with open(imgpath+name, "wb+") as f:
        f.write(r.content)
        f.close()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 00:43:38 2019

@author: darkhan
"""

import os
from random import randint
import glob
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

txt_files = glob.glob("*.txt")
for file_name in txt_files:
    name = "altynai-"+str(i)+".txt"
    name2 = "altynai-"+str(i)+".mp3"
    file = open(file_name,"r")
    content = file.read()
    if(hasNumbers(content)):
        print(content)
        print(name)
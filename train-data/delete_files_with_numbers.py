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
    file_name2 = file_name.split(".")[0]+".mp3"
    file = open(file_name,"r")
    content = file.read()
    if 'төртеуміздің' in content:
        print(content)
        print(file_name)
print(ord('A'))
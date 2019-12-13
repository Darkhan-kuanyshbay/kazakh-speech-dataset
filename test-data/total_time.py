#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 17:35:17 2019

@author: darkhan
"""

from mutagen.mp3 import MP3
import glob,os
duration = 0
for file in glob.glob("*.mp3"):
    audio = MP3(file)
    duration = duration + audio.info.length
print(duration)
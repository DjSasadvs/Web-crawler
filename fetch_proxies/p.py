#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import logging
import json
import codecs
from collections import OrderedDict

proxyes=['sdf','sdf']
fileS = codecs.open('settings.py', 'r', encoding='utf-8').readlines()
fileL = len(fileS) - 1
pL = len(proxyes) - 1
index = 0;
for i in range(fileL):
    if 'ip_port' in fileS[i][2:8]
        fileS[i] = fileS[i].replace(fileS[i], proxyes[index])
        index ++
 open('settings.py','w').writelines(fileS)

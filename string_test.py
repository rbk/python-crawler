#!/usr/bin/env python
# encoding=utf8
import sys 
import os
import re

url = '/https://cliniciansbrief.com/'
# url = url.replace('\/$', 'test')
url = re.sub(r"\/$",  '', url) # replace last slash
url = re.sub(r"^\/",  '', url) # replace first slash
print(url)


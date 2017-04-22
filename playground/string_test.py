#!/usr/bin/env python
# encoding=utf8
import sys 
import os
import re

url = 'https://brief.media/about'
# url = url.replace('\/$', 'test')
url = re.sub(r"\/$",  '', url) # replace last slash
url = re.sub(r"^\/",  '', url) # replace first slash
# print(url)

domain_regex = 'http(?:s)?:\/\/(?:[\w-]+\.)*([\w-]{1,63})(?:\.(?:\w{3}|\w{2}))(?:$|)'
has_domain = re.search(domain_regex, 'https://brief.media/careers')
print(has_domain)
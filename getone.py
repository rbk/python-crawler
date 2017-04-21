#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import ssl
import smtplib
import re
from time import localtime, strftime
import cgi
import cgitb
cgitb.enable()
# from urllib import request
from urllib.request import Request, urlopen

# from bs4 import BeautifulSoup

# html parser
# https://docs.python.org/2/library/htmlparser.html
# from HTMLParser import HTMLParser

# url 
url = 'https://www.cliniciansbrief.com/'
context = ssl._create_unverified_context()
ssl._create_default_https_context = ssl._create_unverified_context
headers={'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}
response = Request(url, headers=headers)
html = urlopen(response).read()
html = re.escape(html)


# db.query("insert into submissions (url, html) values ('" + url + "', '" + html + "')")

# soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())
# print(soup.title.string)
# print(soup.find('meta'))

# for link in soup.find_all('a'):
#     print(link.get('href'))
    # print(link)

# print(soup.get_text())

# file write example
## filename = 'test.html'
## target = open(filename, 'w')
## target.write('test')



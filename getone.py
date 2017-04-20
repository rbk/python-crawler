#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# db
import mysql.connector

config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 's1',
  'raise_on_warnings': True,
  'use_pure': False,
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()


print cursor

# time
from time import localtime, strftime

# cgi, to get params
import cgi

# enable debugging
import cgitb
cgitb.enable()

from bs4 import BeautifulSoup

# html parser
# https://docs.python.org/2/library/htmlparser.html
# from HTMLParser import HTMLParser

# url getter
import urllib2

response = urllib2.urlopen('https://mattsatv.com/')
html = response.read()

# soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())
# print(soup.title.string)
# print(soup.find('meta'))

# for link in soup.find_all('a'):
#     print(link.get('href'))
    # print(link)

# print(soup.get_text())
filename = 'test.html'
target = open(filename, 'w')
target.write('test')


cnx.close()

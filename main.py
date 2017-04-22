from bs4 import BeautifulSoup
import ssl
import smtplib
import re
from time import localtime, strftime
import sys 
import os
import pymysql
import cgitb
cgitb.enable()
from urllib.request import Request, urlopen
print('>>> ' + sys.version)

import settings
settings.db_conf()
settings.dbhost = 'localhost'
settings.dbuser = 'root'
settings.dbpassword = 'password'
settings.dbname = 's1'
# import setup_database

import test_link


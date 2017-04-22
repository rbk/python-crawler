from bs4 import BeautifulSoup
import ssl
import smtplib
import re
from time import localtime, strftime
import cgi
import cgitb
import sys 
import os
import pymysql
print('>>> ' + sys.version)
cgitb.enable()
from urllib.request import Request, urlopen





from my_db import create_tables
from my_db import list_links
# print(conn)
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
import url_string_cleaner as strop
# print('>>> ' + sys.version)

import settings
settings.db_conf()
settings.dbhost = 'localhost'
settings.dbuser = 'root'
settings.dbpassword = 'password'
settings.dbname = 's1'

# import setup_database



import curl

# while count < 100
# 	submit a url
# 	download all links and image
# 	query links
# 	submit url


result = curl.get_page('https://www.cliniciansbrief.com')
html = result['html']
url = result['url']
soup = BeautifulSoup(html, 'html.parser')
print(soup.title.string + ' - ' + result['url'])


# import save_submission
# 
# for obj in soup.find_all('meta'):
# 	# print(obj)
# 	property = obj.get('property')
# 	if property == 'og:image' or property == 'og:description' :
# 		print(obj.get('content'))
# 	name = obj.get('name')
# 	if name == 'description' :
# 		print(obj.get('content'))

# save_submission.save('string')

# html_escaped = re.escape(html)
# soup = BeautifulSoup(html, 'html.parser')



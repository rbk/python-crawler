#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import ssl
import smtplib
import re
from time import localtime, strftime
import cgi
import cgitb
cgitb.enable()
from urllib.request import Request, urlopen
import sqlite3
dbname = 'search.db'
print('>>> Connecting to SQLITE database: ' + dbname)
conn = sqlite3.connect(dbname)
print('>>> Creating cursor')
c = conn.cursor()

submission_table = '''create table IF NOT EXISTS submissions (
	id int auto_increment primary key,
	url varchar(255) not null,
	html longtext not null
)'''

print('>>> Running SQL: ' + submission_table)
c.execute(submission_table)
conn.commit()

# url
url1 = 'http://www.useragentstring.com/pages/useragentstring.php'
url = 'http://www.useragentstring.com/pages/useragentstring.php?name=Accoona-AI-Agent'
context = ssl._create_unverified_context()
ssl._create_default_https_context = ssl._create_unverified_context

agent1 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
agent = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
headers={'User-Agent': agent1}
response = Request(url, headers=headers)
html = urlopen(response).read()
html = re.escape(html)

# html = 'test'

c.execute('INSERT INTO submissions (url, html) VALUES ("'+url+'", "'+html+'")')
conn.commit()



conn.close()
print('>>> Closing DB connection')
print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))





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



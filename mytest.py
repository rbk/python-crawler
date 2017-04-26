from bs4 import BeautifulSoup
import ssl
import smtplib
import re
from time import localtime, strftime
import time
import sys 
import os
import pymysql
import cgitb
cgitb.enable()
from urllib.request import Request, urlopen
import url_string_cleaner as url_man
import curl
# print('>>> ' + sys.version)
# 
conn = pymysql.connect(
	host='localhost',
	user='root',
	password='password',
	db='s1',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor
)
a = conn.cursor()




def addlinks(count):
	# print(links)
	print(len(links))
	
	try:
		html = curl.get_page(links[len(links)-1])
		if html:
			soup = BeautifulSoup(html, 'html.parser')
			more_links = soup.find_all('a')
			print(len(more_links))

			for obj in more_links :
				link = obj.get('href')

				isHttps = re.search((r"https"), link)
				isHttp = re.search((r"http"), link)
				hasSlashes = re.search((r"\/\/"), link)
				if not hasattr(isHttp, 'group') and not hasattr(isHttps, 'group') and hasattr(hasSlashes, 'group'):
					link = 'http:' + link

				excludesDomain = True
				validUrl = True
				# excludesDomain = url_man.does_not_match(link)
				# validUrl = url_man.valid_url(link)

				# time.sleep(.2)

				if link not in links:
					links.append(link)
					link_count = link_count + 1
					print(str(link_count) + ' - ' + link)
					try:
						add_link = 'INSERT INTO links (`url`) VALUES ("'+link+'")'
						q = a.execute(add_link)
						conn.commit()
						print('Success: ' + href)
					except:
						print('Not inserted: ' + href)
				else:
					# print('Doesn\'t meet criteria: ' + link)				
					'null'
	except:
		'null'

def run():
	global count
	global links
	global max_count
	global link_count
	count = 0
	max_count = 1000
	link_count = 0
	links = ['https://www.reddit.com/']
		
	while count < max_count:
		# print(count)
		# print(len(links))
		addlinks(count)
		count = count + 1

	# print(links)

run()


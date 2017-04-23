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
# print('>>> ' + sys.version)

import settings
settings.db_conf()
settings.dbhost = 'localhost'
settings.dbuser = 'root'
settings.dbpassword = ''
settings.dbname = 's1'

# import setup_database



import curl
import save_submission

def run():
	links = save_submission.get_links_that_dont_exist_in_submissions()
	if not links :
		links = [{'url':'http://richardkeller.net'}]
	# print(links)
	for u in links :
		# print(u['url'])
		result = curl.get_page(u['url'])
		html = result['html']
		url = result['url']
		title = result['title']
		save_submission.save(title, url, html)
	# run()

# run()

# print("Start : %s" % time.ctime())
# time.sleep( 5 )
# print("End : %s" % time.ctime())

# Algorithm
# while count < 100
# 	submit a url
# 	download all links and image
# 	query links
# 	submit url


def get_links(html, url):

	print('>>> getting links')

	links = []

	links_to_exlcude = [
		'#',
		'#content',
	]
	matches_to_exclude = [
		'facebook',
		'google',
		'tel:',
		'mailto:'
	]

	domain = url_man.clean_domain(url)
	# print(domain)

	soup = BeautifulSoup(html, 'html.parser')
	for obj in soup.find_all('a'):
		
		href = obj.get('href')
		match = False
		correct_domain = False
		not_in_array = False

		if re.search(domain, href) :
			correct_domain = True

		for regex in matches_to_exclude :
			if re.search(regex, href):
				match = True
				break

		if href not in links :
			not_in_array = True

		if href not in links_to_exlcude and not match and correct_domain and not_in_array:
			links.append(href)
			print(href)
	return links


def init() :
	url = 'https://mattsatv.com/'
	html = curl.get_page(url)
	if html :
		get_links(html, url)

init()

# print(links)

# fomrmat results
		# soup = BeautifulSoup(html, 'html.parser')
		# title = soup.title.string
		# html_escaped = re.escape(html)

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



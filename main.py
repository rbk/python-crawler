from bs4 import BeautifulSoup
import ssl
import smtplib
import re
from time import localtime, strftime
import time
import sys 
import os
import pymysql
from urllib.request import Request, urlopen
import url_string_cleaner as url_man

# Database Setup
import settings
settings.db_conf()
settings.dbhost = 'localhost'
settings.dbuser = 'root'
settings.dbpassword = 'password'
settings.dbname = 's1'

# import setup_database

import db_connection
conn = db_connection.db_conn()
a = conn.cursor()


import curl
import save_submission


def get_links(html, url):
	
	links = []
	links_to_exlcude = [
		'#',
		'#content',
	]
	matches_to_exclude = [
		'facebook.com',
		'twitter.com'
		'google.com',
		'tel:',
		'mailto:',
		'javascript:',
		'ftp:\/\/',
		'\/\/goo.gl',
		'\/\/(\*).wikipedia.org',
		'(\.gifv$)',
		'http:\/\/imgur\.com',
		'http:\/\/i\.imgur\.com',
		'(pdf)$',
		'(gif)$',
		'(gifv)$',
		'(jpg)$',
		'(png)$',
	]

	domain_clean = url_man.clean_domain(url)
	has_protocol = re.search(r"http:\/\/|https:\/\/|\/\/", url)
	if hasattr(has_protocol, 'group'):
		protocol = has_protocol.group(0)
	else: 
		protocol = 'http://'

	no_http = re.search(r"http:\/\/|https:\/\/", url)
	if not hasattr(no_http, 'group') and hasattr(has_protocol, 'group'):
		url = 'https:' +url

	soup = BeautifulSoup(html, 'html.parser')
	for obj in soup.find_all('a'):
		href = obj.get('href')

		if not href:
			href = ''

		match = False
		correct_domain = False
		not_in_array = False
		

		domain_regex = '\/\/(?:[\w-]+\.)*([\w-]{1,63})(?:\.(?:\w{3}|\w{2}))'
		has_domain = re.search(domain_regex, href)
		if hasattr(has_domain, 'group'):
			has_domain = True
		else:
			has_domain = False
		
		for regex in matches_to_exclude :
			exclude_match = re.search(regex, href)
			if hasattr(exclude_match, 'group'):
				match = True
				break

		# NORMALIZE URL
		if not has_domain and not match:
			href = url_man.rm_first_slash(href);
			href = protocol + domain_clean + '/' +  href

		# Limits to domain url passed in the beginning
		# Exclude social networks instead
		if re.search(domain_clean, href) :
			correct_domain = True

		if href not in links :
			not_in_array = True

		href = url_man.rm_last_slash(href)
		# print(href)

		if href not in links_to_exlcude and not_in_array and not match:
			# print(href)
			links.append(href)
			try:
				add_link = 'INSERT INTO links (`url`) VALUES ("'+href+'")'
				q = a.execute(add_link)
				conn.commit()
				print('SAVED: ' + href)
				# print('[' + counter + '] Success: ' + href)
				counter = counter + 1
			except:
				print('EXISTS PROBABLY: ' + href)
				'null'
			
			try:
				domain = url_man.clean_domain(href)
				add_domain = 'INSERT INTO domain (`domain`) VALUES ("'+domain+'")'
				q = a.execute(add_domain)
				conn.commit()
				print('Domain added: ' + domain)
			except:
				'null'

	return links

def crawl(url) :
	global counter
	counter = 0
	max_count = 1000
	links_array = [url]

	for link in links_array:
		try:
			print('Trying...' + link)
			html = curl.get_page(link)
			# print(html)
			if html:
				new_links = get_links(html, link)
				# print(len(new_links))
				for new_link in new_links:
					if new_link not in links_array:
						links_array.append(new_link)
		except:
			'null'

crawl('http://dmoztools.net/')



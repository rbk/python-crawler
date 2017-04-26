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
settings.dbpassword = 'password'
settings.dbname = 's1'

# import setup_database

import db_connection
conn = db_connection.db_conn()
a = conn.cursor()

import curl
import save_submission

def run():
	links = save_submission.get_links_that_dont_exist_in_submissions()
	if not links :
		links = [{'url':'http://richardkeller.net'}]
	for u in links :
		result = curl.get_page(u['url'])
		html = result['html']
		url = result['url']
		title = result['title']
		save_submission.save(title, url, html)



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
	]

	domain = url_man.clean_domain(url)
	# print(domain)

	soup = BeautifulSoup(html, 'html.parser')
	for obj in soup.find_all('a'):

		
		href = obj.get('href')
		match = False
		correct_domain = False
		not_in_array = False

		domain_regex = '\/\/(?:[\w-]+\.)*([\w-]{1,63})(?:\.(?:\w{3}|\w{2}))'
		has_domain = re.search(domain_regex, href)

		# NORMALIZE URL
		if not has_domain:
			# remove first slash
			# remove last slash
			# get domain protocol
			href = domain + '/' +  href

		# Limits to domain url passed in the beginning
		# Exclude social networks instead
		if re.search(domain, href) :
			correct_domain = True

		for regex in matches_to_exclude :
			if re.search(regex, href):
				match = True
				break

		if href not in links :
			not_in_array = True

		if href not in links_to_exlcude and not match and not_in_array:
			links.append(href)
			try:
				add_link = 'INSERT INTO links (`url`) VALUES ("'+href+'")'
				q = a.execute(add_link)
				conn.commit()
				print('Success: ' + href)
			except:
				print('Not inserted: ' + href)
	return links

def crawl(links) :
	links = 'select url from links'
	q = a.execute(links)
	links = a.fetchall()

	for link in links:
		# time.sleep(1)
		try:
			html = curl.get_page(link['url'])
			if html:
				links = get_links(html, link['url'])
		except:
			'null'
	crawl(links)


def init() :
	url = 'https://www.cliniciansbrief.com'
	url = 'https://www.visitorkit.com/'
	html = curl.get_page(url)
	if html :
		links = get_links(html, url)
		crawl(links)
	else: 
		print('invalid link')

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



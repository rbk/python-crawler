from bs4 import BeautifulSoup
import re
import time
import os
import string_clean as url_man
from multiprocessing import Pool as ThreadPool 
import requests

uas = [
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
	'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
]

def get_links(html, url):

	links = []
	matches_to_exclude = [
		'youtu\.be',
		'microsoftstore\.com',
		'market\.android\.com',
		'l\.messenger\.com',
		'itunes\.apple\.com',
		'facebook\.com',
		'twitter\.com',
		'google\.com',
		'amazon.com'
		'tel:',
		'mailto:',
		'javascript:',
		'ftp:\/\/',
		'\/\/goo.gl',
		'\/\/(\*).wikipedia.org',
		'http:\/\/imgur\.com',
		'http:\/\/i\.imgur\.com',
		'(\.pdf)$',
		'(\.gif)$',
		'(\.gifv)$',
		'(\.jpg)$',
		'(\.jpeg)$',
		'(\.png)$',
		'(\.svg)$',
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

		for regex in matches_to_exclude :
			exclude_match = re.search(regex, href)
			if hasattr(exclude_match, 'group'):
				match = True
				break
		if not match:
			links.append(href)
	return links


def crawl(url):
	links = open('LINKS.txt', 'r').read().splitlines()
	html = requests.get(url).text
	new_links = get_links(html, url)
	for link in new_links:
		if link not in links:		
			with open('LINKS.txt', 'a+') as f:
				print(link)
				f.write(link + "\n")
				links.append(link)
			time.sleep(1)
		else:
			pass
			# print("[{}]".format(int(time.time())), 'link exists...', link)
	crawl(link)

urls = [
	'https://nytimes.com',
	'https://reddit.com',
	'https://yahoo.com',
	'https://wired.com',
	'https://techcrunch.com',
	'https://en.wikipedia.org',
	'http://www.thealphaweb.com',
	'https://www.thesaurus.com',
	'https://www.house.gov'
]

# crawl('https://netlify.com')

pool = ThreadPool(len(urls)-1)
results = pool.map(crawl, urls)
pool.close() 
pool.join() 


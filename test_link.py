#!/usr/bin/env python
# encoding=utf8

from bs4 import BeautifulSoup
import re
import ssl
from urllib.request import Request, urlopen

def rm_first_slash(str) :
	return re.sub(r"^\/",  '', str)

def rm_last_slash(str) :
	return re.sub(r"\/$",  '', str)

def rm_protocol(str) :
	return re.sub(r"http:\/\/|https:\/\/|\/\/", '', str)

def clean_domain(str) :
	str = rm_first_slash(str)
	str = rm_last_slash(str)
	str = rm_protocol(str)
	return str

def get_user_agent() :
	agents = [
		'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
	]
	return agents[1]

url = 'http://mattsatv.com/'
url =  rm_last_slash(url)
domain = clean_domain(url)

print('>>>' + str(url))
print('>>>' + str(domain))

context = ssl._create_unverified_context()
ssl._create_default_https_context = ssl._create_unverified_context
headers={'User-Agent': get_user_agent()}
response = Request(url, headers=headers)
html = urlopen(response).read().decode('utf8')
html_escaped = re.escape(html)
soup = BeautifulSoup(html, 'html.parser')
# print(html)
for link in soup.find_all('a'):
	print(link.get('href'))


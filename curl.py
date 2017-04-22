#!/usr/bin/env python
# encoding=utf8

from bs4 import BeautifulSoup
import re
import ssl
import urllib
from urllib.request import Request, urlopen
import url_string_cleaner as strop
import user_agents
import url_string_cleaner as url_man


def get_page(url) :

	if not url_man.valid_url(url) :
		return 'Invalid url'

	# url =  strop.rm_all_after_domain(url)
	domain = strop.clean_domain(url)
	context = ssl._create_unverified_context()
	ssl._create_default_https_context = ssl._create_unverified_context
	headers={'User-Agent': user_agents.get_one(0)}
	try:
		response = Request(url, headers=headers)
		html = urlopen(response).read().decode('utf8')
		soup = BeautifulSoup(html, 'html.parser')
		title = soup.title.string
		html_escaped = re.escape(html)
		obj = {'html': html, 'url': url, 'title': title }
		return obj
	except urllib.error.URLError as e:
		obj = {'html': '', 'url': '', 'title': '' }
		return obj
		# ResponseData = e.read().decode("utf8", 'ignore')
		# return ResponseData

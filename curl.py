#!/usr/bin/env python
# encoding=utf8

import re
import ssl
import urllib
from urllib.request import Request, urlopen
import user_agents
import url_string_cleaner as url_man


def get_page(url) :

	if not url_man.valid_url(url) :
		return 'Invalid url'

	domain = url_man.clean_domain(url)
	context = ssl._create_unverified_context()
	ssl._create_default_https_context = ssl._create_unverified_context
	headers={'User-Agent': user_agents.get_one(0)}
	try:
		response = Request(url, headers=headers)
		html = urlopen(response).read()
		# .decode('utf8')
		return html
	except:
		'null'
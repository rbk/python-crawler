#!/usr/bin/env python
# encoding=utf8

import re
import ssl
from urllib.request import urlopen, Request
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
		request = Request(url, headers=headers)
		response = urlopen(request, timeout=3)
		# print(response.getcode())
		return response.read()
		# .decode('utf8') # Use for saving html to database
		return html
	except:
		# print(response.getcode())
		'null'


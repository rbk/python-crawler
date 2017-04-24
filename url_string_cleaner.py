#!/usr/bin/env python
# encoding=utf8

import re
import settings

settings.regex();

def rm_first_slash(url) :
	return re.sub(r"^\/",  '', url)

def rm_last_slash(url) :
	return re.sub(r"\/$",  '', url)

def rm_protocol(url) :
	return re.sub(r"http:\/\/|https:\/\/|\/\/", '', url)

def rm_all_after_domain(url) :
	protocol = re.search(r"http:\/\/|https:\/\/|\/\/", url)
	if hasattr(protocol, 'group') :
		protocol = protocol.group(0)
	else:
		protocol = 'http://'
	url = clean_domain(url)
	url = re.sub(r"\/(.*)",  '', url)
	return protocol + url

def clean_domain(url) :
	url = rm_protocol(url)
	url = rm_first_slash(url)
	url = rm_last_slash(url)
	url = re.sub(r"\/(.*)",  '', url)
	return url

def valid_url(url) :
	potential_url = re.search(settings.domain_regex, url)
	if hasattr(potential_url, 'group') :
		return True
	else :
		return False
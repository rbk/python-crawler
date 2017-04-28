import re

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



href = 'http://i.imgifvur.com/5bzjxSR.gifv'

for regex in matches_to_exclude :
	exclude_match = re.search(regex, href)
	if hasattr(exclude_match, 'group'):
		print('MATCHED - EXCLUDE')
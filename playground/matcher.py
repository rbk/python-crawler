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

# http://i.imgifvur.com/5bzjxSR.gifv
# http://i.imgur.com/5bzjxSR.gif
# http://i.imgur.com/5bzjxSR.jpg
# http://i.imgur.com/5bzjxSR.pdf
# gifvhttp://imgur.com/a/5AYF6 

href = 'http://i.imgifvur.com/5bzjxSR.gifv'

for regex in matches_to_exclude :
	exclude_match = re.search(regex, href)
	if hasattr(exclude_match, 'group'):
		print('MATCHED - EXCLUDE')
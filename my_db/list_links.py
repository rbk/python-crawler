#!/usr/bin/env python
# encoding=utf8

url = 'https://www.cliniciansbrief.com/'
context = ssl._create_unverified_context()
ssl._create_default_https_context = ssl._create_unverified_context
agent1 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
headers={'User-Agent': agent1}
response = Request(url, headers=headers)
html = urlopen(response).read().decode('utf8')
html_escaped = re.escape(html)
soup = BeautifulSoup(html, 'html.parser')
for link in soup.find_all('a'):
	print(link.get('href'))



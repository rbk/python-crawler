

import pymysql

conn = pymysql.connect(
	host='localhost',
	user='root',
	password='password',
	db='s1',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor
)
a = conn.cursor()

url = 'https://www.reddit.com/user/DChalos'
# Check link before crawling
check_link = 'SELECT url FROM links WHERE url ="'+url+'"'
linked = a.execute(check_link)
print(linked)

if linked:
	print('found')
else:
	print('not found')
		# SELECT url FROM links WHERE url ="https://www.reddit.com/user/DChalo")
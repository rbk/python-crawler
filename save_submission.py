import re
import db_connection
conn = db_connection.db_conn()
a = conn.cursor()

def get_links_that_dont_exist_in_submissions():
	sql = '''
	SELECT l.url
	FROM link_queue l
	LEFT JOIN submissions s
	ON l.did = s.id
	WHERE NOT s.url = l.url 
	'''
	a.execute(sql)
	return a.fetchall()

def save(title, url, html) :
	if title and url and html :
		print(title)
		html_escaped = re.escape(html)
		add_submission = 'INSERT INTO submissions (title, url, html) VALUES ("'+title+'", "'+url+'", "'+html_escaped+'")'
		id = a.execute(add_submission)
		conn.commit()
		print(id)

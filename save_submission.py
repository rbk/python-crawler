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
	result = a.execute(sql)
	return results

def save(string) :
	print(string)
# page_title = soup.title.string

# add_submission2 = 'INSERT INTO submissions (title, url, html) VALUES ("'+page_title+'", "'+url+'", "'+html_escaped+'")'


# print('>>> save page')
# domain_id = a.execute(add_submission2)
# domain_id = str(domain_id)
# print(type(domain_id))
# conn.commit()
conn.close()
from bs4 import BeautifulSoup
import url_string_cleaner as url_man
import re
import db_connection
conn = db_connection.db_conn()
a = conn.cursor()

def get_links_that_dont_exist_in_submissions():
	sql = '''
	SELECT l.url
	FROM link_queue l
	left JOIN submissions s
	ON l.url = s.url
	WHERE s.url != l.url
	'''
	a.execute(sql)
	return a.fetchall()

def save(title, url, html) :
	if title and url and html :
		print(title)
		html_escaped = re.escape(html)
		
		add_submission = 'INSERT INTO submissions (title, url, html) VALUES ("'+title+'", "'+url+'", "'+html_escaped+'")'
		id = a.execute(add_submission)

		add_domain_key = 'INSERT INTO domain_key (sid) VALUES ("'+str(id)+'")'
		domain_id = a.execute(add_domain_key)

		conn.commit()
		add_links(title, url, html, domain_id)


def add_links(title, url, html, domain_id) :
	# Get Links
	print('>>> get links')
	links = []
	soup = BeautifulSoup(html, 'html.parser')
	
	links_to_exlcude = [
		'#',
		'#content',
		'tel:',
		'mailto:'
	]
	
	for link in soup.find_all('a'):
		href = link.get('href')
		if href not in links_to_exlcude :
			links.append(href)


	# print(links)
	# print(links)
	# 

	for link in links:
		domain_regex = '\/\/(?:[\w-]+\.)*([\w-]{1,63})(?:\.(?:\w{3}|\w{2}))'
		has_domain = re.search(domain_regex, link)

		# print(has_domain)
		if has_domain:
				link = re.sub(r"\/$",  '', link) # replace last slash
		else :
			link = re.sub(r"^\/",  '', link) # replace first slash
			link = url + '/' + link

		# print(link) # DEBUG

		domain = url_man.clean_domain(link)

		if domain in link :
			try:
				# print(link)
				add_link = 'INSERT INTO link_queue (`url`, `did`) VALUES ("'+link+'", "'+str(domain_id)+'")'
				q = a.execute(add_link)
				conn.commit()
			except:
				'null'
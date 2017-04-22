import pymysql

def db_conf():
	global dbhost
	global dbuser
	global dbpassword
	global dbname

def regex():
	global domain_regex
	domain_regex = '(\/\/)(?:[\w-]+\.)*([\w-]{1,63})(?:\.(?:\w{3}|\w{2}))'
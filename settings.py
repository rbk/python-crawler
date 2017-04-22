import pymysql

def db_conf():
	global dbhost
	global dbuser
	global dbpassword
	global dbname

def db_conn() :
	conn = pymysql.connect(
		host=settings.dbhost,
		user=settings.dbuser,
		password=settings.dbpassword,
		db=settings.dbname,
		charset='utf8mb4',
		cursorclass=pymysql.cursors.DictCursor
	)

import pymysql
import settings

def db_conn() :
	conn = pymysql.connect(
		host=settings.dbhost,
		user=settings.dbuser,
		password=settings.dbpassword,
		db=settings.dbname,
		charset='utf8mb4',
		cursorclass=pymysql.cursors.DictCursor
	)
	return conn
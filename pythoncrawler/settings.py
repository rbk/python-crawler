import pymysql

def db_conf():
	global dbhost
	global dbuser
	global dbpassword
	global dbname

db_conf()
settings.dbhost = 'localhost'
settings.dbuser = 'root'
settings.dbpassword = ''
settings.dbname = 's1'

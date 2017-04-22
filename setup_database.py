
import db_connection
conn = db_connection.db_conn()

print('>>> dropping all tables')
a = conn.cursor()
a.execute('drop table if exists images')
a.execute('drop table if exists link_queue')
a.execute('drop table if exists submissions')

print('>>> creating submissions table')
submission_table = '''CREATE TABLE IF NOT EXISTS submissions (
	`id` int auto_increment primary key,
	`title` varchar(255) not null,
	`url` varchar(255) not null,
	`html` longtext not null,
	`date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)'''

print('>>> creating link_queue table')
link_queue_table = '''
	CREATE TABLE IF NOT EXISTS link_queue (
	`id` int auto_increment,
	`url` varchar(255) not null unique,
	`text` varchar(255),
	`did` int not null,
	`date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY(id),
  FOREIGN KEY(did) REFERENCES submissions(id)
	)'''


print('>>> creating images table')
image_table = '''
	CREATE TABLE IF NOT EXISTS images (
	`id` int auto_increment,
	`url` varchar(255) not null unique,
	`size` varchar(255) not null,
	`alt` varchar(255),
	`did` int not null,
	`date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY(id),
  FOREIGN KEY(did) REFERENCES submissions(id)
	)'''

a.execute(submission_table)
a.execute(link_queue_table)
a.execute(image_table)
print('>>> tables created!')
conn.close()
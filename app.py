from flask import Flask, jsonify
import settings
settings.db_conf()
settings.dbhost = 'localhost'
settings.dbuser = 'root'
settings.dbpassword = 'password'
settings.dbname = 's1'

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

import db_connection
conn = db_connection.db_conn()
a = conn.cursor()

all_submissions = '''
	select *
	from link_queue
'''

a.execute(all_submissions)
results = a.fetchall()


@app.route('/submissions/api/v1.0/sites', methods=['GET'])
def get_sites():
    return jsonify({'sites': results})

if __name__ == '__main__':
    app.run(debug=True)
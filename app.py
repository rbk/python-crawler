from flask import Flask, jsonify
from flask import request
import settings
settings.db_conf()
settings.dbhost = 'localhost'
settings.dbuser = 'root'
settings.dbpassword = 'password'
settings.dbname = 's1'

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <head>
            </head>
            <body>
                <h1>Submit site</h1>
                <form action="/submissions/api/v1.0/add" method="get">
                    <label>URL</label>
                    <input type="text" name="url"/>
                    <button>Submit</button>
                </form>
            </body>
        </html>
    '''

import db_connection
conn = db_connection.db_conn()
a = conn.cursor()

all_submissions = '''
	select *
	from link_queue
'''

a.execute(all_submissions)
results = a.fetchall()


# List all submissions in a tables
@app.route('/submissions/api/v1.0/all', methods=['GET'])
def get_sites():
    return jsonify({'sites': results})

# Call our save submission function
@app.route('/submissions/api/v1.0/add', methods=['GET'])
def add_site():
    return request.args['url']

if __name__ == '__main__':
    app.run(debug=True)
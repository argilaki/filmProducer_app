

# blog.py - controller
# imports
from flask import Flask, render_template, request, session, \
flash, redirect, url_for, g
import sqlite3
# configuration
DATABASE = 'blog.db'
USERNAME = 'abc'
PASSWORD = 'abc'
SECRET_KEY = 'ABC'

app = Flask(__name__,template_folder='templates')
# pulls in configurations by looking for UPPERCASE variables
app.config.from_object(__name__)
# function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    status_code = 200
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
        request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please try again.'
            status_code = 401
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error=error), status_code

@app.route('/main')
def main():
    return render_template('main.html')
if __name__ == '__main__':
    app.run(debug=True)

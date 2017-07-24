from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: the connection string after :// contains the following info:
# user:password@server:portNumber/databaseName

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:lc101@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLALCHEMY(app)
#sets the database

class Blog(db.Model):
	id = db.Column(db.Integer, primary_key=True)
    
	name = db.Column(db.String(120))
	#this column is called Name which is a string that has a max length of 120 characters
	body = db.Column(db.String(120))
	#this column is called Body which is a string that has a max length of 120 characters

	def __init__(self, name, body):
		self.name = name
		self.body = body

if __name__ == '__main__':
    app.run()

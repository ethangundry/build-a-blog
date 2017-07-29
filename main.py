from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: the connection string after :// contains the following info:
# user:password@server:portNumber/databaseName

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:lc101@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
#sets the database

app.secret_key = 'A0Zr98j/2yX R~XHH!jmN]LWX/,?RT'
#sets the secret key


class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(120))
    #this column is called Name which is a string that has a max length of 120 characters
    body = db.Column(db.String(120))
    #this column is called Body which is a string that has a max length of 120 characters   

    def __init__(self, name, body):
        self.name = name
        self.body = body

posts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    posts = Blogpost.query.all()
    return render_template("blog.html", title="Build-A-Blog", posts=posts)

@app.route('/blog')
def blog():
    post_id = request.args.get('id')
    post = Blogpost.query.get(post_id)
    return render_template("blogpost.html", title="Build-A-Blog", post=post)

@app.route('/newpost', methods=['GET', 'POST'])
def newpost():
    #template defaults
    fields = {}
    errors = {}
    has_error = False

    if request.method == 'POST':
        name = request.form['name']
        body = request.form['body']
        fields['name'] = request.form['name']
        fields['body'] = request.form['body']

        #error for title
        if not fields['name']:
            errors['name'] = "You must have a title for your blog post."
            has_error = True

        #error for body
        if not fields['body']:
            errors['body'] = "You must have a body for your blog post."
            has_error = True

        #checks if there's an error or not
        if not has_error:
            #if no error, commits to database
            post = Blogpost(name, body)
            db.session.add(post)
            db.session.commit()
        
            #redirect to index if succesful
            return redirect(url_for("index"))
        else:
            return render_template('newpost.html',title="New Post", fields=fields, errors=errors, has_error=has_error)

    else:
        return render_template('newpost.html',title="New Post", fields=fields, errors=errors, has_error=has_error)


if __name__ == '__main__':
    app.run(debug=True)

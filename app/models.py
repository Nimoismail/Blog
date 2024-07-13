from app import db, app
from datetime import datetime


def slugify(s):
    pass

class Post(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text(2000))
    created = db.Column(db.DateTime, default=datetime.now() )

# constructer

# are used to accept any number of positional and keyword arguments, respectively.
# *args collects any number of positional arguments into a tuple. It allows a function to accept a variable number of arguments.
# **kwargs collects any number of keyword arguments into a dictionary. It allows a function to accept a variable number of keyword arguments.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
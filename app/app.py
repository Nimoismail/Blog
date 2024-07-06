from flask import Flask

from config import config

# This line imports the post blueprint from the posts.blueprint module. 
# A blueprint in Flask is a way to organize your application into smaller and reusable components.
from posts.blueprint import post

app = Flask(__name__)

# This line loads the configuration settings from the config object into the Flask application.
app.config.from_object(config)

# registration
# This line registers the post blueprint with the Flask application.
# The url_prefix argument specifies that all the routes defined in the post blueprint will be prefixed with /blog
# . For example, if the post blueprint has a route /create, it will be accessible at /blog/create.
app.register_blueprint(post, url_prefix="/blog")
# local host 5000 block address
from flask import Blueprint,render_template

# Blueprint Class instance
# post is the name of the variable again

post = Blueprint('post', __name__, template_folder='templates')


@post.route('/')
def post_list():
 return render_template('posts/posts.html')

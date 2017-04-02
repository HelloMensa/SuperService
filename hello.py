from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/url/')
def url():
    return url_for('user', username='abbc')

@app.route('/about')
def about():
    return 'The about page'



if __name__ == '__main__':
    app.run() #port=8888,host='0.0.0.0'


#def application(env, start_response):
#    import pdb; pdb.set_trace()
#    start_response('200 OK', [('Content-Type','text/html')])
#    return "Hello World"
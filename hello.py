from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run() #port=8888,host='0.0.0.0'


#def application(env, start_response):
#    import pdb; pdb.set_trace()
#    start_response('200 OK', [('Content-Type','text/html')])
#    return "Hello World"
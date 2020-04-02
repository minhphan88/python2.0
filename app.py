from flask import Flask

app = Flask(__name__)

def my_function():
    print("Hello from a function")

@app.route('/')
def index():
    return 'Index Page'

@app.route('/page')
def page():
    return 'This is an different page'

@app.route('/cal')
def cal():
    return my_function

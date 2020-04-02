import re
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

def my_function():
    print("Hello from a function")

@app.route('/')
def index():
    return 'Index Page'

@app.route('/page')
def page():
    return 'This is an different page'

@app.route('/cal', methods= methods=['POST'])
def cal(height):
    try:
        height=json.loads(heightdata.body)
        weight=str(height*10)
        return weight
    except ValueError as e:
        return 0


if __name__ == '__main__':
    app.run(debug=True)

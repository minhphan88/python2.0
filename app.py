from flask import Flask, jsonify, render_template, request

app = Flask(__name__)



@app.route('/')
def index():
    return 'Index Page'

@app.route('/page')
def page():
    return 'This is an different page'


if __name__ == '__main__':
    app.run(debug=True)

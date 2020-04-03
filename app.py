from flask import Flask, jsonify, render_template, request

app = Flask(__name__)



@app.route('/')
def index():
    return 'Index Page'

@app.route('/page')
def page():
    return 'This is an different page'

@app.route('/query_example'):
def query_example():
    language=request.args.get('language')
    return '<h1> The language is : {}</h1>'.format (language)




if __name__ == '__main__':
    app.run(debug=True)

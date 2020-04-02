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
    a = request.args.get('number1', '0')
    operator = request.args.get('operator', '+')
    b = request.args.get('number2', '0')
    # validate the input data
    m = re.match(r'^\-?\d*[.]?\d*$', a)
    n = re.match(r'^\-?\d*[.]?\d*$', b)

    if m is None or n is None or operator not in '+-*/':
        return jsonify(result='Error!')

    if operator == '/':
        result = eval(a + operator + str(float(b)))
    else:
        result = eval(a + operator + b)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)

#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'<h1>{parameter}</h1>'

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(num) for num in range(1, parameter + 1))
    return f'<h1>Numbers from 1 to {parameter}</h1><pre>{numbers}</pre>'

@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1,operation,num2):
    result = None
    if operation =='+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1/num2
        else:
            return '<h1>Error: Division by zero?</h1>'
    elif operation == '%':
        result = num1 % num2

    if result is not None:
        return f'<h1>Result: {result}</h1>'
    else:
        return '<h1>Error: Invalid Operation</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)


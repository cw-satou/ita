from flask import request, render_template

from calcdiv import app
from .model import calc_divide

@app.route('/')
def input():
    return render_template('calc-input.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    number1 = int(request.form.get("num1"))
    number2 = int(request.form.get("num2"))
    
    result = number1 / number2

    return render_template('calc-result.html', result=result)

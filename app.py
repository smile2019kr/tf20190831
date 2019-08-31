from flask import Flask
from flask import render_template, request, jsonify #flask에서 사용할 것들을 등록
import re
from calculator.controller import CalculatorController
#model은 controller에서 호출하는 것이고 app.py에서는 controller를 호출

from cabbage.controller import CabbageController


app = Flask(__name__)

@app.route("/move/<path>") # 페이지 이동 설정 <path>에 해당하는 화면으로 이동하라는 것. "/move/ui_calc" -> ui_calc로 이동
def move(path):
    return render_template('{}.html'.format(path))

@app.route('/ui_calc')
def ui_calc():
    stmt = request.args.get('stmt','NONE')
    if(stmt == 'NONE'):
        print('넘어온 값이 없음')
    else:
        print('넘어온 식: {}'.format(stmt))
        patt = '[0-9]+'
        op = re.sub(patt,'',stmt)
        print('넘어온 연산자: {}'.format(op))
        nums = stmt.split(op)
        result = 0
        n1 = int(nums[0])
        n2 = int(nums[1])
        if op == '+': result = n1 + n2
        elif op == '-': result = n1 - n2
        elif op == '*': result = n1 * n2
        elif op == '/': result = n1 / n2

    return jsonify(result = result) #연산결과를 result에 담겠다는 약속표기. ui_calc.html 114행, 115행

@app.route('/ai_calc', methods=["POST"])
#'', "" 상관없음. ai_calc.html 의 <form action="/ai_calc"></form> 과 이동경로를 일치시키는것
def ai_calc():
    num1 = request.form['num1']
    num2 = request.form['num2']
    opcode = request.form['opcode']
    c = CalculatorController(num1, num2, opcode)
    result = c.calc()
    render_params = {}
    render_params['result'] = int(result)
   # print('app.py 에 출력된 덧셈결과: {}'.result)
    return render_template('ai_calc.html', **render_params)


@app.route("/cabbage")
def cabbage():
#avg_temp min_temp max_temp rain_fall
    avg_temp = request.form['avg_temp']
    min_temp = request.form['min_temp']
    max_temp = request.form['max_temp']
    avg_temp = request.form['avg_temp']

@app.route("/")
def index():
    return render_template('index.html') #index.html을 긁어오는 구문 render_template

if __name__ == '__main__':
    app.debug = True
    app.run()


from flask import Flask, render_template, request, redirect, session, jsonify
import sys

app = Flask(__name__)

app.config['SECRET_KEY'] = '1145141919810'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/runcode', methods=['POST'])
def runcode():
    code = request.form.get('code')  # 获取前端提交的代码值
    try:
        output = sys.stdout
        f = open('test.txt','w',encoding='utf-8')
        sys.stdout = f
        exec(code)
    except Exception as e:
        result = str(e)
    f.close()
    sys.stdout = output
    with open('test.txt','r',encoding='utf-8') as f:
        result = f.read()
        f.close()

    response = {
        'result': result,
    }

    return jsonify(response)

app.run()
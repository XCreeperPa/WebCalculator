import json

from flask import Flask, request, jsonify, render_template

import CalculatorSupport

# 使用 Flask 创建一个简单的 Web 服务器
app = Flask(__name__)


@app.route('/')
def updated_index():
    # 使用 Flask 的 render_template 函数从 "calculator.html" 文件中加载 HTML 内容
    return render_template('commented_calculator_chinese.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    # 从请求中获取用户输入的表达式
    expression = request.form.get('expression')
    try:
        # 使用后端 API 计算结果
        io = CalculatorSupport.log.create_string_io()  # 创建io对象
        result = CalculatorSupport.calc_main(expression)  # 使用后端 API 计算结果
        io.seek(0)
        log = io.read()  # 获取日志结果

        # 返回计算的结果
        return jsonify(success=True, result=str({"result": result, "log": log}))
    except Exception as e:
        # 如果出现错误，返回错误信息
        return jsonify(success=False, error=str(e))


@app.route('/')
def index():
    # 尝试读取 bg.json 文件
    try:
        with open('bg.json', 'r') as file:
            data = json.load(file)
            bg_url = data.get('url', '')  # 获取URL，如果不存在，则默认为空字符串
            print(bg_url)
    except (FileNotFoundError, json.JSONDecodeError):
        bg_url = ''  # 如果文件不存在或存在JSON错误，则默认没有背景

    # 将背景URL传递给HTML模板
    return render_template('commented_calculator_chinese.html', bg_url=bg_url)


# 启动 Flask 应用
if __name__ == "__main__":
    app.run(debug=True)

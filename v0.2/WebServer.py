from flask import Flask, request, jsonify, render_template
# 使用 interpreter 的功能来计算结果
from module import Expression

# 使用 Flask 创建一个简单的 Web 服务器
app = Flask(__name__)


@app.route('/')
def updated_index():
    # 使用 Flask 的 render_template 函数从 "calculator.html" 文件中加载 HTML 内容
    return render_template('calculator.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    # 从请求中获取用户输入的表达式
    expression = request.form.get('expression')
    try:
        # 使用后端 API 计算结果
        result = Expression.calculate(expression)
        # 返回计算的结果
        return jsonify(success=True, result=str(result))
    except Exception as e:
        # 如果出现错误，返回错误信息
        return jsonify(success=False, error=str(e))


# 启动 Flask 应用
if __name__ == "__main__":
    app.run(debug=True)

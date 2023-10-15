from flask import Flask, request, jsonify, render_template
import os
import CalculatorSupport
import json

# 使用 Flask 创建一个简单的 Web  服务器
app = Flask(__name__)
CalculatorSupport.CalcType.set_calc_type(CalculatorSupport.CalcType.Fraction)


@app.route('/')
def updated_index():
    # 使用 Flask 的 render_template 函数从 "calculator.html" 文件中加载 HTML 内容
    return render_template('calculator.html')


@app.route('/calculator')
def updated_calculator():
    # 使用 Flask 的 render_template 函数从 "calculator.html" 文件中加载 HTML 内容
    return render_template('calculator.html')


@app.route('/user-manual')
def updated_UserManual():
    # 使用 Flask 的 render_template 函数从 "user-manual.html" 文件中加载 HTML 内容
    return render_template('user-manual.html')


@app.route('/documentation')
def updated_documentation():
    # 使用 Flask 的 render_template 函数从 "documentation.html" 文件中加载 HTML 内容
    return render_template('documentation.html')


@app.route('/about')
def updated_about():
    # 使用 Flask 的 render_template 函数从 "documentation.html" 文件中加载 HTML 内容
    return render_template('about.html')


@app.route('/settings')
def updated_settings():
    # 使用 Flask 的 render_template 函数从 "documentation.html" 文件中加载 HTML 内容
    return render_template('settings.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/get-docs')
def get_docs():
    docs_dir = os.path.join(app.static_folder, "documentation")
    all_files = [f for f in os.listdir(docs_dir) if f.endswith('.html')]

    # 将index.html移动到列表的第一个位置
    if "index.html" in all_files:
        all_files.remove("index.html")
        all_files.insert(0, "index.html")

    return jsonify(all_files)


@app.route('/get-user-manual')
def get_UserManual():
    docs_dir = os.path.join(app.static_folder, "user-manual")
    all_files = [f for f in os.listdir(docs_dir) if f.endswith('.html')]

    # 将index.html移动到列表的第一个位置
    if "index.html" in all_files:
        all_files.remove("index.html")
        all_files.insert(0, "index.html")

    return jsonify(all_files)


@app.route('/calculator', methods=['POST'])
def calculate():
    # 从请求中获取用户输入的表达式
    expression = request.form.get('expression')
    try:
        # 使用后端 API 计算结果
        io = CalculatorSupport.log.create_string_io()  # 创建io对象
        result = CalculatorSupport.calc_main(expression)  # 使用后端 API 计算结果
        io.seek(0)
        log = io.read()  # 获取日志结果
        data = {
            "result": str(result),
            "log": log
        }
        json_string = json.dumps(data)

        # 返回计算的结果
        return jsonify(success=True, result=json_string)
    except Exception as e:
        # 如果出现错误，返回错误信息
        return jsonify(success=False, error=str(e))


# 启动 Flask 应用
if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True)

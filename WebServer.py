# 本文件是云计算器的一部分。
#
# 云计算器是自由软件：你可以再分发之和/或依照由自由软件基金会发布的 GNU 通用公共许可证修改之，无论是版本 3 许可证，还是（按你的决定）任何以后版都可以。
#
# 发布云计算器是希望它能有用，但是并无保障;甚至连可销售和符合某个特定的目的都不保证。请参看 GNU 通用公共许可证，了解详情。
#
# 你应该随程序获得一份 GNU 通用公共许可证的复本。如果没有，请看 <https://www.gnu.org/licenses/>.
#
# This file is part of WebCalculator.
#
# WebCalculator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# WebCalculator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with WebCalculator. If not, see <https://www.gnu.org/licenses/>.

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


@app.route('/get_license')
def get_license():
    # 拼接静态文件的绝对路径，使用 Flask 应用程序的 root_path 属性
    static_file_path = app.root_path + '/static/LICENSE'

    try:
        # 打开并读取静态文件内容
        with open(static_file_path, 'r') as file:
            license_text = file.read()
        return license_text
    except FileNotFoundError:
        return "文件未找到"
    except Exception as e:
        return str(e)

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

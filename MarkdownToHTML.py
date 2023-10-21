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
import mistune
import os

if __name__ == '__main__':
    # 遍历目录
    for root, dirs, files in os.walk(r"UserManual"):
        for file in files:
            # 检查文件是否为.md文件
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                # 读取.md文件的内容
                with open(file_path, 'r', encoding='utf-8') as md_file:
                    md_content = md_file.read()
                    with open(file=r"static\user-manual\\"+file+".html", mode="w", encoding="utf8") as html_file:
                        html_content = mistune.markdown(md_content)
                        html_file.write(html_content)
                        print(html_file)

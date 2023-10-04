import mistune
import os

if __name__ == '__main__':
    # 遍历目录
    for root, dirs, files in os.walk(r"Documentation"):
        for file in files:
            # 检查文件是否为.md文件
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                # 读取.md文件的内容
                with open(file_path, 'r', encoding='utf-8') as md_file:
                    md_content = md_file.read()
                    with open(file=r"static\documentation\\"+file+".html", mode="w", encoding="utf8") as html_file:
                        html_content = mistune.markdown(md_content)
                        html_file.write(html_content)
                        print(html_file)

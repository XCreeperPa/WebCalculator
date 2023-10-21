# 云计算器

## 一、简介

云计算器是一个基于Python Flask的互联网计算器服务，旨在为用户提供更便捷、强大的计算器服务。云计算器利用云服务的优势，允许用户随时随地访问，无需安装和部署。它支持多端互联，数据互通，以提高效率和用户体验。
![WebCalculator.png](https://github.com/XCreeperPa/WebCalculator/raw/main/README_image/WebCalculator.png)

## 二、基本用法

1. 在浏览器输入服务器的URL（端口号默认5000），下文以http://127.0.0.1:5000为例。
![openWebPage.jpg](https://github.com/XCreeperPa/WebCalculator/raw/main/README_image/openWebPage.jpg)
2. 按下回车进入对应页面。
![mainPage.jpg](https://github.com/XCreeperPa/WebCalculator/raw/main/README_image/mainPage.jpg)
3. 在输入框中键入表达式，按下回车开始计算
![Calculate.jpg](https://github.com/XCreeperPa/WebCalculator/raw/main/README_image/Calculate.jpg)

更多用法详见用户手册和技术文档。

## 三、服务端部署

### 3.1使用可执行文件部署

1. 下载并解压WebCalculator v1.1 WindowsEXE.zip（或者其更新版本）
2. 双击运行startServer.exe

### 3.2使用源代码部署

#### 3.2.1环境和依赖

为了成功部署云计算器，请按照以下步骤配置您的环境和依赖：

1. **Python环境：** 云计算器基于Python 3.11编写。请确保您的Python环境与Python 3.11兼容。

   - **版本检查：** 您可以通过在终端中运行以下命令来检查您的Python版本：

     ```bash
     python --version
     ```

     确保输出显示的Python版本号为3.11或更高。如果您的Python版本不是3.11，请升级到兼容版本。

   - **虚拟环境（可选）：** 为了更好地隔离项目的Python依赖，您可以考虑在项目目录中创建一个虚拟环境。虚拟环境可以帮助您管理项目所需的依赖，而不会影响全局Python环境。

     创建虚拟环境的示例步骤（使用`venv`模块）：

     ```bash
     # 在项目目录中创建虚拟环境（如果不存在）
     python -m venv venv

     # 激活虚拟环境（Windows）
     venv\Scripts\activate

     # 激活虚拟环境（macOS和Linux）
     source venv/bin/activate
     ```

     请注意，虚拟环境的使用是可选的，但强烈建议，以避免与全局Python环境的冲突。

   - **依赖安装：** 一旦Python环境兼容，您可以使用以下命令安装项目所需的依赖：

     ```bash
     pip install -r requirements.txt
     ```


2. **Python依赖库：** 云计算器依赖于Flask。您可以使用以下命令来安装Flask：

   ```bash
   pip install Flask
   ```

   确保您已正确安装并配置Flask。

#### 3.2.2获取源代码

要获取云计算器的源代码，请使用Git工具，按照以下步骤进行：

1. 打开终端：
   - **Windows:** 打开"命令提示符"或使用Windows PowerShell。
   - **macOS和Linux:** 打开终端应用。

2. 切换到您希望保存源代码的目录。例如，要将源代码保存在您的主文件夹中，请运行以下命令：

   ```bash
   cd ~
   ```

3. 运行以下命令以克隆项目存储库：

   ```bash
   git clone https://github.com/XCreeperPa/WebCalculator.git
   ```

   或

   ```bash
   git clone https://gitee.com/xcpcn/WebCalculator.git
   ```

#### 3.2.3启动服务端

一旦您成功获取了源代码，您可以启动服务端。不同操作系统下有不同的方法：

- **Windows:**
   1. 打开"命令提示符"或"Windows PowerShell"。
   2. 使用`cd`命令切换到源代码根目录。
   3. 运行以下命令：`python WebServer.py`

- **macOS和Linux:**
   1. 打开终端。
   2. 使用`cd`命令切换到源代码根目录。
   3. 运行以下命令：`python WebServer.py`

## 四、贡献者

感谢以下贡献者为项目的发展做出了贡献：

- XCreeperPa：前端开发、Web服务器开发、架构设计
- Noob_0：算法设计、架构设计

## 五、许可证

本项目使用GPLv3许可证。有关详细信息，请参阅LICENSE文件。

## 六、联系我们

如有任何问题或建议，欢迎联系我们：

- 云计算器官方Github仓库：[https://github.com/XCreeperPa/WebCalculator](https://github.com/XCreeperPa/WebCalculator)
- 云计算器官方Gitee仓库：[https://gitee.com/xcpcn/WebCalculator](https://gitee.com/xcpcn/WebCalculator)

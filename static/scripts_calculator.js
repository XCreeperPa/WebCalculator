// 本文件是云计算器的一部分。

// 云计算器是自由软件：你可以再分发之和/或依照由自由软件基金会发布的 GNU 通用公共许可证修改之，无论是版本 3 许可证，还是（按你的决定）任何以后版都可以。

// 发布云计算器是希望它能有用，但是并无保障;甚至连可销售和符合某个特定的目的都不保证。请参看 GNU 通用公共许可证，了解详情。

// 你应该随程序获得一份 GNU 通用公共许可证的复本。如果没有，请看 <https://www.gnu.org/licenses/>.

// This file is part of WebCalculator.

// WebCalculator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

// WebCalculator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

// You should have received a copy of the GNU General Public License along with WebCalculator. If not, see <https://www.gnu.org/licenses/>.

version  = "1.1.0"

function getCurrentDateTimeString() {
    // 创建一个 Date 对象，它将包含当前日期和时间
    var currentDate = new Date();

    // 使用 Date 对象的方法获取年、月、日、小时、分钟、秒
    var year = currentDate.getFullYear();
    var month = currentDate.getMonth() + 1; // 月份从0开始，所以需要加1
    var day = currentDate.getDate();
    var hours = currentDate.getHours();
    var minutes = currentDate.getMinutes();
    var seconds = currentDate.getSeconds();

    // 构建日期和时间的字符串
    var dateTimeString = year + "-" + padZero(month) + "-" + padZero(day) + " " + padZero(hours) + ":" + padZero(minutes) + ":" + padZero(seconds);

    // 返回日期和时间字符串
    return dateTimeString;

    // 辅助函数：在数字小于10时补零
    function padZero(number) {
        return (number < 10 ? "0" : "") + number;
    }
}



function addCard(data) {
    var expression = document.querySelector('input[name="expression"]').value;
    var data_json = JSON.parse(data); // 解析 JSON 字符串

    // 创建新的card-container
    const newCardContainer = document.createElement('div');
    newCardContainer.className = 'card-container';

    // 创建新的card元素和其子元素
    const newCard = document.createElement('div');
    newCard.className = 'card';

    const faceExpression = document.createElement('pre');
    faceExpression.innerText = "表达式: " + expression;

    const faceResult = document.createElement('pre');
    faceResult.innerText = "结果: " + data_json.result;

    const backLogContent = document.createElement('pre');
    backLogContent.className = 'log-content';
    backLogContent.style.display = 'inline';  // 设置初始显示值
    backLogContent.innerText = '日志:' + "\n" + data_json.log;

    newCard.appendChild(faceExpression);
    newCard.appendChild(faceResult);
    newCard.appendChild(backLogContent);

    newCardContainer.appendChild(newCard); // 添加card到card-container
    backLogContent.style.display = 'none';


    // 双击 newCardContainer 以切换日志的可见性
    newCardContainer.addEventListener("dblclick", function() {
        const logContentSpan = this.querySelector('.log-content');
        if (logContentSpan.style.display === 'none' || !logContentSpan.style.display) {
            logContentSpan.style.display = 'inline';
        } else {
            logContentSpan.style.display = 'none';
        }
    });

    const container = document.querySelector('.container#cards');
    container.insertBefore(newCardContainer, container.firstChild); // 添加newCardContainer到container所有元素的前面
}

// 当表单被提交时执行以下函数
document.getElementById('calculatorForm').addEventListener('submit', function(e) {
    // 阻止表单的默认提交行为
    e.preventDefault();

    // 获取用户输入的表达式
    let expression = e.target.elements.expression.value;

    // 使用 Fetch API 异步发送 POST 请求到服务器
    fetch('/calculator', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'expression=' + encodeURIComponent(expression)
    })
    .then(response => response.json())  // 解析服务器返回的JSON数据
    .then(data => {
        // 如果成功，使用addCard函数显示结果
        if (data.success) {
            addCard(data.result);
        } else {
            alert('计算错误: ' + data.error);
        }
    });
});

document.getElementById("documentationButton").addEventListener("click", function() {
    window.location.href = "/documentation"; // 替换为你的目标URL
});

document.getElementById("userManualButton").addEventListener("click", function() {
    window.location.href = "/user-manual"; // 替换为你的目标URL
});

document.getElementById("aboutButton").addEventListener("click", function() {
    window.location.href = "/about"; // 替换为你的目标URL
});

document.getElementById("settingsButton").addEventListener("click", function() {
    window.location.href = "/settings"; // 替换为你的目标URL
});

document.getElementById("clearButton").addEventListener("click", function() {
    const cardContainer = document.getElementById('cards');
    cardContainer.innerHTML = '';});

document.getElementById("goToTopButton").addEventListener("click", function() {
    const cardContainer = document.getElementById('cards');
    cardContainer.scrollTop = 0;})

document.getElementById("downloadButton").addEventListener("click", function() {
    // 调用函数并获取当前日期和时间字符串
    var currentDateTime = getCurrentDateTimeString();

    // 获取 ID 为 "cards" 的容器
    var cardsContainer = document.getElementById("cards");

    // 获取所有 class 为 "card" 的元素
    var cardElements = cardsContainer.getElementsByClassName("card");

    var textToDownload = ("云计算器计算日志" + "\n"
                                + "生成日期：" + currentDateTime + "\n"
                                + "版本：" + version + "\n");

    // 遍历所有 "card" 元素并获取其内的所有 <p> 元素的内容
    for (var i = 0; i < cardElements.length; i++) {
        var card = cardElements[i];
        var paragraphElements = card.getElementsByTagName("pre");
        textToDownload +=  "\n" + "卡片 " + (i + 1) + " 的内容：" + "\n";
        console.log(paragraphElements)

        // 遍历 <p> 元素并添加其内容到文本
        for (var j = 0; j < paragraphElements.length; j++) {
            var paragraph = paragraphElements[j];
            var content = paragraph.innerHTML.replace(/<br\s*[/]?>/gi, "\n"); // 使用replace方法将<br>替换为\n
            textToDownload += content + "\n"
            console.log(content)
        }
    }

    // 创建一个Blob对象
    var blob = new Blob([textToDownload], { type: "text/plain" });

    // 创建一个下载链接
    var downloadLink = document.createElement("a");
    downloadLink.href = window.URL.createObjectURL(blob);
    downloadLink.download = "计算结果" + currentDateTime + ".txt"; // 设置下载文件的名称

    // 模拟点击下载链接
    downloadLink.click();
});

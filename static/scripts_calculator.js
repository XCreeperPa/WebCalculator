// 本文件是云计算器的一部分。

// 云计算器是自由软件：你可以再分发之和/或依照由自由软件基金会发布的 GNU 通用公共许可证修改之，无论是版本 3 许可证，还是（按你的决定）任何以后版都可以。

// 发布云计算器是希望它能有用，但是并无保障;甚至连可销售和符合某个特定的目的都不保证。请参看 GNU 通用公共许可证，了解详情。

// 你应该随程序获得一份 GNU 通用公共许可证的复本。如果没有，请看 <https://www.gnu.org/licenses/>.

// This file is part of WebCalculator.

// WebCalculator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

// WebCalculator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

// You should have received a copy of the GNU General Public License along with WebCalculator. If not, see <https://www.gnu.org/licenses/>.
function addCard(data) {
    console.log("test");
    var expression = document.querySelector('input[name="expression"]').value;
    var data_json = JSON.parse(data); // 解析 JSON 字符串

    // 创建新的card-container
    const newCardContainer = document.createElement('div');
    newCardContainer.className = 'card-container';

    // 创建新的card元素和其子元素
    const newCard = document.createElement('div');
    newCard.className = 'card';

    const faceExpression = document.createElement('p');
    faceExpression.innerText = "表达式: " + expression;

    const faceResult = document.createElement('p');
    faceResult.innerText = "结果: " + data_json.result;

    const backLogLabel = document.createElement('span');
    backLogLabel.innerText = '日志:';

    const backLogContent = document.createElement('span');
    backLogContent.className = 'log-content';
    backLogContent.style.display = 'inline';  // 设置初始显示值
    backLogContent.innerText = "\n" + data_json.log;

    const backLog = document.createElement('p');
    backLog.appendChild(backLogLabel);
    backLog.appendChild(backLogContent);

    newCard.appendChild(faceExpression);
    newCard.appendChild(faceResult);
    newCard.appendChild(backLog);

    newCardContainer.appendChild(newCard); // 添加card到card-container

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

document.getElementById("downloadButton").addEventListener("click", function() {
    window.location.href = "/404"; // 替换为你的目标URL
});

document.getElementById("clearButton").addEventListener("click", function() {
    const cardContainer = document.getElementById('cards');
    cardContainer.innerHTML = '';});

document.getElementById("goToTopButton").addEventListener("click", function() {
    const cardContainer = document.getElementById('cards');
    cardContainer.scrollTop = 0;})

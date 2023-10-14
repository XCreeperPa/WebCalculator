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
    fetch('/calculate', {
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
    window.location.href = "http://127.0.0.1:5000/documentation"; // 替换为你的目标URL
});

document.getElementById("userManualButton").addEventListener("click", function() {
    window.location.href = "http://127.0.0.1:5000/user-manual"; // 替换为你的目标URL
});
document.getElementById("clearButton").addEventListener("click", function() {
    const cardContainer = document.getElementById('cards');
    cardContainer.innerHTML = '';});

document.getElementById("goToTopButton").addEventListener("click", function() {
    const cardContainer = document.getElementById('cards');
    cardContainer.scrollTop = 0;})

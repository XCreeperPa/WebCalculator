window.onload = function() {
    const documentSelector = document.getElementById("documentSelector");
    const documentContainer = document.getElementById("documentContainer");

    function loadDocument(docName) {
        fetch('/static/documentation/' + docName)
            .then(response => response.text())
            .then(data => {
                documentContainer.innerHTML = data;
            });
    }

    // 动态获取并更新选择框
    fetch('/get-docs')
        .then(response => response.json())
        .then(data => {
            data.forEach(doc => {
                const option = document.createElement('option');
                option.value = doc;
                option.textContent = doc.replace('.html', '');  // 显示文件名，不包含扩展名
                documentSelector.appendChild(option);
            });
        });

    documentSelector.addEventListener('change', function() {
        loadDocument(this.value);
    });

    // 默认加载第一个文档
    setTimeout(() => {
        if (documentSelector.options.length > 0) {
            loadDocument(documentSelector.options[0].value);
        }
    }, 500);
}

document.getElementById("goToHomePageButton").addEventListener("click", function() {
    window.location.href = "http://127.0.0.1:5000/calculator"; // 替换为你的目标URL
});

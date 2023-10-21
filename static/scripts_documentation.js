// 本文件是云计算器的一部分。

// 云计算器是自由软件：你可以再分发之和/或依照由自由软件基金会发布的 GNU 通用公共许可证修改之，无论是版本 3 许可证，还是（按你的决定）任何以后版都可以。

// 发布云计算器是希望它能有用，但是并无保障;甚至连可销售和符合某个特定的目的都不保证。请参看 GNU 通用公共许可证，了解详情。

// 你应该随程序获得一份 GNU 通用公共许可证的复本。如果没有，请看 <https://www.gnu.org/licenses/>.

// This file is part of WebCalculator.

// WebCalculator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

// WebCalculator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

// You should have received a copy of the GNU General Public License along with WebCalculator. If not, see <https://www.gnu.org/licenses/>.
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
    window.location.href = "/calculator"; // 替换为你的目标URL
});

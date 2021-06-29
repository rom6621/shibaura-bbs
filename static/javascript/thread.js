var socket = io.connect();

// 投稿ボタンが押された時の処理
const writeBtn = document.getElementById('writeBtn');
const inputField = document.getElementById('inputField');
const threadId = Number(window.location.search.substring(1).split('&')[0].split('=')[1])

var entries = document.getElementById('entries');
entries.scrollTop = entries.scrollHeight;

writeBtn.addEventListener('click', function(event) {
    if(inputField.value === '') alert('入力されていません');
    else {
        if(confirm("書き込みますか?")) {
            socket.emit('write board', {threadId: threadId, content: inputField.value});
            inputField.value = '';    
        }    
    }
})

socket.on('add entry', function(event) {
    if(threadId === event['threadId']) {
        var entryAuthor = event['entryAuthor'];
        var entryContent = event['entryContent'];
        var entries = document.getElementById('entries');
        var div = document.createElement('div');
        div.id = "entry";
        div.classList.add('rounded', 'bg-light', 'me-3');
        div.innerHTML = `<p class="px-3 pt-3">${entryAuthor}</p>
        <p class="px-3 pb-3">${entryContent}</p>`
        entries.appendChild(div);
        entries.scrollTop = entries.scrollHeight;
    }
})
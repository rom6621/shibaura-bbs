var socket = io.connect();

// 投稿ボタンが押された時の処理
const writeBtn = document.getElementById('writeBtn');
const deleteBtn = document.getElementById('deleteBtn');
const inputField = document.getElementById('inputField');
const threadId = Number(window.location.search.substring(1).split('&')[0].split('=')[1])
const inputLength1 = document.getElementById('inputLength1');
const userId = document.getElementById('userId').innerText;

var entries = document.getElementById('entries');
entries.scrollTop = entries.scrollHeight;

writeBtn.addEventListener('click', function(event) {
    if(inputField.value.length === 0 ) alert('入力されていません');
    else if(inputField.value.length > 128 ) alert('文字数オーバーです');
    else {
        if(confirm("書き込みますか?")) {
            socket.emit('write board', {threadId: threadId, content: inputField.value});
            inputField.value = '';
            inputLength1.innerText = "000/128"
        }
    }
})

function deleteEntry(event){
    if(confirm("削除しますか?")) {
        socket.emit('delete entry', {threadId: threadId, entryId: event.value});
        document.getElementById("contents-" + String(event.value)).innerText = "削除されました";
    }
}

function showLength() {
   inputLength1.innerText =("00" + String(inputField.value.length)).slice(-3) + "/128";
   if(inputField.value.length > 128){
    inputLength1.style.color = "red";
   } else if(inputField.value.length <= 128){
    inputLength1.style.color = "#0b4e3c";
   }
}

socket.on('add entry', function(event) {
    if(threadId === event['threadId']) {
        if(document.getElementById('noEntry') !== null) {
            document.getElementById('noEntry').remove();
        }
        var entryAuthor = event['entryAuthor'];
        var entryContent = event['entryContent'];
        var authorId = event['authorId'];
        var entryId = event['entryId'];
        var entries = document.getElementById('entries');
        var div = document.createElement('div');
        div.id = "entry";
        if(authorId === userId) {
            div.classList.add('rounded', 'bg-warning', 'me-3');
            div.innerHTML = `<div class="float-end"><button class="btn btn-danger" id="deleteBtn" value="${entryId}" onclick="deleteEntry(this)">削除</button></div>
            <p class="px-3 pt-3" id="author-${entryId}">${entryAuthor}</p>
            <p class="px-3 pb-3" id="contents-${entryId}">${entryContent}</p>`    
        } else {
            div.classList.add('rounded', 'bg-light', 'me-3');
            div.innerHTML = `<p class="px-3 pt-3" id="author-${entryId}">${entryAuthor}</p>
            <p class="px-3 pb-3" id="contents-${entryId}">${entryContent}</p>`    
        }
        entries.appendChild(div);
        entries.scrollTop = entries.scrollHeight;
    }
})

socket.on('update entry', function(event) {
    if(threadId === event['threadId']) {
        document.getElementById("contents-" + String(event['entryId'])).innerText = "削除されました";
    }
})
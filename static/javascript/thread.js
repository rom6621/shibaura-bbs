var socket = io.connect();

// 投稿ボタンが押された時の処理
const writeBtn = document.getElementById('writeBtn');
const inputField = document.getElementById('inputField');
const threadId = Number(window.location.search.substring(1).split('&')[0].split('=')[1])
const inputLength1 = document.getElementById('inputLength1');

var entries = document.getElementById('entries');
entries.scrollTop = entries.scrollHeight;

writeBtn.addEventListener('click', function(event) {
    if(inputField.value.length === 0 ) alert('入力されていません');
    else if(inputField.value.length > 128 ) alert('文字数オーバーです');
    else {
        if(confirm("書き込みますか?")) {
            socket.emit('write board', {threadId: threadId, content: inputField.value});
            console.log(("test"));
            alert("a")
            inputField.value = '';
        }
    }
})

function ShowLength() {
   inputLength1.innerText =("00" + String(inputField.value.length)).slice(-3) + "/128";
   if(inputField.value.length > 128){
       inputLength1.style.color = "red";
   }
   else if(inputField.value.length <= 128){
    inputLength1.style.color = "black";
   }
}

socket.on('add entry', function(event) {
    if(threadId === event['threadId']) {
        if(document.getElementById('noEntry') !== null) {
            document.getElementById('noEntry').remove();
        }
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


const submit = document.getElementById('submit');
const nameField = document.getElementById('nameField');
const detailField = document.getElementById('detailField');

function checkThread() {
    if(nameField.value.length === 0 ){ 
        alert('スレッド名が入力されていません'); 
        return false;
    }
    else if(nameField.value.length > 128 ){
        alert('スレッド名が文字数オーバーです');
        return false;
    }
    if(detailField.value.length === 0 ){ 
        alert('スレッド内容が入力されていません');
        return false;
    }
    else if(detailField.value.length > 1024 ){ 
        alert('スレッド内容が文字数オーバーです');
        return false;
    }  
}
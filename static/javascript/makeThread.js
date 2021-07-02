
const submit = document.getElementById('submit');
const nameField = document.getElementById('nameField');
const detailField = document.getElementById('detailField');
const inputThreadLength1 = document.getElementById('inputThreadLength1');
const inputThreadLength2 = document.getElementById('inputThreadLength2');

function checkThread() {
    let submitFlg = true;
    if(nameField.value.length === 0 ){ 
        alert('スレッド名が入力されていません'); 
        submitFlg = false;
    }
    else if(nameField.value.length > 128 ){
        alert('スレッド名が文字数オーバーです');
        submitFlg = false;
    }
    if(detailField.value.length === 0 ){ 
        alert('スレッド内容が入力されていません');
        submitFlg =  false;
    }
    else if(detailField.value.length > 1024 ){ 
        alert('スレッド内容が文字数オーバーです');
        submitFlg = false;
    } 
    return submitFlg; 
}
function showLength1() {
    inputThreadLength1.innerText =("00" + String(nameField.value.length)).slice(-3) + "/128";
    if(nameField.value.length > 128){
        inputThreadLength1.style.color = "red";
    }
    else if(nameField.value.length <= 128){
     inputThreadLength1.style.color = "black";
    }
 }
 function showLength2() {
    inputThreadLength2.innerText =("000" + String(detailField.value.length)).slice(-4) + "/1024";
    if(detailField.value.length > 1024){
        inputThreadLength2.style.color = "red";
    }
    else if(detailField.value.length <= 1024){
     inputThreadLength2.style.color = "black";
    }
 }
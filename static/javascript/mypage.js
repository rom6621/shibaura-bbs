const inputNameLength = document.getElementById('inputNameLength');
const userName = document.getElementById('userName');
const nameBtn = document.getElementById('nameBtn');

function checkName() {
    let submitFlg = true;
    if(userName.value.length === 0 ){ 
        alert('名前が入力されていません'); 
        submitFlg = false;
    }
    else if(userName.value.length > 10 ){
        alert('入力欄が文字数オーバーです');
        submitFlg = false;
    }
    return submitFlg; 
}
function showLength4() {
    inputNameLength.innerText =("0" + String(userName.value.length)).slice(-2) + "/10";
    if(userName.value.length > 10){
        inputNameLength.style.color = "red";
    } else if(userName.value.length <= 10){
     inputNameLength.style.color = "#0b4e3c";
    }
 }
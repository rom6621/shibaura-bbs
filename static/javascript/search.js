
const inputSearchLength = document.getElementById('inputSearchLength');
const searchInput = document.getElementById('searchInput');
const searchBtn = document.getElementById('searchBtn');

function checkSearch() {
    let submitFlg = true;
    if(searchInput.value.length === 0 ){ 
        alert('検索語句が入力されていません'); 
        submitFlg = false;
    }
    else if(searchInput.value.length > 128 ){
        alert('検索欄が文字数オーバーです');
        submitFlg = false;
    }
    return submitFlg; 
}
function showLength3() {
    inputSearchLength.innerText =("00" + String(searchInput.value.length)).slice(-3) + "/128";
    if(searchInput.value.length > 128){
        inputSearchLength.style.color = "red";
    } else if(searchInput.value.length <= 128){
     inputSearchLength.style.color = "white";
    }
 }
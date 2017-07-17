var nums = [];

for (var i = 0 ; i<10 ; i++){
    nums.push(i);
}

function odds(num){
    return num%2 == 1;
}

function evens(num){
    return num%2 == 0;
}

function sum(total, num){
    return total + num;
}

window.onload = function(){
    var br_1 = document.createElement('br');
    var br_2 = document.createElement('br');
    
    var arr_evens =  nums.filter(evens);    
    var text_evens = document.createTextNode(arr_evens);
    var text_evens_sum = document.createTextNode(arr_evens.reduce(sum));
    document.getElementById("even").appendChild(text_evens);
    document.getElementById("even").appendChild(br_1);
    document.getElementById("even").appendChild(text_evens_sum);
    
    var arr_odds = nums.filter(odds);    
    var text_odds = document.createTextNode(arr_odds);
    var text_odds_sum = document.createTextNode(arr_odds.reduce(sum));
    document.getElementById("odd").appendChild(text_odds);
    document.getElementById("odd").appendChild(br_2);
    document.getElementById("odd").appendChild(text_odds_sum);

};





















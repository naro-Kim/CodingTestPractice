/**
1. 튜플이 짧은 순서로 정렬한다. 
2. 짧은 튜플에 들어가있는 원소부터 배열에 집어넣는다. 
3. 만일 배열에 그 원소가 없다면 마지막 튜플까지 돌면서 배열에 계속 넣는다.
*/

function solution(s) {
    var ans = [];
    s = s.slice(2,-2).split(/},{/g).sort((a,b)=>a.length-b.length);
    for(const arr of s){
        const nums = arr.split(',');
        for(let num of nums){ 
            if(!ans.includes(num)) ans.push(num);
        }
    }
    return ans.map(v=>+v);
}
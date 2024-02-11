/**
* 문자열 길이가 1인 알파벳 대문자로 사전을 초기화한다.
* 현재 입력에서 가장 일치하는 부분이 긴 문자 w를 찾는다.
* w에 해당하는 사전의 색인을 출력하고 입력에서 w를 제거한다.
* 입력에 w를 제외하고도 글자 c가 남아있다면 w+c를 사전에 등록한다.
*/


function solution(msg) {
    let obj = {}; 
    for(let i=1; i<27; i++){ 
        obj[String.fromCharCode(i+64)] = i;
    }

    
    let ans = []; 
    let chk = ''; // chk includes cur sentence
    let i = 0; 
 
    const str = msg.split("").reduce((acc, cur)=>{
        chk = acc+cur; 
        if(!obj[chk]) {
            obj[chk] = ++Object.keys(obj).length;
        } else {
            return acc+cur;
        } 
        if(obj[acc]) ans.push(obj[acc]);
        return cur;
    });
        
    if(str && obj[str]) {
        ans.push(obj[str])
    }; 
    return ans;
}
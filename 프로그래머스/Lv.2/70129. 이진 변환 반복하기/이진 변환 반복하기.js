function solution(s) {
    let ans = [];
    let len = s.length;
    let cnt = 0;
    let zeroCnt = 0;
    
    while(s != "1"){ 
        s = s.split("").filter((num) => { if(num === "0") zeroCnt++; return num === "1"}); 
        len = s.length;
        s = len.toString(2);
        cnt++;
    }
    ans.push(cnt);
    ans.push(zeroCnt);
    return ans;
}


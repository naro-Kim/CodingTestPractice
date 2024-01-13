/** 수열의합 = '첫 수 + 마지막 수 * 개수 / 2'
개수 = end - start + 1
*/ 
const solution = (n) => {
    let sum = 0; 
    let cnt = 1; //반드시 end === n이 된다 
       
    for(i = 1; i <= Math.floor(n/2); i++){
        let start = i;
        let end = start+1;
        while(end < n){ 
            const curSum = ((start + end) * (Math.abs(end-start) + 1)) / 2;
            if(curSum < n){
                end++;
            } else if(curSum > n){
                start++;
                end++;
            } else {
                [start, end] = [end+1, start+1];
                cnt++;
                break;
            }
        }
    }

    
    return cnt
}
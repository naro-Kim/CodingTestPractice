// 최대공약수
const gcd = (a,b) => a%b === 0 ? b : gcd(b, a%b); 

function solution(arr) { 
    let g = gcd(arr[0], arr[1]);
    let ans = Math.floor((arr[0] * arr[1])/g); 
    
    for(let i=2; i < arr.length; i++){
        g = gcd(ans, arr[i]); 
        ans = ((ans * arr[i]) / g) 
    }
    return ans;
}
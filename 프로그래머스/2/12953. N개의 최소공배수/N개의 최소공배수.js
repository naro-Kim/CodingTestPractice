// 최대공약수
const gcd = (a,b) => a%b === 0 ? b : gcd(b, a%b); 

// n개의 최소공배수는 최소공배수 누적
const solution = (arr) => arr.reduce((a,b)=> a*b / gcd(a,b)); 
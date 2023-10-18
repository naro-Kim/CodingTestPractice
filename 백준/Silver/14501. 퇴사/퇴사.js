let [n, ...input] = require("fs").readFileSync('/dev/stdin').toString().trim().split("\n").map((v) => v.split(" ").map((v) => +v));

n = n[0];
const dp = new Array(n).fill(0);

for(let i=0; i<n; i++){
    const [t, p] = input[i]; 
    if (i + t > n) continue;
    dp[i] += p;
    for(let j=i+t; j<n;j++){
        dp[j] = Math.max(dp[j], dp[i])
    }
}
 
console.log(Math.max(...dp));
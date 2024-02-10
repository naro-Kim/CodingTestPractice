const [n, ...input] = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => +v) 

 let cnt = 0;
for (let i = n-1; i > 0; i--) {
  while(input[i]-1 < input[i-1]) {
    input[i-1]--;
    cnt++;
  }
}

console.log(cnt);

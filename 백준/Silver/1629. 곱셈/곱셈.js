const [A, B, C] = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split(' ')
  .map(BigInt);

function pow(a, b) {
  if (b == 1n) return a % C; // break 조건
  
  let val = pow(a, b / 2n); // 짝수 조건. 지수끼리 더해지므로 2n == n * n
  if (b % 2n) return (val * val * (a%C)) % C;
  else return val = (val * val) % C;
}

console.log(pow(A,B,C).toString());
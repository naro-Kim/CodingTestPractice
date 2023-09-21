const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');

const [n, m] = input[0].split(' ').map((v) => +v);
const balls = new Array(n).fill(0);

for (let idx = 0; idx <= m; idx++) {
  let [i, j, k] = input[idx].split(' ').map((v) => +v);
  for (i; i <= j; i++) {
    balls[i - 1] = k;
  }
}
console.log(balls.join(" "));
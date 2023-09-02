const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');

const [n, m] = input[0].split(' ');
const arr = input[1].split(' ').map((e) => +e).sort((a, b) => a - b);

function solution(n, m, arr) {
  const seq = new Array(m).fill(0);
  const visited = new Array(n).fill(false);
  let result = '';

  const recursion = (k) => { 
    if (k >= m) {
      result += `${seq.join(' ')}\n`; 
      return;
    } 
    for (let i = 0; i < n; i++) {
      if (!visited[i]) {
        visited[i] = true;
        seq[k] = arr[i];
        recursion(k + 1);
        visited[i] = false;
      }
    }
  }

  recursion(0);
  console.log(result);
}

solution(n, m, arr);
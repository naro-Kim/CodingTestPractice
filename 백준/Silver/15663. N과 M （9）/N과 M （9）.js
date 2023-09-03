const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');

const [n, m] = input[0].split(' ');
const arr = input[1].split(' ').map((e) => +e).sort((a, b) => a - b);
//const len = arr.length

function solution(n, m, arr) {
  const seq = new Array(m).fill(0);  
  const visited = new Array(n).fill(0);  
  let result = new Set();

  const recursion = (k, num) => { 
    if (num >= m) {
      result.add(`${seq.join(' ')}`); 
      return;
    } 
    for (let i = 0; i < n; i++) { 
        if(!visited[i]){
            visited[i] = true;
            seq[num] = arr[i];
            recursion(k + 1, num + 1); 
            visited[i] = false;
        }
    }
  }
  recursion(0, 0);
  console.log([...result].join('\n'));
}

solution(n, m, arr);
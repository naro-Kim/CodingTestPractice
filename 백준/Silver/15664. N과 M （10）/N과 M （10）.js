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
  const visited = new Array(n).fill(false);   
  let result = new Set();

  const recursion = (k, num) => { 
    if (k >= m) {
      result.add(`${seq.join(' ')}`); 
      return;
    } 
    for (let i = num; i < n; i++) { 
        if(!visited[i]){
            visited[i] = true;
            seq[k] = arr[i];
            recursion(k + 1, i + 1);  
            visited[i] = false;
        }
    }
  }
  recursion(0, 0);
  console.log([...result].join('\n'));
}

solution(n, m, arr);
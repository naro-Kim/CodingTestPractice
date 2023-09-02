/**
 * input = [N. M]
 * 1부터 N까지 자연수 중에서 M개를 고른 수열 
 * 같은 수를 여러 번 골라도 된다.
*/

const [n, m] = require('fs')
  .readFileSync('/dev/stdin')
  .toString() 
  .split(' ')
  .map(Number);

function solution(n, m) {
    const seq = new Array(m).fill(0);
    let result = ''; 
    
    // k = 현재 탐색중인 인덱스 
    const recurssion = (k) => {
          if (k === m) {
            result += `${seq.join(' ')}\n`
            return;
          }
          for (let i = 1; i <= n; i++) {
            seq[k] = i;
            recurssion(k+1);
          }
    } 
    recurssion(0);
    console.log(result)
}

solution(n, m);
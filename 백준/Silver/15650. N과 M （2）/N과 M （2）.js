const [n, m] = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split(' ')
  .map(Number);

function solution(n, m) {
    const seq = new Array(m).fill(0);
    const visited = new Array(n+1).fill(false);
    let result = []; 
    
    // k = 현재 탐색중인 인덱스
    // num = 현재 배열에 들어있는 수
    const dfs = (k, num) => {
          if (num === m) {
            result.push(seq.slice())
            return;
          }
          for (let i = k; i <= n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                seq[num] = i;
                dfs(i+1, num+1);
                visited[i] = false;
            }
          }
    }
    
    dfs(1, 0)
    for(const combination of result) {
        console.log(combination.join(' '));
    }
}

solution(n, m, 0, new Array(10).fill(false));
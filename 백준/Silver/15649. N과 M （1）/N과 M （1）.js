const [n, m] = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split(' ')
  .map(Number);

function solution(n, m, cnt, visited, combination = '') {
  if (cnt === m) {
    console.log(combination);
    return;
  }

  for (let i = 1; i <= n; i++) {
    if (!visited[i]) {
      visited[i] = true;
      const newCombination = combination === '' ? i : `${combination} ${i}`;
      solution(n, m, cnt + 1, visited, newCombination);
      visited[i] = false;
    }
  }
}

solution(n, m, 0, new Array(10).fill(false));
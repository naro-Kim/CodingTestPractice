class Queue {
  constructor() {
    this.storage = {};
    this.front = 0;
    this.rear = 0;
  }

  isEmpty(){
    return this.size() === 0;
  }
  
  size() {
    if (this.storage[this.front] === undefined) return 0;
    else return this.rear - this.front + 1;
  }

  add(value) {
    if (this.size() === 0) this.storage["0"] = value;
    else {
      this.rear++;
      this.storage[this.rear] = value;
    }
  }

  popleft() {
    let tmp;
    tmp = this.storage[this.front];
    delete this.storage[this.front];
    if (this.front === this.rear) {
      this.front = 0;
      this.rear = 0;
    } else {
      this.front++;
    }
    return tmp;
  }
}

let map = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(""));
 
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
const combX = new Array(25);
const combY = new Array(25);
const visited = new Array(7).fill(false);
let ans = 0;

for (let i = 0; i < 25; i++) {
  combX[i] = i % 5;
  combY[i] = Math.floor(i / 5);
}

function combination(comb, idx, depth, left) {
  if (left === 0) {
    bfs(comb);
    return;
  }

  if (depth === 25) return;

  comb[idx] = depth;
  combination(comb, idx + 1, depth + 1, left - 1); // 선택한 경우
  combination(comb, idx, depth + 1, left); // 선택하지 않은 경우
}

function bfs(comb) {
  const queue = [];
  visited.fill(false);

  visited[0] = true;
  queue.push(comb[0]);
  let cnt = 1;
  let sCnt = 0;

  while (queue.length > 0) {
    const cur = queue.shift();
    if (map[combY[cur]][combX[cur]] === 'S') sCnt++;

    for (let i = 0; i < 4; i++) {
      for (let next = 1; next < 7; next++) {
        if (
          !visited[next] &&
          combX[cur] + dx[i] === combX[comb[next]] &&
          combY[cur] + dy[i] === combY[comb[next]]
        ) {
          visited[next] = true;
          queue.push(comb[next]);
          cnt++;
        }
      }
    }
  }

  if (cnt === 7 && sCnt >= 4) {
    ans++;
  }
}

combination(new Array(7), 0, 0, 7);
console.log(ans);
let [nm, ...board] = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map((v) => +v));

const dxdy = [
  [-1, 0],
  [1, 0],
  [0, -1],
  [0, 1],
];

let ans = 0;
let cnt;
let visited;

const chkRange = (y, x) => {
  return 0 <= y && y < nm[0] && 0 <= x && x < nm[1];
};

// 빙산 하나 당 주변 바다를 계산한다.
const chkMelting = (y, x) => {
  let result = 0;
  for (let i = 0; i < 4; i++) {
    const [ny, nx] = [y + dxdy[i][1], x + dxdy[i][0]];
    if (chkRange(ny, nx) && !board[ny][nx]) result++;
  }
  return result;
};

// 빙산이 얼마나 나뉘었는지 체크한다.
const bfs = (y, x) => {
  const queue = [[y, x]];
  visited[y][x] = true;

  while (queue.length) {
    let [curY, curX] = queue.shift();
    for (let i = 0; i < 4; i++) {
      const [ny, nx] = [curY + dxdy[i][1], curX + dxdy[i][0]];
      if (chkRange(ny, nx) && !visited[ny][nx] && board[ny][nx]) {
        queue.push([ny, nx]);
        visited[ny][nx] = true;
      }
    }
  }
};

// 빙산 상태를 카피한 후에 visited와 빙산 나뉨 상태를 재초기화
while (true) {
  cnt = 0;
  visited = Array.from({ length: nm[0] }, () =>
    Array.from({ length: nm[1] }, () => false),
  );
  
  for (let i = 0; i < nm[0]; i++) {
    for (let j = 0; j < nm[1]; j++) {
      if (board[i][j] && !visited[i][j]) { 
        cnt++;
        bfs(i, j);
      }
    }
  }

  if (cnt === 0) return console.log(0);
  if (cnt >= 2) return console.log(ans);

  // copy map
  let copiedBoard = Array.from({ length: nm[0] }, () =>
    Array.from({ length: nm[1] }, () => 0),
  );

  for (let i = 0; i < nm[0]; i++) {
    for (let j = 0; j < nm[1]; j++) {
      if (board[i][j]) {;
        copiedBoard[i][j] = board[i][j] - chkMelting(i, j);
        if (copiedBoard[i][j] < 0) copiedBoard[i][j] = 0;
      }
    }
  }

  // paste copied map into board
  board = copiedBoard.map((row) => row.slice());
  ans++;
}
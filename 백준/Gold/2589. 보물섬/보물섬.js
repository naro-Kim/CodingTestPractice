let input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [L, W] = input.shift().split(" ").map(Number);
board = input.map((row) => row.split(""));
const visitedBoard = Array.from({ length: L }, () => new Array(W).fill(false));
let ans = 0;
const dxdy = [
  [-1, 0],
  [1, 0],
  [0, -1],
  [0, 1],
];

const bfs = (row, col) => {
  const visited = Array.from({ length: L }, () => new Array(W).fill(false));
  const q = [[row, col]];
  visited[row][col] = 1;
  let res = 0;

  while (q.length) {
    const [y, x] = q.shift();
    for (let i = 0; i < 4; i++) {
      nx = x + dxdy[i][0];
      ny = y + dxdy[i][1];
      if (
        nx <= -1 ||
        nx >= W ||
        ny <= -1 ||
        ny >= L ||
        visited[ny][nx] ||
        board[ny][nx] === "W"
      )
        continue;
      if (board[ny][nx] === "L") {
        visited[ny][nx] = visited[y][x] + 1;
        res = Math.max(visited[ny][nx], res);
        q.push([ny, nx]);
      }
    }
  }
  return res - 1;
};

for (let i = 0; i < L; i++) {
  for (let j = 0; j < W; j++) {
    if (!visitedBoard[i][j] && board[i][j] == "L") {
      ans = Math.max(ans, bfs(i, j));
    }
  }
}

console.log(ans);
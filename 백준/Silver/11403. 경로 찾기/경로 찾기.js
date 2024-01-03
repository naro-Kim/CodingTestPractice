const [N, ...board] = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map(v=>+v));

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    for (let k = 0; k < N; k++) {
      if (board[j][i] && board[i][k])
        // 두 정점이 경로를 가진 경우
        board[j][k] = 1;
    }
  }
}

for (const line of board) {
  console.log(...line.join(""));
}
const [NM, ...relation] = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map((v) => +v));

const [N, M] = NM;
const mat = Array.from({ length: N }, () => new Array(N).fill(Infinity));

for (const [a, b] of relation) {
  mat[a - 1][b - 1] = mat[b - 1][a - 1] = 1;
}

for (let k = 0; k < N; k++) {
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      mat[i][j] = Math.min(mat[i][j], mat[i][k] + mat[k][j]);
    }
  }
}

for (let i = 0; i < N; i++) {
  mat[i][i] = 0;
}

const sum = [];
for (const line of mat) {
  sum.push(line.reduce((acc, cur) => acc + cur, 0));
}

let min = sum[0];
let idx = 0;

for (let i = 1; i < N; i++) {
  if (min > sum[i]) {
    min = sum[i];
    idx = i;
  }
}

console.log(idx + 1);
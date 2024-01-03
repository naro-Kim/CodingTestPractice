let [N, ...relation] = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map((v) => +v));

N = +N;

const mat = Array.from({ length: N }, () => new Array(N).fill(1e2));
const ans = [];

for (let i = 0; i < relation.length - 1; i++) {
  const [a, b] = relation[i];
  mat[a-1][b-1] = mat[b-1][a-1] = 1;
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

let result = [];
let score = 100;

for (let i = 0; i < N; i++) {
  const tmpMax = Math.max(...mat[i]);
  ans.push(tmpMax);
  score = Math.min(score, tmpMax);
}

ans.map((x, idx) => {
  if (x === score) {
    result.push(idx + 1);
  }
});

console.log(score, result.length);
console.log(result.join(" "));
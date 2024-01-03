let [N, ...relation] = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map((v) => +v));

relation.pop();
N = +N;

let ans = "";
let score = 0;
let candidates = [];

const mat = Array.from({ length: N }, () => new Array(N).fill(Infinity));

for (let i = 0; i < relation.length; i++) {
  const [a, b] = relation[i];
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

let min = Infinity;
for (let i = 0; i < N; i++) {
  let tmp = Math.max(...mat[i]);
  if (tmp < min) {
    min = tmp;
  }
}
score = min;

for (let i = 0; i < N; i++) {
  let tmp = Math.max(...mat[i]);
  if (tmp === score) {
    candidates.push(i + 1);
  }
}

console.log(score, candidates.length);
console.log(candidates.join(' '));
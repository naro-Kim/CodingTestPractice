const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map((v) => +v));

const [n, m] = input.shift();
const graph = Array.from({ length: n + 1 }, () => []);
const visited = Array.from({ length: n + 1 }, () => false);
let ans = 0;

const dfs = (start) => {
  let st = [...start]; // child nodes
  while (st.length) {
    let child = st.pop();
    if (!visited[child]) {
      visited[child] = true;
      st.push(...graph[child]);
    }
  }
};

for (const [from, to] of input) {
  graph[from].push(to);
  graph[to].push(from);
}

// 1<= u <= N 이므로, 0부터 시작할 필요가 없음
for (let i = 1; i < graph.length; i++) {
  if (!visited[i]) {
    ans++;
    dfs(graph[i]);
  }
}

console.log(ans);
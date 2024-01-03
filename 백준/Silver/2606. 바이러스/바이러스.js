const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = Number(input.shift());
const M = Number(input.shift());
const graph = Array.from({ length: N + 1 }, () => []);
const visited = Array.from({ length: N + 1 }, () => false);
let ans = 0;
for (const line of input) {
  const [a, b] = line.split(" ").map((v) => +v);
  graph[b].push(a);
  graph[a].push(b);
}

const dfs = (start) => {
  const st = [...start];
  while (st.length) {
    let child = st.pop();
    if (!visited[child]) {
      ans++;
      visited[child] = true;
      st.push(...graph[child]);
    }
  }
};

dfs(graph[1]);
console.log(ans > 0 ? ans - 1 : 0);
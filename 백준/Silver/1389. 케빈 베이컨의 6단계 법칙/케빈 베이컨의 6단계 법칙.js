class Deque {
  constructor() {
    this.data = [];
    this.head = 0;
    this.tail = 0;
  }

  popLeft() {
    if (this.head >= this.tail) return null;
    else return this.data[this.head++];
  }

  append(item) {
    this.data[this.tail++] = item;
  }

  size() {
    return this.tail - this.head;
  }
}

const [NM, ...relation] = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map((v) => +v));

const [N, M] = NM;
const graph = Array.from({ length: N }, () => []);

for (const [a, b] of relation) {
  graph[a - 1].push(b - 1);
  graph[b - 1].push(a - 1);
}

const sum = [];
let min = Infinity;
let idx = 0;

const bfs = (start) => {
  const visited = Array.from({ length: N }, () => 0);
  const q = new Deque();
  q.append(start);
  while (q.size()) {
    const node = q.popLeft();
    for (const next of graph[node]) {
      if (!visited[next]) {
        visited[next] = visited[node] + 1;
        q.append(next);
      }
    }
  }
  return visited.reduce((a, c) => a + c, 0);
};

for (let i = 0; i < N; i++) {
  sum.push(bfs(i));
  if (min > sum[i]) {
    min = sum[i];
    idx = i;
  }
}
console.log(idx + 1);
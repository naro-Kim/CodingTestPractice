class Deque {
  constructor() {
    this.data = [];
    this.head = 0;
    this.tail = 0;
  }

  appendLeft(item) {
    if (this.data[0]) {
      for (let i = this.arr.length; i > 0; i--) {
        this.data[i] = this.data[i - 1];
      }
    }
    this.data[this.head] = item;
    this.tail++;
  }

  append(item) {
    this.data[this.tail++] = item;
  }

  popLeft() {
    if (this.head >= this.tail) {
      return null;
    } else {
      return this.data[this.head++];
    }
  }

  pop() {
    if (this.head >= this.tail) {
      return null;
    } else {
      return this.data[--this.tail];
    }
  }

  size() {
    return this.tail - this.head;
  }
}

const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = Number(input.shift());
const M = Number(input.shift());
const graph = Array.from({ length: N + 1 }, () => []);
const visited = Array.from({ length: N + 1 }, () => false);
let cnt = 0;

for (const line of input) {
  const [a, b] = line.split(" ").map((v) => +v);
  graph[a].push(b);
  graph[b].push(a);
}

const q = new Deque();
q.append([1, 0]); // [start node, depth]
visited[1] = true;

while (q.size()) {
  const [node, depth] = q.popLeft();
  if (depth <= 2) cnt++;
  for (const next of graph[node]) {
    if (!visited[next]) {
      visited[next] = true;
      q.append([next, depth + 1]);
    }
  }
}

console.log(cnt > 0 ? cnt-1 : 0);
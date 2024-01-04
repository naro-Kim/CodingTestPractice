const [NM, ...relation] = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map((v) => +v));

/**
1. 순방향, 역방향 인접 리스트 만들기.
 * @params {number} v : 노드 갯수
 * @params {[number, number][]} edges : 간선 정보
 */
const makeConnection = (v, edges) => {
  const graph = Array.from({ length: v + 1 }, () => []); //순방향 그래프
  const reGraph = Array.from({ length: v + 1 }, () => []); //역방향 그래프
  edges.forEach(([from, to]) => {
    graph[from].push(to);
    reGraph[to].push(from);
  });
  return [graph, reGraph];
};

/** 
2. 후위 순회 dfs
* @param {number} node : 노드 번호
* @param {number[]} stack : 순회 순서가 저장된 스택
* @param {number[][]} graph : 순회할 그래프
* @param {boolean[]} visit : 방문 여부를 조회하는 스택
*/
const dfs = (node, stack, graph, visit) => {
  graph[node].forEach((next) => {
    if (!visit[next]) {
      visit[next] = true;
      dfs(next, stack, graph, visit);
    } else return;
  });
  stack.push(node);
};

/**
3. 후위 순회 dfs 스택
 * @param {number} v 노드 갯수 
 * @param {number[][]} graph
 */
const makeStack = (v, graph) => {
  const visit = Array(v).fill(false);
  const stack = [];
  for (let node = 1; node < v; node++) {
    if (!visit[node]) {
      visit[node] = true;
      dfs(node, stack, graph, visit);
    }
  }
  return stack;
};

/** 
4. SCC 결합
 * @param {number} v : 정점
 * @param {number[]} stack : 순방향 순회 후 root가 가장 위에 있는 스택
 * @param {number[][]} reGraph : 역방향 그래프
*/

const makeSCC = (v, stack, reGraph) => {
  const visit = Array(v).fill(false);
  const res = [];

  for (let i = stack.length - 1; i >= 0; i -= 1) {
    const node = stack[i];
    if (!visit[node]) {
      const group = [];
      visit[node] = true;
      dfs(node, group, reGraph, visit);
      res.push(group);
    }
  }

  return res;
};

const [N, M] = NM;
const [graph, reGraph] = makeConnection(N, relation);
const stack = makeStack(N, graph);

const scc = makeSCC(N, stack, reGraph)
  .map((arr) => arr.sort((a, b) => a - b))
  .sort((a, b) => Math.min(...a) - Math.min(...b));

console.log(scc.length);
scc.forEach((arr)=>{
  console.log(...arr, -1);
})
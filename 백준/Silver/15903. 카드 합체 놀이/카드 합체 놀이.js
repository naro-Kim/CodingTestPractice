// 가장 작은 수 순의 정렬을 유지해야 한다 -> 힙
class MinHeap {
  constructor() {
    this.heap = [null];
  }

  getMin() {
    return this.heap[1];
  }

  size() {
    return this.heap.length - 1;
  }

  isEmpty() {
    return this.heap.length < 2;
  }

  insert(node) {
    let current = this.heap.length;
    //child 정리
    while (current > 1) {
      const parent = Math.floor(current / 2);
      if (this.heap[parent] > node) {
        this.heap[current] = this.heap[parent];
        current = parent;
      } else break;
    }
    this.heap[current] = node;
  }

  remove() {
    // root를 제거하고 반환하며 힙을 정렬합니다
    let min = this.heap[1];
    if (this.heap.length > 2) {
      this.heap[1] = this.heap[this.heap.length - 1];
      this.heap.splice(this.heap.length - 1);

      let current = 1;
      let left = current * 2;
      let right = current * 2 + 1;

      while (this.heap[left]) {
        let childIndexToCompare = left;
        if (
          this.heap[right] &&
          this.heap[right] < this.heap[childIndexToCompare]
        )
          childIndexToCompare = right;
        if (this.heap[childIndexToCompare] < this.heap[current]) {
          [this.heap[childIndexToCompare], this.heap[current]] = [
            this.heap[current],
            this.heap[childIndexToCompare],
          ];
          current = childIndexToCompare;
        } else break;

        left = current * 2;
        right = current * 2 + 1;
      }
    } else if (this.heap.length === 2) {
      this.heap.splice(1, 1);
    } else {
      return null;
    }
    return min;
  }

  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }
}

const minHeap = new MinHeap();
let [nm, nums] = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" "))
  .map((str) => str.map((v) => +v));

const [n, m] = nm;
nums = nums.sort((a, b) => a - b).forEach((num) => minHeap.insert(num));

for (let i = 0; i < m; i++) {
  const a = minHeap.remove();
  const b = minHeap.remove();
  const sum = BigInt(a) + BigInt(b);
  minHeap.insert(sum);
  minHeap.insert(sum);
}

const ans = minHeap.heap
  .slice(1)
  .reduce((acc, cur) => BigInt(acc) + BigInt(cur), 0n);
console.log(ans.toString());

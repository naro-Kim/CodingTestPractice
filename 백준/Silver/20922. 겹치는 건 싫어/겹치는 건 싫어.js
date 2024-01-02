const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");
const [n, k] = input[0].split(" ").map((x) => +x);
const nums = input[1].split(" ").map((x) => +x);

const cnt = new Array(100000).fill(0);
let res = 0;
let start = 0;
let end = 0;

while (end < n) {
  if (cnt[nums[end]] >= k) {
    // start 포인터를 옮김
    cnt[nums[start]]--;
    start++;
  } else {
    // end 포인터를 옮김
    cnt[nums[end]]++;
    end++;
  }
  res = Math.max(res, end - start);
}

console.log(res);

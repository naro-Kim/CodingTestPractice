let [nm, ...nums] = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

nums = nums.map((v) => +v).sort((a, b) => a - b);
const [n, m] = nm.split(" ").map((v) => +v);

let sub = Infinity;
let l = 0;
let r = 0;

// 같은 수를 두번 고를 수도 있으므로 l<=r
while (l <= r && r < n) {
  const diff = Math.abs(nums[r] - nums[l]);
  if (diff < m) {
    r++;
  } else {
    l++;
    sub = Math.min(sub, diff);
  }
  if (diff === m) {
    break;
  }
}
console.log(sub);

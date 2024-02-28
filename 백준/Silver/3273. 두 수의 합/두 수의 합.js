let [n, nums, x] = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" "))
  .map((str) => str.map((v) => +v));
nums = nums.sort((a,b)=> a-b);

let a = 0;
let b = n[0] - 1;
let ans = 0;
while (a !== b) {
  const sum = nums[a] + nums[b];
  if (sum === x[0]) {
    ans++;
    a++;
  } else if (sum < x[0]) {
    a++;
  } else {
    b--;
  }
} 

console.log(ans);
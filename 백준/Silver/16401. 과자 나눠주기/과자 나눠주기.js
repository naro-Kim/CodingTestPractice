let [MN, cookie] = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((e) => e.split(" ").map((v) => +v));

const [M, N] = MN;
cookie = cookie.sort((a, b) => a - b);

const check = (M, cookie, ans) =>
  cookie.reduce((acc, cur) => acc + Math.floor(cur / ans), 0) >= M;

const binarySearch = (M, cookie) => {
  let answer = 0;
  let left = 1; // 과자 최소길이
  let right = 1000000000; //과자 최대길이

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (check(M, cookie, mid)) {
      left = mid + 1;
      answer = mid;
    } else {
      right = mid - 1;
    }
  }
  return answer;
};

console.log(binarySearch(M, cookie));
const input = require("fs")
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split("\n");
const [n, m] = input[0].split(" ").map((num) => +num); // 공백을 기준으로 number type 변수 n,m을 저장
const arr = input[1].split(" ").map((v) => +v); //  // 공백을 기준으로 array에 number type values 저장
const cumsum = new Array(arr.length + 1).fill(0);
const output = [];

arr.forEach((v, i) => {
  cumsum[i + 1] = cumsum[i] + v;
});

input.slice(2).forEach((item) => {
  const [start, end] = item.split(" ").map((v) => +v);
  output.push(cumsum[end] - cumsum[start - 1]);
});

console.log(output.join("\n"));

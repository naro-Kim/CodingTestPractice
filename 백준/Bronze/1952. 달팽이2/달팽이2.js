const [m, n] = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map((v) => +v);

m <= n ? console.log((m - 1) * 2) : console.log(Math.min(m, n) * 2 - 1);
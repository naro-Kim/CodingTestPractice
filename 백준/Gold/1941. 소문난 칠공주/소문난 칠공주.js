let input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((e) => e.split(""));
let ans = 0;
let usedRoom = new Array(25).fill(0);
let tmp = [];
let dr = [-1, 0, 1, 0];
let dc = [0, 1, 0, -1]; 
check();
console.log(ans);

function check(n = 0, r, c, y = 0) {
  if (y == 4) return;
  if (n == 7) {
    let cnt = dfs(tmp[0]);
    setUsedRoomByTmp();
    if (cnt == 7) {
      ans++;
    }
    return;
  }
  if (n == 0) {
    for (let i = 0; i < 5; i++) {
      for (let j = 0; j < 5; j++) {
        usedRoom[i * 5 + j] = 1;
        tmp[n] = i * 5 + j;
        if (input[i][j] == "Y") check(1, i, j, 1);
        else check(1, i, j, 0);
        usedRoom[i * 5 + j] = 0;
        tmp.length = 0;
      }
    }
  } else {
    for (let i = r; i < 5; i++) {
      for (let j = i == r ? c + 1 : 0; j < 5; j++) {
        usedRoom[i * 5 + j] = 1;
        tmp[n] = i * 5 + j;
        if (input[i][j] == "Y") {
          check(n + 1, i, j, y + 1);
        } else check(n + 1, i, j, y);
        usedRoom[i * 5 + j] = 0;
        tmp.length = n;
      }
    }
  }
}

function dfs(dn) {
  let nr,
    nc,
    tr,
    tc,
    cnt = 1;
  usedRoom[dn] = 0;
  nr = Math.floor(dn / 5);
  nc = dn % 5;
  for (let d = 0; d < 4; d++) {
    tr = nr + dr[d];
    tc = nc + dc[d];
    if (0 <= tr && tr < 5 && 0 <= tc && tc < 5 && usedRoom[tr * 5 + tc] == 1)
      cnt += dfs(tr * 5 + tc);
  }
  return cnt;
}

function setUsedRoomByTmp() {
  for (let i = 0; i < 7; i++) {
    usedRoom[tmp[i]] = 1;
  }
}
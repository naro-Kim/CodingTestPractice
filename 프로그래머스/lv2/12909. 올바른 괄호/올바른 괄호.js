function solution(s) {
  let st = 0;
  for (let char of s) {
    if (char === "(") {
      st++;
    } else if (char === ")" && st) {
      st--;
    } else {
      return false;
    }
  }
  return st ? false : true;
}

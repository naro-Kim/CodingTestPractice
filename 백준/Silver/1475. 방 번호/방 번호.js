const input = require("fs")
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split(""); 

const counts = new Array(10).fill(0);

const SIX = 6;
const NINE = 9;

for (const numStr of input) {  
    const num = Number(numStr);
    if (num === SIX || num === NINE) {
        const otherNum = num === SIX ? NINE : SIX;
        if (counts[num] > counts[otherNum]) {
            counts[otherNum]++;
        } else {
            counts[num]++;
        }
    } else {
        counts[num]++;
    }
}

console.log(Math.max(...counts));

const input = require("fs")
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split("\n");
let output ="";
const n = Number(input.shift())
const nums = input.map(Number).sort((a, b)=> a - b);
const l = input.length; 

output += `${Math.round((nums.reduce((a,b)=> a+b, 0))/n)}\n`;
output += `${nums[Math.floor(l/2)]}\n`;

const freq = nums.reduce((freq, num)=> {
    freq[num] = (freq[num] || 0) + 1;
    return freq;
},[]);

let maxFreq = 0;
let mode = [];

for (const [n, cnt] of Object.entries(freq)){
    if(cnt > maxFreq){
        maxFreq = cnt;
        mode = [n];
    } else if (cnt === maxFreq){
        mode.push(n);
    }
}

mode = mode.map(Number).sort((a, b) => a - b); 

output += mode.length > 1 ? `${mode[1]}\n` : `${mode[0]}\n`
output += `${Math.max(...nums) - Math.min(...nums)}`

console.log(output)   
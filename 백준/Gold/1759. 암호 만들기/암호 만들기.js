const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');

const [L, C] = input[0].split(' ').map((e)=>+e);
const arr = input[1].split(' ').sort();
const vowels = ['a', 'e', 'i', 'o', 'u'];

function solution(L, C, arr) {
  const seq = new Array(L).fill(0);   
  const used = new Array(C).fill(false);   
  let result = new Set(); 


  const recursion = (index, start) => { 
    if (start >= L) {
        let vow = 0;
        seq.forEach((char)=>{
            if(vowels.includes(char)) vow++;
        }) 
        if(vow && L-vow > 1) result.add(`${seq.join('')}`); 
      return;
    } else {
        for (let i = index; i < C; i++) { 
            if(!used[i]){
                used[i] = true;
                seq[start] = arr[i];
                recursion(i, start+1); 
                used[i] = false;
            }
        }
    }
  }
  recursion(0, 0);
  console.log([...result].join('\n'));
}

solution(L, C, arr);

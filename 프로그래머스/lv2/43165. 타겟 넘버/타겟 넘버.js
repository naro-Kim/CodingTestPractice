function solution(numbers, target) {
    let ans = 0;
    let leaves = [0];
    numbers.forEach((num)=>{
        let tmp = []
        leaves.forEach((leaf)=>{
            tmp.push(leaf + num)
            tmp.push(leaf - num)
        })
        leaves = [...tmp]
    })
    
    leaves.forEach((leaf)=>{
        leaf === target && ans++;
    })
    return ans;
}
  
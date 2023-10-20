function solution(n, left, right) {
    const arr = []
    for(let i=left;i<=right;i++){
        let x = i % n;
        let y = Math.floor(i/n) 
        arr.push(Math.max(x,y)+1)
    }
    return arr;
}
 
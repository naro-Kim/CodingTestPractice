function solution(s) {
    let nums = s.split(" ").map((v)=>+v); 
    return `${Math.min(...nums)} ${Math.max(...nums)}`;
}
function solution(n, lost, reserve) {
    lost = lost.sort((a,b)=> a-b);
    reserve = reserve.sort((a,b)=> a-b);
    
    const list = new Map(reserve.map(e => [e,e])); 
    lost = lost.filter(e=> !list.delete(e))
    lost.forEach((e)=> list.delete(e-1) || list.delete(e+1) ? null : n--);
    
    return n
}
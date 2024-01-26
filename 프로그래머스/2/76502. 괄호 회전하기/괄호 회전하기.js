const isBalanced = (s) => {
    let brackets = {"(":")", "{":"}", "[":"]"}; 
    const validation = s.split('').reduce((acc,cur)=>{
        if(cur === brackets[acc[acc.length-1]]) acc.pop();
        else acc.push(cur);
        return acc;
    }, []);
    return validation.length === 0;
}

function solution(s) {
    const exLen = s.length;
    s = s.concat(s);
    const len = s.length;
    let ans = 0;
    
    for(i=0; i<exLen; i++){
        const str = s.slice(i, i+exLen); 
        if(isBalanced(str)) ans++;
    }
    
    return ans;
}
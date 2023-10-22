// 문자열 => number로 만들고 정렬한다. 
// k개의 수만큼 작은 수 부터 삭제한다. 


function solution(number, k) {
    number = number.split('')
    const stack = [];
    number.forEach((num)=>{
        while (stack.length > 0 && stack[stack.length - 1] < num && k > 0) {
            k -= 1;
            stack.pop();
        }
        stack.push(num);
    }) 

    if (k !== 0) {
        stack.splice(-k);
    }
    
    return stack.join("")
}
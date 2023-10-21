function solution(numbers) {
    let arr = [0,1,2,3,4,5,6,7,8,9]
    const ans = arr.filter(num => !numbers.includes(num)).reduce((acc,n)=> acc+=n, 0);
    return ans
}
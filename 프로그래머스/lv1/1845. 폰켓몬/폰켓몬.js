function solution(nums) { 
    let s = new Set(nums); 
    return nums.length/2 > s.size ? s.size : nums.length/2
}
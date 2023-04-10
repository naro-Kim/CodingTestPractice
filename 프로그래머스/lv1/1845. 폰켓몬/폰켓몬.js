function solution(nums) { 
    let map = new Map();
    nums.forEach(key => map.set(key, (map.get(key) || 0) + 1)) 
    return nums.length/2 > map.size ? map.size : nums.length/2
}
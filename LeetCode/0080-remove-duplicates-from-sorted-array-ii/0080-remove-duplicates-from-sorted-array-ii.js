/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let left = 2;
    for(let right=2; right<nums.length; right++){
        if(nums[left-2] !== nums[right]){ 
            nums[left++] = nums[right];
        } 
    } 
    return left;
};

 
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    let sum = 0;
    for (let left = 0; left < nums.length - 1; left++) {
        for (let right = left + 1; right < nums.length; right++) {
            sum = nums[left] + nums[right];
            if (sum === target) return [left, right];
        }
    }
};
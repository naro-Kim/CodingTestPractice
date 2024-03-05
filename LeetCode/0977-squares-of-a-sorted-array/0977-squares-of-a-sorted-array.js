var sortedSquares = function(nums) {
    const n = nums.length;
    const ans = new Array(n);
    let start = 0, end = n-1;
    for(let i=n-1; i>=0; i--){
        if(Math.abs(nums[start]) >= Math.abs(nums[end])){
            ans[i] = nums[start]**2;
            start++;
        } else {
            ans[i] = nums[end]**2;
            end--;
        }
    }
    return ans;
};
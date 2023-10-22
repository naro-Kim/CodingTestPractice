function solution(word) {
    const dict = { 'A': 1, 'E': 2, 'I': 3, 'O': 4, 'U': 5 };
    let nums = [1];
    let sum = 0;

    for (let i = 1; i < 5; i++) {
        if (nums[nums.length - 1]) {
            nums.push(nums[nums.length - 1] * 5 + 1);
        }
    }

    nums.reverse();

    for (let i = 0; i < word.length; i++) {
        if (dict[word[i]]) sum += nums[i] * (dict[word[i]] - 1) + 1;
    }

    return sum;
} 
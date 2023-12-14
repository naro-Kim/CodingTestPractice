const [n, nums] = require('fs')
	.readFileSync('dev/stdin')
	.toString()
	.trim()
	.split('\n')
	.map((v) => v.split(' ').map((v) => +v));

const ans = [];
const st = []; // stack에는 현재보다 높은 탑과 현재 탑만 존재한다.

// 스택 수열 응용
for (let i = 0; i < n; i++) {
	const cur = nums[i];
	while (st.length && nums[st[st.length - 1]] < cur) {
		st.pop(); // 현재 탑이 가장 높은 탑이 된다
	}
	if (st.length === 0) {
		ans.push(0);
	} else {
		ans.push(st[st.length - 1] + 1);
	}
	st.push(i);
}

console.log(ans.join(' '));

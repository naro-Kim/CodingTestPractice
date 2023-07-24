function solution(orders, course) {
    let answer = [];
    const d = {};
    let maxNum = {};
    
    const getCombinations = (arr, num) => {
        const results = []
        if (num === 1) return arr.map((el) => el);
        arr.forEach((fixed, idx, origin) => {
            const rest = origin.slice(idx + 1);
            const comb = getCombinations(rest, num - 1);
            const attached = comb.map((c) => [fixed, ...c].sort().join(''));
            results.push(...attached)
        })
        return results
    } 


    orders.forEach((order) => {
        const menu = order.split('').sort()
        course.forEach((num) => { 
            maxNum[num] = 0;
            getCombinations(menu, num).forEach((item) => {
                if (!d[item]) d[item] = 1;
                else d[item]++; // 조합 등장횟수
            })
        })
    });
    
    for (const item in d) {
        const len = item.length;
        if (d[item] > maxNum[len]) {
            maxNum[len] = d[item];
        }
    }

    for (const item in d) {
        const len = item.length;
        if (d[item] === maxNum[len] && maxNum[len] > 1 ) {
            answer.push(item);
        }
    } 

    return answer.sort();
}

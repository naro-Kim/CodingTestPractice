function solution(arr1, arr2) { 
    const a = arr1.length;
    const b = arr2[0].length;
    const c = arr2.length;
    const ans = Array.from({length : a}, () => new Array(b).fill(0));

    for(let i = 0; i < a; i++) {       
        for(let j = 0; j < b; j++) {
            for(let k = 0; k < c; k++) {
                ans[i][j] += arr1[i][k] * arr2[k][j];
            }
        }
    }

    return ans;
}

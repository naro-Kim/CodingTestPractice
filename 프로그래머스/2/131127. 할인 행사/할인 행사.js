/** 10일 연속으로 일치할 경우에 맞춰서 회원가입을 하려 합니다. === 수량만 일치하면 됨 
* 윈도우를 움직일 때마다 map 객체에 아이템을 넣었다가 뺀다
* 각 키 값을 세어 10개를 모두 살 수 있는지 확인
*/

const isMapEquals = (m1, m2) => m1.size === m2.size && Array.from(m1.keys()).every((key) => m1.get(key) === m2.get(key));

function solution(want, number, discount) {
    let ans = 0;
    const wantItems = new Map(want.map((key, idx) => [key, number[idx]]));

    for (let i = 0; i <= discount.length - 10; i++) {
        const windowItems = new Map();
        for (let j = i; j < i + 10; j++) {
            const item = discount[j];
            windowItems.set(item, (windowItems.get(item) || 0) + 1);
        }
        
        if (isMapEquals(windowItems, wantItems)) ans++;
    }

    return ans;
}

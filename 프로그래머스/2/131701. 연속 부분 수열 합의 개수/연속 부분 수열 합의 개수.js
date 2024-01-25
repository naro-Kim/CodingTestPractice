function solution(elements) {
    let s = new Set(); 
    const len = elements.length;

    for(let i=1; i<=len; i++){
        // i = 부분 수열 사이즈
        let sum = 0;
        let rear = 0;

         // 원소가 하나인 부분 수열은 바로 합을 구해 더해준다 
        for(let front=0; front<len; front++){  
            if(front === 0){
                while(rear < len) sum += elements[rear++];
            } else { 
                sum += elements[(front+i-1)%len];

            }
        s.add(sum);
        } 
    }

    return s.size
}

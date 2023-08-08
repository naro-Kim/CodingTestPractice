function solution(N, stages) {
    let answer = []; 
    let totalPlayers  = stages.length;
    const counts = new Array(N + 2).fill(0);
    stages.forEach(stage => counts[stage]++); 
    // prefix sum
    for (let i = 1; i <= N; i++) {
        const currentSuccess = counts[i];
        const failureRate = (totalPlayers-currentSuccess) / totalPlayers;
        
        totalPlayers -= currentSuccess
        answer.push({ stage: i, failureRate }); 
    } 
    answer.sort((a, b) => a.failureRate - b.failureRate);
    
    return answer.map(item => item.stage);
}
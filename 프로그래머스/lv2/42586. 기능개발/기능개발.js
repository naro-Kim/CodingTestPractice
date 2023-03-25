function solution(progresses, speeds) { 
    const answer = [0]
    const days = []
    progresses.forEach((key, idx)=>{ 
        days[idx] = Math.ceil((100 - key) / speeds[idx]);
    })  
    let num = days[0];
    for(let i=0,j=0 ; i < days.length; i++){
        if(num < days[i]){
            num = days[i]
            answer[++j] = 1
        } else {
            answer[j] += 1
        } 
        console.log(num,days[i],answer[j])
    }
     
    return answer;
}
function getKr(t){
    const curr = new Date(t) ;
    return curr.toLocaleString('sv') 
}

function chkPrivacies(today, time, term){
    const parsedDate = new Date(getKr(time))
    const t = new Date(parsedDate.setMonth(parsedDate.getMonth() + Number(term)))
    const now = new Date((today))
    return getKr(t) <= getKr(now)
}

function solution(today, terms, privacies) {
    var answer = [];
    for(let i=0; i< privacies.length; i++ ){
        let cur = privacies[i].split(' ')
        for(let j=0; j< terms.length; j++){
            let term = terms[j].split(' ')
            if(cur[1] == term[0] && chkPrivacies(today, cur[0], term[1])){
                answer.push(i+1)
            }
        }
    }
    return answer;
}
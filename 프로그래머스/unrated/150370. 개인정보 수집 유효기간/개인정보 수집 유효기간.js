function getFormattedDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleString('sv');
}

function checkPrivacies(today, time, term) {
    const parsedDate = new Date(getFormattedDate(time));
    const targetDate = new Date(parsedDate.setMonth(parsedDate.getMonth() + Number(term)));
    const currentDate = new Date(today);
    return getFormattedDate(targetDate) <= getFormattedDate(currentDate);
}

function solution(today, terms, privacies) {
    const answer = [];
    for (let i = 0; i < privacies.length; i++) {
        const cur = privacies[i].split(' ');
        for (let j = 0; j < terms.length; j++) {
            const term = terms[j].split(' ');
            if (cur[1] === term[0] && checkPrivacies(today, cur[0], term[1])) {
                answer.push(i + 1);
            }
        }
    }
    return answer;
}

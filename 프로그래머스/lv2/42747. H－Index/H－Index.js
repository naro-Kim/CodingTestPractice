const solution = (citations) => citations.sort((a, b) => b - a).filter((el, idx) => el >= idx + 1).length;

/**
#1. 각 논문들의 인용 횟수를 조사한다
#2. 연구자의 논문을 인용 횟수를 기준으로 내림차순 정렬한다 
#3. 인용횟수와 논문의 순서(Index)가 같거나 인용횟수가 더 높은 구간까지의 논문 편수를 구한다 

function solution(citations) {
    return citations.sort((a, b) => b-a) // Sort the citations array in descending order
    .map((citation, index) => Math.min(citation, index + 1)) // Calculate h-index for each element
    .reduce((maxHIndex, hIndex) => Math.max(maxHIndex, hIndex), 0); // Find the maximum h-index
}

*/
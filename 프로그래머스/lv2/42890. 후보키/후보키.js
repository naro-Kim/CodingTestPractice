function solution(relation) {
    const idxArr = Array.from({ length: relation[0].length }, (_, i) => i);
    let combinations = idxArr.flatMap((_, i) => getCombination(idxArr, i + 1));

     combinations = checkUniqueness(relation, combinations); 
     combinations = checkMinimality(combinations); 
    return combinations.length;
}

function checkUniqueness(relation, combinations) {
    return combinations.filter(combination => {
        const set = new Set(
            relation.map(rel => combination.map(combi => rel[combi]).join(','))
        );  
        return set.size === relation.length;
    });
}

function checkMinimality2(combinations) {
    const usedAttributes = new Set();
    return combinations.filter(combination => { 
        const hasUsedAttribute = combination.some(num => usedAttributes.has(num)); 
        if (!hasUsedAttribute) {
            combination.forEach(num => usedAttributes.add(num));
            return true;
        }
        return false;
    });
}
 
function checkMinimality(combinations){
    let results=[]; 
  
    while(combinations.length){
        results.push(combinations[0]);
        combinations=combinations.reduce((acc,cur)=>{
            let notMinimal=combinations[0].every(combination=>cur.includes(combination));
            
            console.log(notMinimal, acc, cur)
            if(!notMinimal) acc.push(cur); 
            return acc;
        },[])
    }
  
    return results;
    
}

function getCombination(arr, selectNum) {
    if (selectNum === 1) {
        return arr.map(a => [a]);
    }
    return arr.flatMap((fix, i, origin) => {
        const rest = origin.slice(i + 1);
        const combi = getCombination(rest, selectNum - 1);
        return combi.map(c => [fix, ...c]);
    });
}

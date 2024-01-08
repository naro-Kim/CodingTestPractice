const makeMat = (v, n, e) => { 
    const mat = Array.from({length: n}, ()=> new Array(n).fill(0));
    
    const graph = v.reduce((map, key, idx) => { 
    map.set(key, idx);
    return map;
}, new Map);
     
    for(const [a,b] of e){
        mat[graph.get(a)][graph.get(b)] = mat[graph.get(a)][graph.get(b)] + 1 || 1 ; //선물 주는 사람
    }
    return mat
}

const makeTable = (mat) => {
    const len = mat.length;
    const arr = [];

    for (let i = 0; i < len; i++) {
        let sumRows = mat[i].reduce((acc, cur) => acc + cur, 0); // sum of rows
        let sumCols = 0; 
        for (let j = 0; j < len; j++) {
            sumCols += mat[j][i]; // sum of columns
        }
        arr.push(sumRows - sumCols); // difference
    }

    return arr;
}

const getGift = (friends, mat, tb) => { 
    const len = friends.length;
    const giftArr = new Array(len).fill(0);
    for(let i=0; i<len; i++){  
        for(let j=0; j<len; j++){
            if(mat[i][j]){ 
                if(mat[i][j] > mat[j][i]){
                    giftArr[i]++;
                } else if(mat[i][j] == mat[j][i]){
                    if(tb[i] > tb[j]) giftArr[i]++;
                }    
            } else if (!mat[i][j] && !mat[j][i]) {           
                if(tb[i] > tb[j]) giftArr[i]++; 
            }
        } 
    }
    
    return Math.max(...giftArr);
}

const solution = (friends, gifts) => {
    let answer = 0;
    const len = friends.length;
    gifts = gifts.map((v)=> v.split(" "));
    const mat = makeMat(friends, friends.length, gifts);
    const tb = makeTable(mat); 
    answer = getGift(friends, mat, tb); 
    
    return answer;
}
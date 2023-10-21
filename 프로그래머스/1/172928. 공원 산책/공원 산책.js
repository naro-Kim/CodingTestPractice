function solution(park, routes) { 
    const dir = { W:[-1, 0],
             E:[1,0],
             S:[0,1],
             N:[0,-1]}
    let [x, y] = [0, 0];
    
    park = park.map((row, rowIdx) => {
        return row.split("").map((col, colIdx) => {
            if (col === "S") {
                [x, y] = [colIdx, rowIdx];
            }
            return col;
        });
    });
    
    while(routes.length > 0){
        const [op, n] = routes.shift().split(" ");
        let nx = x;
        let ny = y;
        let flag = false;
        
        for(let i=0; i<n; i++){
            if (op === "E") nx++;
            else if (op === "W") nx--;
            else if (op === "S") ny++;
            else if (op === "N") ny--;
            if(nx < 0 || nx >= park[0].length || ny < 0 || ny >= park.length || park[ny][nx] === 'X') { 
                flag = true; 
                break; 
            }
        }
        if(!flag){
            x = nx
            y = ny
        }
    }
    return [y, x]
}


function solution(n, s, a, b, fares) {
    INF = Number(1e7)
    let answer = INF;
    let graph = new Array(n).fill().map(_ => new Array(n).fill(Infinity));

    for (let i=0; i<n; i++) graph[i][i] = 0;

      fares.forEach(info => {
        const [c, d, f] = info;
        graph[c-1][d-1] = f;
        graph[d-1][c-1] = f;
      }); 
 
    for (let k=0; k<n; k++){
        for(let i=0; i<n; i++){
            for(let j=0; j<n; j++){
                graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
            }
        }
    }  
 
    for (let i=0; i<n; i++){
        cost = graph[s-1][i] + graph[i][a-1] + graph[i][b-1]
        answer = Math.min(answer, cost)
    }


    return answer;
}
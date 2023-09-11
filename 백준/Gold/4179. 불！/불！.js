/** Queue 자료구조 구현
 * js의 Object 객체는 key-value 형태로
 * key를 hash로 사용하여, O(1)의 시간을 써 key를 통해 value에 접근한다.
 * front와 rear는 포인터.
 * 포인터를 통해 Queue의 size를 구할 수 있다.
 * Queue의 메소드 로직은 데이터의 존재 유무로 구분한다.
*/

class Queue {
  constructor() {
    this.data = {}; // 데이터를 저장하는 객체
    this.front = 0; // 첫 번째 데이터를 가리키는 포인터
    this.rear = 0; // 마지막 데이터를 가리키는 포인터
  }
  
  size(){ 
      //rear가 가리키는 값이 없다면 데이터가 없다.
      if(this.data[this.rear] === undefined){ 
          return 0;
      }
      else return this.rear - this.front + 1;
  }
  
  push(value){
      if(this.size()===0){
          this.data[0] = value; 
      }
      else {
          this.rear += 1;
          this.data[this.rear] = value;
      }
  }
  
  popleft(){
      let tmp;
      if(this.front === this.rear){
          tmp = this.data[this.front];
          delete this.data[this.front];
          this.front = 0;
          this.rear = 0;
          return tmp
      } else {
          tmp = this.data[this.front];
          delete this.data[this.front];
          this.front += 1;
          return tmp;
      }
  }
}

// file I/O
const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')


function solution (){
    const [r,c] = input.shift().split(' ').map((v)=>+v);
    const graph = input.map((row)=> row.trim().split(''));  
    const map = Array.from({ length: r}, ()=> Array(c));
    const dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]; 
    let visited;
    
    const fireQ = new Queue();
    const q = new Queue(); 
    
    for(let i=0; i < r; i++){
        for(let j=0; j < c; j++){
            if(graph[i][j] === 'J'){
                q.push([i, j, 1]);
                map[i][j] = 0;
            } else if (graph[i][j] === 'F') {
                fireQ.push([i, j]);
                map[i][j] = 1;
            } else if (graph[i][j] === '#') {
                map[i][j] = -1;
            } else {
                map[i][j] = 0;
            }
        }
    }
    
    const fireBFS = () => {
        visited = Array.from({ length: r }, () => Array(c).fill(false)); 
        
        while (fireQ.size()) {
            const [x, y] = fireQ.popleft();
        
          for(const [dx, dy] of dir){
                const [nx, ny] = [x + dx, y + dy];  
        
                if (nx < 0 || ny < 0 || nx >= r || ny >= c) continue;
                if (map[nx][ny] !== 0 || visited[nx][ny]) continue;
        
                map[nx][ny] = map[x][y] + 1;
                visited[nx][ny] = true;
                fireQ.push([nx, ny]);
            }
        }
    }
    
    const bfs = () => {
        visited = Array.from({ length: r }, () => Array(c).fill(false));
        while(q.size()){
            const [x, y, cnt] = q.popleft();
            for(const [dx, dy] of dir){
                const [nx, ny] = [x + dx, y + dy];  
                
                if(nx < 0 || ny < 0 || nx >= r || ny >= c) {
                    console.log(cnt);
                    return;
                }
                if(map[nx][ny] !== 0 && map[nx][ny] <= cnt+1) continue;
                if(visited[nx][ny]) continue;
                if(map[nx][ny] === -1) continue;
                
                visited[nx][ny] = true;
                q.push([nx, ny, cnt+1]);
            }
        }
        console.log("IMPOSSIBLE")
    }
    
    fireBFS();
    bfs();
} 

solution()
 
const input = require("fs")
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split("\n");  
 
const n = Number(input.shift()); // 보드 크기
const k = Number(input.shift()); // 사과 개수

//사과 처리
const apples = input.slice(0, k).map(v => v.split(' ').map(Number));

// 방향 처리
const l = Number(input[k])
const dir = input.slice(k+1).map((el)=>{
    const [t, d] = el.split(' '); 
    return [+t, d ==='L' ? -1 : 1] 
});

// pos, dir init
const snake = [[0, 0]] // (0,0)에서 시작
const dx = [0, 1, 0, -1];
const dy = [1, 0, -1, 0];

// board init
const board = Array.from(new Array(n), ()=> new Array(n).fill(0)) 
board[0][0] = 1; // 시작지점 visited 처리

let curDir = 0; // 시작 시 꼬리는 (0,0)에서 우측 출발
let dirIndex = 0;
let tailIndex = 0;
let t = 0;

apples.forEach(([x, y]) => board[x-1][y-1] = 2);

// game loop
while(true){
    t++ //시간 증가

    
    const [x, y] = snake[snake.length -1]; 
    const nx = Number(x+dx[curDir]);
    const ny = Number(y+dy[curDir]); 
     
    // loop break condition
    if(nx < 0 || nx >= n || ny < 0 || ny >= n || board[nx][ny] === 1){
        break;
    }
    
    if(!board[nx][ny]){
        const [tx, ty] = snake[tailIndex];
        board[tx][ty] = 0; // 꼬리를 옮김  
        tailIndex++;
    }
    
    snake.push([nx, ny]);
    board[nx][ny] = 1;
    
    if( dirIndex < dir.length && t === dir[dirIndex][0]){
        curDir = (curDir + dir[dirIndex][1] + 4) % 4;
        dirIndex++;
    } 
}
  
console.log(t) 
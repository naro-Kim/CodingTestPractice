function solution(record) { 
    let m = new Map([])
    const msg = {in: "님이 들어왔습니다.", out: "님이 나갔습니다."}
    let ans = [];
    record.forEach((log)=>{
        const [inst, uid, nick] = log.split(' ')
        if(inst != 'Leave') m.set(uid, nick)
    })
    
    record.forEach((log)=>{
        const [inst, uid, nick] = log.split(' ') 
        switch(inst){
            case 'Enter':
                ans.push(m.get(uid) + msg.in)
                break;
            case 'Leave':
                ans.push(m.get(uid) + msg.out)
                break;
        }
    }) 
    return ans;
}

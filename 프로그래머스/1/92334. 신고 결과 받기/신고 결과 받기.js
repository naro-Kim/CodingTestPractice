function solution(id_list, report, k) {
    const ans = new Array(id_list.length).fill(0)      
    // create report data list for each id
    const user = id_list.reduce((acc, id)=> ({...acc, [id]:[]}),{});  
    
    // checking report and push data into Object
    report.forEach((c)=>{
        const [a, b] = c.split(" ");
        if(!user[b].includes(a)) user[b].push(a); // push data to send a mail to reporter 
    }) 
     
    for (const u in user) {
        if (user[u].length >= k) {
          user[u].forEach((item) => (ans[id_list.indexOf(item)] += 1));
        }
    }
    return ans
}
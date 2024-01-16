/*
* st맨 뒤 문자 !== 다음 문자
- st = [b]
char = a

[b, a]

st [b, a]
char = a
pop! [b]

st [b]
char = b

st [0]
s = [a, a]



-
*/

const solution = (s) => {
    let answer = 0;  
    let st = [s[0]]
    s = s.slice(1) 
    
    for(const char of s){
        st.push(char) 
        if(st[st.length-1] === st[st.length-2]) {
            st.pop();
            st.pop();
        }
    }  
    
    return st.length === 0 ? 1 : 0;
}
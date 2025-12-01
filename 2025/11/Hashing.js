const fs = require('fs')

const input = fs.readFileSync(0).toString().split('\n')

const L = parseInt(input[0])
const string = input[1]
const r = 31
const M = 1234567891
const alphabet = {
    a:1,b:2,c:3,d:4,e:5,f:6,g:7,h:8,i:9,j:10,k:11,l:12,m:13
    ,n:14,o:15,p:16,q:17,r:18,s:19,t:20,u:21,v:22,w:23,x:24,y:25,z:26
}
const rmodM = [1]
let a = 1
for (let i=1; i<50; i++){
    a *= r
    a %= M
    rmodM.push(a)
}
let result = 0

for (let i=0; i<L; i++){
    result += alphabet[string[i]] * rmodM[i]
    result %= M
}

console.log(result)

// 아스키코드로 번호 배열 만들기
const arr = {}
for (let i=0; i<26; i++){
    arr[String.fromCharCode(97+i)] = i+1
}
// GPT 로 다듬은 버전
// const [L, str] = fs.readFileSync(0).toString().trim().split('\n');

// const R = 31;
// const M = 1234567891;

// let power = 1;
// let hash = 0;

// for (let i = 0; i < Number(L); i++) {
//   const value = str.charCodeAt(i) - 96; // 'a' = 97 → 1
//   hash = (hash + value * power) % M;
//   power = (power * R) % M;
// }

// console.log(hash);
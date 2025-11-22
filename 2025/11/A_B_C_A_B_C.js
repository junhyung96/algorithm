const fs = require('fs')

const [A, B, C] = fs.readFileSync(0).toString().split('\n')

// A,B,C 를 숫자로 생각했을 때 A+B-C
console.log(Number(A) + Number(B) - Number(C))

// A,B,C 를 문자로 생각했을 때 A+B-C
console.log(A+B-C)
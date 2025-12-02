const fs = require('fs')

const input = fs.readFileSync(0).toString().split('\n')

let i = 0
let result = ''
while (true){
    let num = input[i]
    i++
    let answer = 'no'

    if (num === '0') break;

    let flag = true;
    for (let j=0; j<Math.floor(num.length/2); j++){
        if (num[j] !== num[num.length-1-j]) {
            flag = false
            break
        }
    }

    if (flag) {
        answer = 'yes'
    }
    result += answer + '\n'
}

console.log(result)
const fs = require('fs')

const input = fs.readFileSync(0).toString().trim()

let w = 1
let value = 0

let i = -1
for (const num of input){
    i++
    if (num === '*'){
        if (i % 2 === 1){
            w = 3;
        }
        continue
    }
    if (i % 2 === 1){
        value += parseInt(num) * 3
    } else {
        value += parseInt(num) * 1
    }
}

let result = 0;
if (w === 1){
    result = 10 - value % 10
} else {
    for (let i=0; i<10; i++){
        if ((value + 3*i) % 10 === 0){
            result = i
            break
        }
    }
}
console.log(result)
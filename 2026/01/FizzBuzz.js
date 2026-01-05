const fs = require('fs')

const input = fs.readFileSync(0).toString().trim().split('\n')

let num;
if (input[0][0] !==  'F' && input[0][0] !== 'B') {
    num = Number(input[0]) + 3
}
if (input[1][0] !==  'F' && input[1][0] !== 'B') {
    num = Number(input[1]) + 2
}
if (input[2][0] !==  'F' && input[2][0] !== 'B') {
    num = Number(input[2]) + 1
}
if (num % 15 === 0) {
    console.log('FizzBuzz')
} else if (num % 3 === 0) {
    console.log('Fizz')
} else if (num % 5 === 0) {
    console.log('Buzz')
} else {
    console.log(num)
}
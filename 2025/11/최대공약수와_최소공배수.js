// 최대공약수. 최대공배수
// 소인수분해
// 소수를 알아야하고
// 소인수분해해서 교집합 = 최대공약수
// 합집합 = 최소공배수

const fs = require('fs')
let [A, B] = fs.readFileSync(0).toString().split(' ').map(Number)
// A > B 가 되도록
if (A < B){
    [A, B] = [B, A]
}
let gcd = 1;
let lcm = 0;

let [a, b] = [A, B]
while (true){
    if (a % b === 0) {
        gcd = b
        break
    }
    let r = a%b
    a = b
    b = r
}
lcm = Math.floor((A*B)/gcd)
console.log(gcd + '\n' + lcm)

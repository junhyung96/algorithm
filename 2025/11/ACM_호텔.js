// 방 배정
// H 높이 W 너비 N 번째 사람은 어디에?
// 왼쪽 끝에 엘레베이터가 있고
// 층 상관없이 엘레베이터로부터 가까운 방을 선호
// 같은 거리라면 아래층을 선호
// YYXX 호 YY 층 XX 엘레베이터로부터 방을 세었을 때 번호
// 101 호, 201 호 .... 순으로 배정
// 1201 호는 102 호 보다 선호됨
// 101 호는 201호 보다 선호됨

const fs = require('fs')

const input = fs.readFileSync(0).toString().split('\n')
const T = parseInt(input[0])

result = ""

for (let i=1; i<=T; i++){
    let [H, W, N] = input[i].split(" ").map(Number)
    let floor = N % H
    let dist = 0;
    if (N%H) {
        dist = parseInt(N / H) + 1
    } else {
        floor = H
        dist = parseInt(N / H)
    }
    if (dist < 10) {
        result += floor + "0" + dist + "\n"
    } else {
        result += floor + "" + dist + "\n"
    }
}

console.log(result)
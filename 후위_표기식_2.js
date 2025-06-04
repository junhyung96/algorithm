// 풀이 날짜 및 소요 시간
// YYYY-MM-DD HH:MM ~ HH:MM

// 문제 요약

// 입력 예제

// 입력 범위 및 조건

// 풀이 방법 및 시간, 공간복잡도 계산

// 코드 작성
const fs = require("fs");

input = fs.readFileSync(0).toString().trim().split('\n');
// N = fs.readFileSync('/dev/stdin').toString().trim(); // 백준 제출용
print = console.log

N = Number(input[0]);
postfix = input[1]
num_map = {}

for (i=2; i<N+2; i++){
    num_map[String.fromCharCode(65+i-2)] = Number(input[i])
}

stack = Array()
for (i=0; i<postfix.length; i++){
    value = postfix[i]
    if (value !== '+' && value !== '-' && value !== '*' && value !== '/') {
        stack.push(num_map[value])
    } else {
        numB = stack.pop()
        numA = stack.pop()
        value === '+' ? stack.push(numA + numB) :
        value === '-' ? stack.push(numA - numB) :
        value === '*' ? stack.push(numA * numB) :
        stack.push(numA / numB)
    }
}

print(stack[0].toFixed(2))
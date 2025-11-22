// 풀이 날짜
// 2025-11-15

// 문제 요약
// 컴퓨터 제조회사 KOI 는 각 컴퓨터에 6자리 고유번호를 매긴다
// 00000 ~ 99999 까지의 수 중 하나 + 6번째 자리 고유수
// 고유수는 고유번호 처음 5자리의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지

// 입력 예제
// 0 4 2 5 6
// ans : 1

// 입력 범위 및 조건

// 풀이 방법 및 시간, 공간복잡도 계산
// 고유번호 앞 5자리 입력받아서 각각 제곱해서 더한 후 10으로 나눈 나머지 출력

// 코드 작성

const fs = require('fs')

let nums = fs.readFileSync(0).toString().trim().split(" ").map(Number)
let answer = 0;

nums.forEach((num) => 
    answer += num * num
)

console.log(answer % 10)

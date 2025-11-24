const fs = require("fs");

const input = fs.readFileSync(0).toString().split("\n");

const N = parseInt(input[0]);
let arr = input[1].split(" ").map(Number);
let [T, P] = input[2].split(" ").map(Number);

let res1 = 0;
let res2 = Math.floor(N / P) + " " + (N % P);
arr.forEach((item) => {
  if (item !== 0) {
    res1 += Math.floor((item - 1) / T) + 1;
  }
});

console.log(res1 + "\n" + res2);

// 몫을 구하기
// parseInt 는 문자열 파싱용 함수
parseInt(4.9); // 4  (버림처럼 보임)
parseInt("10.9") // 10
parseInt("10px") // 10
parseInt("08", 10) // 8
parseInt(0.0000004)  // 4  (원하는 결과가 아님!)
//내부적으로 숫자를 문자열로 바꿔서 "4e-7" → parseInt("4e-7") → 4

// 숫자용 API 사용을 권장
// 양수일 때, Math.floor 올림
Math.floor(10 / 3); // 3
// Math.trunc 버림
Math.trunc(10 / 3); // 3
Math.trunc(-10 / 3); // -3
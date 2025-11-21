const fs = require("fs");

const input = fs.readFileSync(0).toString().split("\n");
const T = parseInt(input[0]);
let quiz = "";
let point = 0;
let total_point = 0;

let result = "";
for (let i = 1; i <= T; i++) {
  quiz = input[i];
  total_point = 0;
  point = 0;

  for (let j = 0; j < quiz.length; j++) {
    if (quiz[j] === "O") {
      point += 1;
    } else {
      point = 0;
    }
    total_point += point;
  }

  result += total_point + "\n";
}

console.log(result);

// 문자열 - for 문을 사용하는 방법

// 전통 for문
// for (let j = 0; j < quiz.legnth; j++)

// GPT - JS 스러운 방법
// for (const ch of quiz)

// 인덱스가 필요할 때 - 비싼 방법이다.
// for ( const [i, ch] of [...quiz].entries())

// forEach 는 배열로 바꿔야 쓸 수 있음
// [...quiz].forEach(ch => {}) 비추천
// quiz.split("").forEach(ch => {}) 메모리낭비

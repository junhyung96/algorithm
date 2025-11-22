const fs = require("fs");

const input = fs.readFileSync(0).toString().split("\n");

let result = "";
let isRight;
let i = 0;
while (true) {
  isRight = "wrong";
  let [a, b, c] = input[i].split(" ").map(Number);
  if (a === 0 && b === 0 && c === 0) {
    break;
  }
  // bubble sort
  if (a > b) {
    [a, b] = [b, a];
  }
  if (b > c) {
    [b, c] = [c, b];
  }
  if (a > b) {
    [a, b] = [b, a];
  }
  if (c * c === a * a + b * b) {
    isRight = "right";
  }
  result += isRight + "\n";
  i++;
}
console.log(result);

// sort
arr = [10, 2, 5]
// 기본 유니코드 순 
arr.sort() // "10", "2", "5" 순이 됨
// 숫자 정렬
arr.sort((a, b) => a - b) // 오름차순
arr.sort((a, b) => b - a) // 내림차순
// 원본 배열 유지
const sorted = [...arr].sort((a, b) => a - b)

// 변수 스왑
// 구조 분해 할당 ES6
[a, b] = [b, a] 
// 임시 변수 temp
let tmp = a;
a = b;
b = tmp;
// XOR 스왑 ( 정수만 가능 )
a = a ^ b;
b = a ^ b;
a = a ^ b;
// 덧셈 뺄셈 스왑 ( 오버플로 위험 )
a = a + b;
b = a - b;
a = a - b;
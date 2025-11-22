const fs = require("fs");

const [A, B, C] = fs.readFileSync(0).toString().split("\n").map(Number);

calculated_num = A * B * C + "";
let arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

for (let i = 0; i < 10; i++) {
  arr[parseInt(calculated_num[i])]++;
}

let result = "";
for (let i = 0; i < 10; i++) {
  result += arr[i] + "\n";
}

console.log(result);

// JS 배열 생성
const array1 = [];
const array2 = Array(10); // 길이 10, 값 empty
const array3 = Array.from({ length: 10 }, () => 0); // 길이 10, 값 0 으로 채움
const array4 = new Array(5); // 잘 사용하지 않음 array2 와 동일
// 2차원 배열 생성
const matrix = Array.from({ length: N }, () => Array(M).fill(0));

// Array.from
// Array.from(x)는 x가 아래 조건을 만족하면 배열로 변환
// - x.length가 숫자일 것 (number coercible)
// - x[i] 형태로 접근이 가능할 것 (array-like)
// { 0: 'a', 1: 'b', length: 2 } 와 같이 생긴 객체는 "유사 배열 객체" 로 인정
// Array.from({ length: 10 })
// → [undefined, undefined, undefined, ...]  // 총 10개
// 이 경우 실제 값이 없기 때문에 map 등으로 순회할 수 없음

// 풀이 날짜 및 소요 시간
// 2025-05-03 00:02 ~ HH:MM

// 문제 요약
// N 개의 수로 이루어진 수열에서
// (i, j) 구간의 합이 M 이 되는 경우의 수를 출력하라

// 입력 예제
// 4 2
// 1 1 1 1
// ans: 3

// 입력 범위 및 조건
// 0.5 sec 128MB
// N 1 ~ 10,000
// M 1 ~ 300,000,000

// 풀이 방법 및 시간, 공간복잡도 계산
// 모든 경우의 수를 탐색하기
// 배열 길이 10,000
// 누적합 구하기 -> 누적합 배열 O(1)
// 모든 경우의 수 : 연속된 구간.. sum(1~10000) = 50000000
// 0.5 초 꽉 채울듯..

// 코드 작성
const fs = require("fs");
print = console.log;

// input = fs.readFileSync(0).toString().trim().split("\n");
input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");
[N, M] = input[0].split(" ").map(Number);
arr = input[1].split(" ").map(Number);

psum = Array(N).fill(0);
arr.map((value, index) => {
  psum[index] = value;
  if (index > 0) {
    psum[index] += psum[index - 1];
  }
});

output = 0;

for (i = 0; i < N; i++) {
  if (psum[i] == M) {
    output += 1;
  }
  for (j = 0; j < i; j++) {
    if (psum[i] - psum[j] === M) {
      output += 1;
    }
  }
}

print(output);

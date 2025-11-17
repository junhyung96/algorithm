const fs = require('fs')

const input = Number(fs.readFileSync(0).toString().trim())

let result = ""
for (let i=1; i<=input; i++){
    result += i + "\n"
}

console.log(result)

// 빠른 코드 68ms 메모리사용량은 더 많음
// gpt 답변
// 1. var 때문에 V8이 str 변수를 별도의 최적화 없이 
// 단순 스트링 누적용으로 처리하는 경향이 있음.
// 2. Linux 환경에서는 /dev/stdin이 캐시로 인해 더 빠를 수 있다.
// 3. trim() 사용으로 인한 추가 비용
// 적용
// 1. var 바꿔도 빨라지지 않음
// 2. /dev/stdin 해도 빨라지지 않음
// 3. trim 지워도 빨라지지 않음
// 4. parseInt 변경해도 빨라지지 않음
// 앞선 코드는 8년전 제출된 코드
// 현재 서버 상황이 다른 것으로 추측
// 결론 :
// let 사용 - var 는 스코프 오류 유발 가능성이 있다
// 추가 
// process.stdout.write 사용 - 메모리 적게 쓰고 속도가 빠름

// ✔ 왜 console.log가 느린가?

// 내부적으로 개행 자동 추가
// 디버그용 작업(형식 문자열 처리, 타입 검사 등)
// stdout 버퍼에 안전하게 동기 flush
// UTF-8 처리 강화로 과거보다 더 느려짐
// 샌드박스 환경(Docker)에서 console.log는 더 느림

// ✔ stdout.write는 어떤가?

// 아주 얇은 wrapper → 실제로는 OS의 write() 호출에 더 가까움
// 데이터 포맷 검사 없음
// 개행도 직접 넣어야 해서 오히려 부담 ↓

// var fs = require('fs');
// var input = fs.readFileSync('/dev/stdin').toString();
// var a = parseInt(input);
// var str ="";
// for(var i=1;i<=a;i++){
// 	str += i+"\n";
// }
// console.log(str);
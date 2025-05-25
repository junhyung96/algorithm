# 풀이 날짜 및 소요 시간
# 2025-05-23 13:55 ~ HH:MM

# 문제 요약
# 전체 페이지 수가 N 인 책에서
# 각 숫자는 전체 페이지 번호에서 몇 번 나오는가
# 첫페이지는 1, 마지막 페이지는 N

# 입력 예제
# 11 # 1 4 1 1 1 1 1 1 1 1

# 입력 범위 및 조건
# N 1 ~ 1,000,000,000

# 풀이 방법 및 시간, 공간복잡도 계산
# 0 1 2 3 4 5 6 7 8 9
# 17 일때
# 1의 자리수 1바퀴 + 1~7
# 10의 자리수 10 ~ 17

# 118
# 1 = 1 11 21 31 41 51 61 71 81 91 101 111  16개
#   =   10 12 13 14 15 16 17 18 19          9개
#   =   100 102 103 104 105 106 107 108 109 110 11개
#   =   112 113 114 115 116 117 118 14 
# 1 의 출현 
# 1의 자리에서 11 번 반복 + 1 => 12개
# 10의 자리에서 1번 반복 + 10~18(9) => 19개
# 100의 자리에서 0번 반복 + 100~118(19개) => 19개
# 50개
# 2의 출현
# 1의 자리에서 11번 반복 + 1
# 10의 자리에서 1번 반복 + x
# 100의 자리에서 0번 반복 + x 

# 59538 일때
# 0 의 출현 횟수
# 1의 자리. 5953번 + ( 8 > 0 ? 1 : 0 )
# 10의 자리. 

# 코드 작성
import sys
_input = sys.stdin.readline
def minput(): return map(int, _input().split())

N = int(_input())

cnts = []

# 0 에 대한 처리
i = 0
num = N
power_of_ten = 1
sub_cnt = 0
r = 0
# print("when ", i)
# 각 자리수마다 몇번 등장하는지를 체크
while num > 0:
    if num < 10:
        break
    # 현제 자리에서 자신의 자리수보다 큰 자리 수에 의해 반복되는 횟수
    sub_cnt += ((num // 10)-1) * power_of_ten
    remain = num % 10
    r += remain * power_of_ten
    # print("upside", sub_cnt, r, power_of_ten)
    # 현재 자리수가 탐색하는 숫자보다 큰지 같은지
    # 크다면 현재 자리수에 해당하는 모든 수
    # 예를 들면 i = 3, power_of_ten = 100, 300 ~ 399 에 해당하는 3이 들어간 모든 횟수
    if remain > i:
        sub_cnt += power_of_ten
    else:
        sub_cnt += r + 1

    # print("downside", sub_cnt, r)
    num //= 10
    power_of_ten *= 10

cnts.append(sub_cnt)

for i in range(1, 10):
    num = N
    power_of_ten = 1
    sub_cnt = 0
    r = 0
    # print("when ", i)
    # 각 자리수마다 몇번 등장하는지를 체크
    while num > 0:
        # 현제 자리에서 자신의 자리수보다 큰 자리 수에 의해 반복되는 횟수
        sub_cnt += (num // 10) * power_of_ten
        remain = num % 10
        r += remain * power_of_ten
        # print("upside", sub_cnt)
        # 현재 자리수가 탐색하는 숫자보다 큰지 같은지
        # 크다면 현재 자리수에 해당하는 모든 수
        # 예를 들면 i = 3, power_of_ten = 100, 300 ~ 399 에 해당하는 3이 들어간 모든 횟수
        if remain > i:
            sub_cnt += power_of_ten
        elif remain == i:
            sub_cnt += r - i*power_of_ten + 1

        # print("downside", sub_cnt, r)
        num //= 10
        power_of_ten *= 10

    
    cnts.append(sub_cnt)
print(" ".join(map(str, cnts)))

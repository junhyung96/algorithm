# 풀이 날짜 및 소요 시간
# 2025-05-24 18:42 ~ HH:MM

# 문제 요약
# 기어 두개 맞물리게 하는 최소길이

# 입력 예제
# 2112112112
# 2212112

# 입력 범위 및 조건
# 2초 128MB

# 풀이 방법 및 시간, 공간복잡도 계산
# 

# 코드 작성
import sys
_input = sys.stdin.readline
def minput(): return map(int, _input().split())

gear_b = list(map(int, _input().rstrip()))
gear_t = list(map(int, _input().rstrip()))

if len(gear_b) < len(gear_t):
    gear_b, gear_t = gear_t, gear_b

len_b = len(gear_b)
len_t = len(gear_t)
result = len_b + len_t

s = -len_t + 1

x = 0
while True:
    is_possible = True

    for i in range(len_t):
        if s + i < 0 or s+i >= len_b:
            continue
        if gear_t[i] == 2 and gear_b[s+i] == 2:
            is_possible = False

    # print(s, is_possible, s+i)
    if is_possible:
        if s < 0 :
            result = min(result, len_b + (-s))
        else:
            if s + i >= len_b:
                result = min(result, s+i+1)
            else:
                result = min(result, len_b)
    
    s += 1
    if s >= len_b:
        break

print(result)
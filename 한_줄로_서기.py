# 풀이 날짜 및 소요 시간
# 2025-05-23 16:17 ~ HH:MM

# 문제 요약
# N 명 줄세우기
# 키가 1 부터 N 까지 모두 다른 N 명이 줄을 서야한다
# 자신의 왼쪽에 자기보다 키가 큰 사람이 몇명이 있는지 주어질 때
# 어떻게 줄을 서야하는지 출력하라

# 입력 예제
# 4
# 2 1 1 0

# 입력 범위 및 조건
# N 1 ~ 10
# 2초 128MB

# 풀이 방법 및 시간, 공간복잡도 계산
# 자기보다 큰 사람이 적은 사람이 앞으로
# 자기보다 큰 사람이 많을 수록 오른쪽으로
# 1의 위치는 확정임 제일 키가 작기 때문에
# N의 위치도 확정임 제일 키가 크기 때문에

# 코드 작성
import sys
_input = sys.stdin.readline
def minput(): return map(int, _input().split())

N = int(_input())
arr = [0] + list(minput())

line = [11] * N
line[arr[1]] = 1

for i in range(2, N+1):
    cnt = 0
    idx = -1
    while True:
        idx += 1
        if line[idx] > i:
            if cnt == arr[i]:
                break
            cnt += 1
        else:
            continue

    line[idx] = i

print(" ".join(map(str, line)))
    
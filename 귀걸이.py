# 풀이 날짜 및 소요 시간
# 2025-05-31 HH:MM ~ HH:MM

# 문제 요약

# 입력 예제

# 입력 범위 및 조건

# 풀이 방법 및 시간, 공간복잡도 계산

# 코드 작성
import sys
_input = sys.stdin.readline
def minput(): return map(int, _input().split())

scenario = 0

while True:
    scenario += 1
    N = int(_input())

    if N == 0:
        break

    students = []
    for _ in range(N):
        students.append(_input().rstrip())
    
    items = {}
    for _ in range(2*N-1):
        num, symbol = _input().rstrip().split()

        if items.get(num):
            if items[num][0] != symbol:
                items[num][1] -= 1
                if items[num][1] == 0:
                    del items[num]
            else:
                items[num][1] += 1
        else:
            items[num] = [symbol, 1]

    for item in items:
        print(scenario, students[int(item)-1])


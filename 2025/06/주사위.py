# 풀이 날짜 및 소요 시간
# 2025-05-13 08:40 ~ HH:MM

# 문제 요약
# 1 x 1 x 1 주사위 각 면의 숫자가 주어짐
# n x n x n 주사위를 만들어 바닥에 놓았을 때 보이는 수의 합의 최소값

# 입력 예제
# 2
# 1 2 3 4 5 6
# ans : 36

# 입력 범위 및 조건
# n 1 ~ 1,000,000

# 풀이 방법 및 시간, 공간복잡도 계산
# n x n x n 주사위
# k 면이 노출되는 주사위 개수
# 1면 : 윗면 ( n - 2 ) ^ 2 개 + 옆면 4 * ( ( n - 2 ) ^ 2 + ( n - 2) )
# 2면 : 모서리 (n-2) * 8 + 하단 꼭지점 4개
# 3면 : 상단 꼭지점 4개
# 합 : 5n^2

# 코드 작성
import sys
_input = sys.stdin.readline
def minput(): return map(int, _input().split())

N = int(_input())
dice = list(minput())
dice.sort()
one_face = dice[0]
two_face = dice[0] + dice[1]
three_face = dice[0] + dice[1] + dice[2]

if N == 1:
    print(sum(dice) - dice[5])
else:
    answer = 0
    answer += one_face * ( (N-2)**2 + 4*((N-2)**2 + N-2) )
    answer += two_face * ( (N-2)*8 + 4)
    answer += three_face * 4
    print(answer)
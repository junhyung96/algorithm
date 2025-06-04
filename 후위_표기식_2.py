# 풀이 날짜 및 소요 시간
# YYYY-MM-DD HH:MM ~ HH:MM

# 문제 요약

# 입력 예제

# 입력 범위 및 조건

# 풀이 방법 및 시간, 공간복잡도 계산

# 코드 작성
import sys
_input = sys.stdin.readline
def minput(): return map(int, _input().split())

N = int(_input())
postfix = _input().rstrip()
num_map = {}
for i in range(N):
    num_map[chr(65+i)] = int(_input())

stack = []
for value in postfix:
    if value in '+-*/':
        b = stack.pop()
        a = stack.pop()
        if value == '+':
            stack.append(a+b)
        elif value == '-':
            stack.append(a-b)
        elif value == '*':
            stack.append(a*b)
        else:
            stack.append(a/b)
        
    else:
        stack.append(num_map[value])
        
print(f"{stack[0]:.2f}")
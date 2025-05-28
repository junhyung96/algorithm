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
output = 10**9

def dfs(cur, d, cost, first):
    global output
    print(cur, cost, d)
    if cost > output:
        return 
    
    if d == N:
        if adj_matrix[cur][first] == 0:
            return
        output = min(output, cost + adj_matrix[cur][first])
        
    for nxt in range(N):
        if visited[nxt]:
            continue
        if adj_matrix[cur][nxt] == 0:
            continue
        visited[nxt] = True
        dfs(nxt, d+1, cost+adj_matrix[cur][nxt], first)
        visited[nxt] = False
        
adj_matrix = tuple(tuple(minput()) for _ in range(N))
visited = [False] * N
for i in range(N):
    visited[i] = True
    dfs(i, 1, 0, i)
    visited[i] = False

print(output)
# stack = []
# for i in range(N):

#     stack.append([i, 0, 0])
#     visited = [False] * N
#     visited[i] = True

#     while stack:
#         # print(stack)
#         cur, vi, cost = stack[-1]
#         stack[-1][1] += 1
        
#         if vi >= N:
#             node, nxt, cost = stack.pop()
#             visited[node] = False
#             continue
        
#         if visited[vi]:
#             continue
        
#         if not adj_matrix[cur][vi]:
#             continue
        
#         if cost + adj_matrix[cur][vi] > output:
#             continue
        
#         visited[vi] = True
#         stack.append([vi, 0, cost+adj_matrix[cur][vi]])
        
#         if len(stack) == N:
#             start = stack[0]
#             end = stack[-1]
#             total_cost = end[2] + adj_matrix[end[0]][start[0]]
#             if total_cost < output:
#                 output = total_cost

# print(output)
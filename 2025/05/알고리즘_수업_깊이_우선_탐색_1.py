# 풀이 날짜 및 소요 시간
# 2025-05-17 11:25 ~ HH:MM

# 문제 요약

# 입력 예제

# 입력 범위 및 조건

# 풀이 방법 및 시간, 공간복잡도 계산

# 코드 작성
import sys
_input = sys.stdin.readline
def minput(): return map(int, _input().split())

def dfs(n, s):
    time = 1
    stack = [[s, 0]]
    visited[s] = time
    time += 1
    
    while stack:
        cur, id = stack[-1]
        
        if id < len(adj_ls[cur]):
            nxt = adj_ls[cur][id]
            stack[-1][1] += 1
            
            if visited[nxt]:
                continue
            
            stack.append([nxt, 0])
            visited[nxt] = time
            time += 1
            
        else:
            stack.pop()

N, M, R = minput()
adj_ls = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = minput()
    adj_ls[a].append(b)
    adj_ls[b].append(a)

# 오름차순으로 방문
for ls in adj_ls:
    ls.sort()
    
dfs(N, R)
output = []
for time in visited[1:]:
    output.append(str(time))
print("\n".join(output))
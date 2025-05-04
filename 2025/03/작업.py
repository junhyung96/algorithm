import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N, M = minput()
adj_ls = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = minput()
    adj_ls[b].append(a)
    
visited = [False]*(N+1)
q = deque()
q.append(int(input_()))
result = 0

while q:
    now = q.popleft()
    for nxt in adj_ls[now]:
        if not visited[nxt]:
            visited[nxt] = True
            result += 1
            q.append(nxt)
    
print(result)
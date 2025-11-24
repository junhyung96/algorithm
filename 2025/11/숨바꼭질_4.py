import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
MAX_N = 100_001

q = deque()
visited = [False] * MAX_N
prev = [0] * MAX_N
q.append((N, 0))
visited[N] = True
prev[N] = N

result = ""
while q:
    now, time = q.popleft()
    
    if now == K:
        result += str(time) + '\n'
        break
    
    if now-1 >= 0 and not visited[now-1]:
        q.append((now-1, time+1))
        visited[now-1] = True
        prev[now-1] = now
    if now+1 <= 100_000 and not visited[now+1]:
        q.append((now+1, time+1))
        visited[now+1] = True
        prev[now+1] = now
    if now*2 <= 100_000 and not visited[now*2]:
        q.append((now*2, time+1))
        visited[now*2] = True
        prev[now*2] = now

path_history = str(K)
cur = K
while True:
    if cur == N:
        break
    path_history = str(prev[cur]) + " " + path_history
    cur = prev[cur]
print(result + path_history)
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
q = deque()
visited = [False] * 100_001
q.append((N, 0))
visited[N] = True

while q:
    now, time = q.popleft()
    
    if now == K:
        print(time)
        break
    
    if now-1 >= 0 and not visited[now-1]:
        q.append((now-1, time+1))
        visited[now-1] = True
    if now+1 <= 100_000 and not visited[now+1]:
        q.append((now+1, time+1))
        visited[now+1] = True
    if now*2 <= 100_000 and not visited[now*2]:
        q.append((now*2, time+1))
        visited[now*2] = True
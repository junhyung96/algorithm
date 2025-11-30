import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

F, S, G, U, D = map(int, input().split())

q = deque()
visited = [-1] * 1_000_001

result = 'use the stairs'

q.append((S, 0))
visited[S] = 0

while q:
    floor, time = q.popleft()
    up = floor + U
    down = floor - D
    if up <= F:
        if visited[up] == -1:
            q.append((up, time+1))
            visited[up] = time+1
    if down > 0:
        if visited[down] == -1:
            q.append((down, time+1))
            visited[down] = time+1
    

if visited[G] == -1:
    print(result)
else:
    print(str(visited[G]))
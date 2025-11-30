import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

T = int(input().rstrip())

result = []

# '.': 빈 공간
# '#': 벽
# '@': 상근이의 시작 위치
# '*': 불
delta = ((0,1),(1,0),(0,-1),(-1,0))
for tc in range(T):
    w, h = map(int, input().split())
    graph = [input().rstrip() for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    answer = "IMPOSSIBLE"
    q = deque()
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                q.appendleft([i, j, 0, 0]) # x, y, time, type(0: fire, 1:player)
                visited[i][j] = True
            elif graph[i][j] == '@':
                q.append([i, j, 0, 1])
                visited[i][j] = True
                
    flag = False
    while q: 
        x, y, time, epyt = q.popleft()
        
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                if epyt == 1:
                    flag = True
                    answer = str(time+1)
                    break
                continue
            if graph[nx][ny] == '#':
                continue
            if visited[nx][ny]:
                continue
            q.append([nx, ny, time+1, epyt])
            visited[nx][ny] = True
        
        if flag:
            break
    result.append(answer)
    
print("\n".join(result))
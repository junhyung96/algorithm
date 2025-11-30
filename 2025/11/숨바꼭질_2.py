import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().split())

max_N = 100_000
q = deque()
visited = [0] * (max_N+1)
q.append((N, 0)) # 위치, 시간
visited[N] = 1
arrived_time = [0] * (max_N+1)

while q:
    cur, time = q.popleft()
    if cur+1 <= max_N:
        if visited[cur+1]:
            if arrived_time[cur+1] == time+1:
                visited[cur+1] += visited[cur]
        else:
            visited[cur+1] = visited[cur]
            arrived_time[cur+1] = time+1
            q.append((cur+1, time+1))
    if cur-1 >= 0:
        if visited[cur-1]:
            if arrived_time[cur-1] == time+1:
                visited[cur-1] += visited[cur]
        else:
            visited[cur-1] = visited[cur]
            arrived_time[cur-1] = time+1
            q.append((cur-1, time+1))
    if cur*2 <= max_N:
        if visited[cur*2]:
            if arrived_time[cur*2] == time+1:
                visited[cur*2] += visited[cur]
        else:
            visited[cur*2] = visited[cur]
            arrived_time[cur*2] = time+1
            q.append((cur*2, time+1))


print(str(arrived_time[K]) + "\n" + str(visited[K]))
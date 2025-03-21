# NxM 크기의 미로
# 0 빈방 1 벽
# 1, 1 위치에서 N, M 으로 이동하려면 최소 벽을 몇개 부숴야 하는가

# 위치를 우선순위 큐에 저장. 파이썬 heapq 이용
# 델타탐색으로 이동하면서
# 벽을 만나면 벽을 만난 횟수 1 을 올리고 해당 장소로 이동
# 우선순위 큐에서는 벽을 만난 횟수가 작을 것을 계속해서 뽑아 다음 장소로 이동
# N, M 에 도달하면 벽을 만난 횟수 출력

import sys, heapq
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

h = [] # [벽 만난 횟수, x좌표, y좌표]
M, N = minput()
graph = [list(map(int, input_().rstrip())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
delta_search = [[0, 1], [1, 0], [0, -1], [-1, 0]]
heapq.heappush(h, [0, 0, 0])
visited[0][0] = True

while h:
    wall, x, y = heapq.heappop(h)

    for dx, dy in delta_search:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if visited[nx][ny]:
            continue
        visited[nx][ny] = True
        if graph[nx][ny]:
            heapq.heappush(h, [wall+1, nx, ny])
        else:
            heapq.heappush(h, [wall, nx, ny])
    
    if x == N-1 and y == M-1:
        print(wall)
        break
        
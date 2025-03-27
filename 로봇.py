import sys
from collections import deque
def minput(): return map(int, sys.stdin.readline().split())
INF = int(1e9)
M, N = minput()
graph = [list(minput()) for _ in range(M)]
sx, sy, sd = minput()
sx -= 1
sy -= 1
tx, ty, td = minput()
tx -= 1
ty -= 1
# 동서남북 => 1234
# 동
delta_search = [ # 저장방식 [dx, dy, 방향전환횟수, 회전 후 방향]
    [],
    [[0, 1, 0, 1], [1, 0, 1, 3], [-1, 0, 1, 4], [0, -1, 2, 2]], # 동 : 현재 방향
    [[0, -1, 0, 2], [1, 0, 1, 3], [-1, 0, 1, 4], [0, 1, 2, 1]], # 서
    [[1, 0, 0, 3], [0, -1, 1, 2], [0, 1, 1, 1], [-1, 0, 2, 4]], # 남
    [[-1, 0, 0, 4], [0, -1, 1, 2], [0, 1, 1, 1], [1, 0, 2, 3]], # 북
]

q = deque()
visited = [[[INF, INF, INF, INF, INF] for _ in range(N)] for _ in range(M)] # [도착했을떄 order 수, 동, 서, 남, 북]

q.append([sx, sy, sd, 0, 0]) # x, y, d, order_count, dist_count
visited[sx][sy][0] = 0

def update_vistied(x, y, d, o):
    for dx, dy, do, dd in delta_search[d]:
        visited[x][y][dd] = min(visited[x][y][dd], o + do)

def find_min_order(x, y, d, o):
    for dx, dy, do, dd in delta_search[d]:
        if visited[x][y][dd] >= o + do:
            return True
    return False


update_vistied(sx, sy, sd, 0)

while q:
    x, y, d, o, dist = q.popleft()
    # print('pop from q : ', x, y, 'direction: ', d)
    for dx, dy, do, dd in delta_search[d]:
        nx, ny, no = x+dx, y+dy, o+do
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if graph[nx][ny]:
            continue
        # visited 로직을 변경
        # 동서남북 중 하나라도 작은걸로 업데이트 된다면 진행

        if d == dd:
            if x == sx and y == sy:
                if find_min_order(nx, ny, dd, no+1):
                    visited[nx][ny][0] = min(no+1, visited[nx][ny][0])
                    q.append([nx, ny, dd, no+1, 1])
                    update_vistied(nx, ny, dd, no+1)
            else:
                if find_min_order(nx, ny, dd, no):
                    if dist == 3:
                        no += 1
                        dist = 0
                    visited[nx][ny][0] = min(no, visited[nx][ny][0])
                    q.append([nx, ny, dd, no, dist+1])
                    update_vistied(nx, ny, dd, no)
        else:
            if find_min_order(nx, ny, dd, no+1):
                visited[nx][ny][0] = min(no+1, visited[nx][ny][0])
                q.append([nx, ny, dd, no+1, 1])
                update_vistied(nx, ny, dd, no+1)

        # if nx == 1 and ny == 3:
        #     print('from', x, y, 'print next point : ', nx, ny)
        #     print('direction: ', dd, 'orders:', no)
        #     print(visited[tx][ty])

# print(visited[tx][ty])
print(visited[tx][ty][td])
# for i in range(M):
#     for j in range(N):
#         if visited[i][j][0] == INF:
#             print(0, end=" ")
#         else:
#             print(visited[i][j][0], end=" ")
#     print()
# 풀이 날짜 및 소요 시간
# 2025-05-28 13:35 ~ HH:MM

# 문제 요약
# N x N 체스판에서 비숍을 놓으려고 한다
# 각 칸에는 비숍을 놓을 수 있는지 없는지에 대한 정보가 담겨있다. 1 가능 / 0 불가능
# 비숍은 대각선으로만 이동 가능하여 다른 말을 잡을 수 있으며 놓을 수 없는 자리도 지나갈 수있다.
# 비숍을 서로가 서로를 잡지 못하게 체스판 위에 최대 몇 개 놓을 수 있는지 출력하라.

# 입력 예제
# 5
# 1 1 0 1 1
# 0 1 0 0 0
# 1 0 1 0 1
# 1 0 0 0 0
# 1 0 1 1 1

# 입력 범위 및 조건
# 10초 128MB
# N 1 ~ 10

# 풀이 방법 및 시간, 공간복잡도 계산
# 좌 대각선 번호
# 우 대각선 번호를 지정해서 어떤 칸에 비숍을 놓았다면 해당 줄은 선택할 수 없음을 나타내야 함
# 4x4 크기의 체스판에서 대각선 번호
# 좌대각선 우대각선
# 4567    1234
# 3456    2345
# 2345    3456
# 1234    4567


# 코드 작성
import sys
from collections import deque
_input = sys.stdin.readline
def minput(): return map(int, _input().split())
N = int(_input())

def l_cross():
    q = deque()
    q.append((N-1, 0, 1))
    l_graph[N-1][0] = 1
        
    while q:
        x, y, num = q.popleft()
        for dx, dy in [[-1, 0], [0, 1]]:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >=N:
                continue
            if l_graph[nx][ny]:
                continue
            q.append((nx, ny, num+1))
            l_graph[nx][ny] = num+1
    
def r_cross():
    q = deque()
    q.append((0, 0, 1))
    r_graph[0][0] = 1
        
    while q:
        x, y, num = q.popleft()
        for dx, dy in [[1, 0], [0, 1]]:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >=N:
                continue
            if r_graph[nx][ny]:
                continue
            q.append((nx, ny, num+1))
            r_graph[nx][ny] = num+1
    
def dfs(i, j):
    stack = []
    stack.append([i, j, i, j])
    l_visit[l_graph[i][j]] = True
    r_visit[r_graph[i][j]] = True
    cnt = 0
    
    while stack:
        xi, yi, x, y = stack[-1]
        # print(xi, yi, x, y)
        is_valid = True
        while True:
            y += 1
            if y == N:
                if x == N-1:
                    is_valid = False
                    break
                x += 1
                y = 0
            if graph[x][y] == 0:
                continue
            if l_visit[l_graph[x][y]] or r_visit[r_graph[x][y]]:
                continue
            break
        if not is_valid:
            cnt = max(cnt, len(stack))
            a, b, c, d = stack.pop()
            if stack:    
                stack[-1][2] = a
                stack[-1][3] = b
                l_visit[l_graph[xi][yi]] = False
                r_visit[r_graph[xi][yi]] = False
            continue
        # print(x, y)
        # print(l_graph[x][y])
        stack.append([x, y, x, y])
        l_visit[l_graph[x][y]] = True
        r_visit[r_graph[x][y]] = True
        
    return cnt

graph = [list(minput()) for _ in range(N)]

l_graph = [[0] * N for _ in range(N)]
r_graph = [[0] * N for _ in range(N)]
r_cross()
l_cross()
l_visit = [False] * (2*N)
r_visit = [False] * (2*N)

output = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            continue
        output = max(output, dfs(i, j))
    
print(output)
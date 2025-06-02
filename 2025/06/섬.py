# 풀이 날짜 및 소요 시간
# 2025-05-26 12:34 ~ 2025-05-27 13:58

# 문제 요약
# . 은 바다 x 는 섬으로 표현된 NxM 크기의 지도가 주어짐
# 하나의 섬은 상하좌우대각선으로 이어진 x 를 의미함
# 바다는 상하좌우로 이어진 . 을 의미함
# 섬의 기본 높이는 0 임 
# 어떤 섬이 다른 섬을 포함하고 있다면 높이가 1 높아짐
# 포함한다는 것은 안에 있는 섬이 바깥 섬을 지나지 않고서 나갈 수 없을 때이다
# 이때 이동은 상하좌우만 가능, 대각선 불가능
# 섬의높이 0부터 k 까지 몇 개의 섬이 있는지 차례대로 출력
# 아무 섬도 없다면 -1 을 출력

# 입력 예제x
# 5 5
# xxxxx
# x...x
# x.x.x
# x...x
# xxxxx
# ans : 1 1

# 입력 범위 및 조건
# 2초 128MB
# N, M 1 ~ 50

# 풀이 방법 및 시간, 공간복잡도 계산
# 1. 각 섬에 1번부터 번호를 부여한다
# 2. 최외곽 바다에서 출발해 닿는 섬을 최외곽 섬.. 바다를 부모로 지정한다.
# 3. 각 섬에서 출발해 바다로는 가지 않고 내부로만 탐색하고 섬을 만나면.. 시작섬을 부모로 지정한다.
# 최외곽부터 내부로만 들어가니까 50x50 = 2500 크기의 bfs 만큼만 시간복잡도가 들지않을까?
# 정점수 2500 간선수 5000? 약 1만의 BFS 비용 
# 1.이 BFS 1번
# 2~3. 이 BFS 1번.


# 섬의 포함관계 여부를 따져 높이를 계산해야 함
# 포함관계를 알려면 섬의 안과 밖을 구분해야함
# 델타 탐색을 밖으로만 나가야 알수 있음
# 안과 밖을 구분하기 쉽지 않다
# 바다인 최외각에 닿는다 => 어떤 섬에 포함되어있지 않은 섬이다
# 각 섬에서 탐색을 진행하는데 특정 조건을 만족했을 때 포함되거나 포함되지 않는다는 것을 찾아내야 함
# 바다를 각 섬의 번호에 -를 붙인걸로 내부바다를 칠해놓기
# 최외곽 바다는 -1
# 해당 섬의 내부 바다는 섬번호
# 
# [-1, -1, -1, -1, -1, -1, -1],
# [-1, 1, 1, 1, 1, 1, -1], 
# [-1, 1, 0, 0, 0, 1, -1], 
# [-1, 1, 0, 2, 0, 1, -1],
# [-1, 1, 0, 0, 0, 1, -1],
# [-1, 1, 1, 1, 1, 1, -1],
# [-1, 1, 1, 1, 1, 1, -1],
# [-1, 1, 0, 0, 0, 1, -1],
# [-1, 1, 0, 3, 0, 1, -1],
# [-1, 1, 0, 0, 0, 1, -1], 
# [-1, 1, 1, 1, 1, 1, -1],
# [-1, -1, -1, -1, -1, -1, -1]]

# 코드 작성
import sys
from collections import deque, defaultdict
_input = sys.stdin.readline
def minput(): return map(int, _input().split())
N, M = minput()

def set_islands():
    q = deque()
    visited = [[False] * M for _ in range(N)]
    num = 0
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == ".":
                continue
            if visited[i][j]:
                continue
            num += 1
            islands[i][j] = num
            visited[i][j] = True
            q.append((i, j))
            
            while q:
                x, y = q.popleft()
                for dx, dy in delta_8way:
                    nx, ny = x+dx, y+dy
                    if nx < 0 or nx >= N or ny < 0 or ny >= M:
                        continue
                    if visited[nx][ny]:
                        continue
                    if graph[nx][ny] == ".":
                        continue
                    
                    islands[nx][ny] = num
                    visited[nx][ny] = True
                    q.append((nx, ny))

                    
def set_parents():
    # 최외곽 바다 설정 + 접촉한 섬 기록
    q = deque()
    visited = [[False] * M for _ in range(N)]
    islands[0][0] = 0
    visited[0][0] = True
    q.append((0, 0))
    found = [{}, {}]
    
    while q:
        x, y = q.popleft()
        for dx, dy in delta_4way:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == "x":
                if not found[0].get(islands[nx][ny]):
                    found[0][islands[nx][ny]] = (nx, ny)
                    parents[islands[nx][ny]] = 0
                    children[0].append(islands[nx][ny])
                continue
            
            islands[nx][ny] = 0
            visited[nx][ny] = True
            q.append((nx, ny))
    # print(found)
    # 사용할 found 번호
    switch = 0
    # 접촉한 섬부터 탐색
    while True:
        if not found[switch]:
            break
        
        for num in found[switch]:
            i, j = found[switch][num]
            
            q.append((i, j))
            
            while q:
                x, y = q.popleft()
                delta = delta_4way
                if graph[x][y] == "x":
                    delta = delta_8way
                for dx, dy in delta:
                    nx, ny = x+dx, y+dy
                    if nx < 0 or nx >= N or ny < 0 or ny >= M:
                        continue
                    if visited[nx][ny]:
                        continue
                    # 부모 바다면 넘어가기
                    if islands[nx][ny] == parents[num]:
                        continue
                    
                    if graph[nx][ny] == "x" and islands[nx][ny] != num:
                        if not found[not switch].get(islands[nx][ny]):
                            found[not switch][islands[nx][ny]] = (nx, ny)
                            parents[islands[nx][ny]] = num
                            children[num].append(islands[nx][ny])
                        continue
                    
                    islands[nx][ny] = num
                    visited[nx][ny] = True
                    q.append((nx, ny))
                
        found[switch] = {}
        # print(found)
        if switch:
            switch = 0
        else:
            switch = 1
    


# 전체 지도 ( 바다로 감싸기 )
graph = ["." * (M+2)] + ["." + _input().rstrip() + "." for _ in range(N)] + ["." * (M+2)]
# 바다크기만큼 N, M 수정
N += 2 
M += 2

islands = [[-1] * M for _ in range(N)]
delta_8way = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
delta_4way = [[-1, 0], [1, 0], [0, -1], [0, 1]]

set_islands()

parents = [-1] * (N * M)
children = defaultdict(list)
set_parents()

heights = [-1] * (N * M)
# print(children)
# children 로 높이 계산하기 - 메모이제이션
def get_heights(cur):
    if heights[cur] != -1:
        return heights[cur]
    
    if not children[cur]:
        heights[cur] = 0
        return 0
    
    for child in children[cur]:
        heights[cur] = max(heights[cur], get_heights(child) + 1)
    return heights[cur]
        
get_heights(0)

cnts = [0] * (N * M)
for i in range(1, N*M):
    if heights[i] == -1:
        break
    cnts[heights[i]] += 1

output = []
for cnt in cnts:
    if cnt == 0:
        break
    output.append(str(cnt))

if not output:
    print(-1)
else:
    print(" ".join(output))



## 메모리 초과, 시간 초과
# import sys
# from collections import deque
# _input = sys.stdin.readline
# def minput(): return map(int, _input().split())
# N, M = minput()

# def set_outer_sea():
#     q = deque()
#     q.append((0, 0))
#     while q:
#         x, y = q.popleft()
#         visited[x][y] = True
#         islands[x][y] = -1
        
#         for dx, dy in delta_4way:
#             nx, ny = x+dx, y+dy
#             if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                 continue
#             if graph[nx][ny] != '.' or visited[nx][ny]:
#                 continue
            
#             q.append((nx, ny))

# def set_island_num(num, i, j): # bfs
#     q = deque()
#     q.append((i, j, 0)) # x좌표, y좌표, 0(섬),1(바다)
#     while q:
#         x, y, is_sea = q.popleft()
#         visited[x][y] = True
#         islands[x][y] = num
#         for dx, dy in delta_8way:
#             nx, ny = x+dx, y+dy
#             if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                 continue
#             if visited[nx][ny]:
#                 continue
#             if graph[nx][ny] == '.':
#                 if islands[nx][ny] == -1:
#                     continue
#                 q.append((nx, ny, 1))
#             else:
#                 if is_sea:
#                     continue
#                 q.append((nx, ny, 0))

# def classify_island_hierarchy(num, i, j): # bfs
#     islands_found = set()
    
#     q = deque()
#     q.append((i, j))
#     while q:
#         x, y = q.popleft()
#         visit[x][y] = num
        
#         for dx, dy in delta_4way:
#             nx, ny = x+dx, y+dy
#             if nx < 0 or nx >= N or ny < 0 or ny >=M:
#                 continue
#             # 현재 바다인데 경계를 만났다 최외곽 섬이다
#             if islands[nx][ny] == -1:
#                 return 0
#             if visit[nx][ny] == num:
#                 continue
#             visit[nx][ny] = num
#             if islands[nx][ny]!= num:
#                 parents[num] = islands[nx][ny]
#                 return
#             q.append((nx, ny))
            

# graph = ["."*(M+2)] + ["." + _input().rstrip() + "." for _ in range(N)] + ["."*(M+2)]
# N += 2
# M += 2
# islands = [[0]*M for _ in range(N)]
# visited = [[False]*M for _ in range(N)]
# delta_8way = [[1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1], [0, 1], [0, -1]] # 상하좌우 대각선
# delta_4way = [[1, 0], [-1, 0], [0, 1], [0, -1]] # 상하좌우
# set_outer_sea()
# # 각 섬에 번호를 부여
# num = 0
# for i in range(N):
#     for j in range(M):
#         if visited[i][j]:
#             continue
#         if graph[i][j] == ".":
#             continue
#         num += 1
#         set_island_num(num, i, j)
# del visited
# if num == 0:
#     print(-1)
#     exit()

# # 각 섬의 높이
# visit = [[0]*M for _ in range(N)]
# levels = [-1] * (num + 1)
# parents = [0] * (num + 1)
# # 각 섬에서 포함관계를 찾기
# # 1. 바다인 벽을 만날 수 있다면 높이가 0임
# for k in range(1, num+1):
#     is_valid = True
#     for i in range(N):
#         for j in range(M):
#             if islands[i][j] == num:
#                 classify_island_hierarchy(k, i, j)
#                 is_valid = False
#             if not is_valid:
#                 break
#         if not is_valid:
#             break

# for i in range(1, num+1):
#     levels[i] = max(levels[i], 0)
#     cnt = 0
#     cur = i
#     while True:
#         if not parents[cur]:
#             break
#         cnt += 1
#         cur = parents[cur]
#     levels[cur] = max(levels[i], cnt)
        
# cnts = [0] * (num+1)
# for l in levels:
#     if l == -1:
#         continue
#     cnts[l] += 1

# output = []
# for cnt in cnts:
#     if cnt == 0:
#         break
#     output.append(str(cnt))

# print(" ".join(output))
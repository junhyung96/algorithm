import sys
from collections import deque
def minput(): return map(int, sys.stdin.readline().split())

# 플로이드 워셜
# 방향 그래프에서 a -> b 최단 거리 다 저장해놓고
# a -> b + b -> a 가 최소인 것을 출력
V, E = minput()
INF = int(1e9)
adj_m = [[INF]*(V+1) for _ in range(V+1)]
result = INF

for _ in range(E):
    a, b, c = minput()
    adj_m[a][b] = c

for mid in range(1, V+1):
    for s in range(1, V+1):
        for e in range(1, V+1):
            adj_m[s][e] = min(adj_m[s][e], adj_m[s][mid] + adj_m[mid][e])

for x in range(1, V+1):
    for y in range(1, V+1):
        if adj_m[x][y]+adj_m[y][x] >= INF:
            continue
        result = min(result, adj_m[x][y]+adj_m[y][x])

if result == INF:
    print(-1)
else:
    print(result)
# --------------------------------------------실패------------------------------------------------------
# 시간초과


# import sys
# from collections import deque
# def minput(): return map(int, sys.stdin.readline().split())

# V, E = minput()
# # V 마을(정점) 2 ~ 400
# # E 도로(간선) 0 ~ V(V-1)
# # 도로 길이가 최소가 되는 운동 경로 찾기 
# # 운동 경로는 사이클 이며 두 마을을 왕복하는 것도 포함
# # 운동 경로 도로 길이의 합을 출력

# # 싸이클을 찾는법..
# # 트리처럼 저장한다면?
# # 해당 정점의 부모를 기록하고 그래프 탐색중 부모로 향하는 간선을 만나면 사이클 등록
# # 부모가 여러명이면 어떻게 저장?

# # 1. 한 정점에서 그래프 탐색 을 시도함
# # 2. 방향 그래프니까 갈 수 있는 곳을 다 vistied 처리하고
# # 3. 탐색 종료하면 그 안에서 사이클 존재 와 거리를 찾음
# # 탐색하지 못한 정점에서 1. 으로 돌아감

# # 어떤 한 정점이 그래프 탐색으로 도달할 수 있는 하나의 집합을 만드는 것
# # 각각의 집합에서 싸이클이 존재하는 지
# # 싸이클이 여럿 존재한다면 최소는 무엇인지

# adj_ls = [[] for _ in range(V+1)] # 인접 리스트 ( 간선 정보 저장)
# dist = {} # a 에서 b 정점으로 가는 거리 저장

# for _ in range(E):
#     a, b, c = minput()
#     # a 에서 b 로 가는 도로길이 c ( 방향 그래프임 )
#     adj_ls[a].append(b)
#     dist[str(a)+"-"+str(b)] = c


# result = int(1e9)
# no_cycle = True
# visited = [0] * (V+1)
# group_num = 1
# grouped = [0] * (V+1)

# for i in range(1, V+1): 
#     if grouped[i]:
#         continue
#     # 그래프 탐색 및 사이클 감지
#     # visited 를 그룹숫자로 저장하고
#     # 간선을 통해 가려는 지점이 같은 그룹이라면 사이클 인 건 알 수 있음
#     # 그러면 어디서부터 어디까지가 사이클인가
#     # stack 에서 해당 점정이 나오는 곳까지 뽑아서 따로 사이클의 거리 합을 계산
#     # 이후 그래프 탐색 이어서
#     stack = [[i, 0]] # [정점, adj_ls 탐색한 마지막 정점 index]
#     visited[i] = group_num
#     grouped[i] = group_num

#     while stack:
#         now, idx = stack[-1]
#         for nxt in adj_ls[now][idx:]:
#             # print(now, nxt, idx, stack)
#             stack[-1][1] += 1
#             if visited[nxt]:
#                 # continue
#                 # 이미 저장된 곳인지
#                 if visited[nxt] == group_num:
#     #                 print("cycle", stack)
#                     # 같은 그룹이라면 사이클 발생
#                     # 사이클에서 거리 정보 추출하는 로직 필요
#                     q = deque()
#                     j = -1
#                     is_cycle = False
#                     while True:
#                         # print(stack, nxt, j, stack[j][0])
#                         q.appendleft(stack[j][0])
#                         if stack[j][0] == nxt:
#                             is_cycle = True
#                             break
#                         if -j == len(stack):
#                             break
#                         j -= 1
                    
#                     if is_cycle:
#                         no_cycle = False
#                         dist_sum = 0
#                         l = len(q)
#                         for qi in range(l-1):
#                             key = str(q[qi])+"-"+str(q[qi+1])
#                             dist_sum += dist[key]
#                         key = str(q[qi+1])+"-"+str(q[0])
#                         dist_sum += dist[key]
#                         # print(q, dist_sum)
#                         result = min(dist_sum, result)
#                 continue
#             stack.append([nxt, 0])
#             visited[nxt] = group_num
#             grouped[nxt] = group_num
#             break
            
#         else:
#             visited[stack.pop()[0]] = 0

#     # 사이클 끝나면 group_num ++
#     group_num += 1
#     # print("visit", grouped)

# if no_cycle:
#     print(-1)
# else:
#     print(result)
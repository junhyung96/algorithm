# 풀이 날짜 및 소요 시간
# 2025-05-05 16:00 ~ HH:MM

# 문제 요약
# 그래프에서 간선을 끊었을 때 그래프가 두 개이상으로 나뉘는 간선을 단절선이라 한다
# 단절선을 찾아 출력하라. (사전순으로 출력)

# 입력 예제
# 7 8
# 1 4
# 4 5
# 5 1
# 1 6
# 6 7
# 2 7
# 7 3
# 2 3

# 입력 범위 및 조건
# V 1~100,000
# E 1~1,000,000
# 메모리 256MB, 시간 1초

# 풀이 방법 및 시간, 공간복잡도 계산
# DFS 돌면서 사이클 확인
# 1- > 4 -> 5 -> 1 사이클 만나면
# 1 을 부모로 하는 사이클임을 stack pop 할 때 -1 에 정보를 넘기기
# 사이클 정보가 없다면 단절선임으로 단절선으로 추가
# cycle 인건 어떻게 아느냐? 
# stack 에 들어갈 때 is_stack = node : true 
# stack 에서 빠질 때 is_stack = node : false
# 간선을 타고 갔더니 is_stack true, 스택에 남아있다 사이클 발생

# 코드 작성
import sys
from collections import defaultdict
_input = sys.stdin.readline
def minput(): return map(int, _input().split())
INF = int(1e9)

V, E = minput()
adj_ls = defaultdict(list)
result = []

for _ in range(E):
    a, b = minput()
    adj_ls[a].append(b)
    adj_ls[b].append(a)

visited = [False] * (V+1)
low = [INF] * (V+1)
par = [1] * (V+1)
times = [1] * (V+1)

time = 1
low[1] = time
times[1] = time
visited[1] = True
stack = [[1, 0]] # 노드, 탐색인덱스

while stack:
    cur, vi = stack[-1]

    if vi < len(adj_ls[cur]):
        nxt = adj_ls[cur][vi]
        stack[-1][1] += 1
        if nxt == par[cur]:
            continue

        if visited[nxt]:
            low[cur] = min(low[nxt], low[cur])
        else:
            time += 1
            visited[nxt] = True
            stack.append([nxt, 0])
            par[nxt] = cur
            times[nxt] = time
            low[nxt] = time
        
    else:
        node, i = stack.pop()
        if low[node] > times[par[node]]:
            result.append((min(node, par[node]), max(node, par[node])))
        else:
            low[par[node]] = min(low[par[node]], low[node])
# print(low)
output = []    
result.sort(key = lambda x: (x[0], x[1]))
output.append(str(len(result)))
for edge in result:
    output.append(str(edge[0]) + " " + str(edge[1]))
print("\n".join(output))


# import sys
# from collections import defaultdict
# _input = sys.stdin.readline
# def minput(): return map(int, _input().split())

# V, E = minput()
# adj_ls = defaultdict(list)
# result = []

# for _ in range(E):
#     a, b = minput()
#     adj_ls[a].append(b)
#     adj_ls[b].append(a)


# # dfs 1번 노드부터 탐색
# is_stack = defaultdict(bool)
# # stack = [[1, 0, {}]] # 노드 번호, 간선 탐색 인덱스, 사이클(부모) 맵
# stack = [[1, 0, 0]] # 노드 번호, 간선 탐색 인덱스, 사이클(부모)
# is_stack[1] = True
# visited = [False] * (V+1)
# visited[1] = True
# par = [0] * (V+1)
# depth = [0] * (V+1)
# time = 0
# depth[1] = time

# pre = 0
# while stack:
#     # print(stack)
#     # cur, vi, cycle_map = stack[-1]
#     cur, vi, cycle_par = stack[-1]
#     is_stack[cur] = True
#     stack[-1][1] += 1
#     # 간선이 존재하는지
#     if vi < len(adj_ls[cur]):
#         nxt = adj_ls[cur][vi]
#         if nxt == par[cur]:
#             continue
#         # 깊이 탐색 중 스택에 존재하는 것 = 사이클 발생
#         if is_stack[nxt]:
#             # stack[-1][2][nxt] = True
#             if (not stack[-1][2]) or depth[nxt] < depth[stack[-1][2]]:
#                 stack[-1][2] = nxt

#         if visited[nxt]:
#             continue
#         else:
#             # stack.append([nxt, 0, {}])
#             stack.append([nxt, 0, 0])
#             visited[nxt] = True
#             par[nxt] = cur
#             time += 1
#             depth[nxt] = time

#     else:
#         # cur, vi, cycle_map = stack.pop()
#         # print(stack[-1])
#         cur, vi, cycle_par = stack.pop()
#         is_stack[cur] = False

#         # if cycle_map.get(cur):
#         #     del cycle_map[cur]
#         if cycle_par == cur:
#             cycle_par = 0

#         # if not cycle_map and cur != 1:
#         if not cycle_par and cur != 1:
#             result.append((min(cur, par[cur]), max(cur, par[cur])))
#         if stack:
#             if (not stack[-1][2]) or depth[cycle_par] < depth[stack[-1][2]]:
#                 stack[-1][2] = cycle_par
#             # for node in cycle_map:
#             #     stack[-1][2][node] = True

# output = []    
# result.sort(key = lambda x: (x[0], x[1]))
# output.append(str(len(result)))
# for edge in result:
#     output.append(str(edge[0]) + " " + str(edge[1]))
# print("\n".join(output))


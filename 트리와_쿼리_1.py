# N 개의 정점으로 이루어진 트리(무방향 사이클없는 연결 그래프)
# 간선 1~N-1 번호
# 두 쿼리를 수행하라
# 1. i번 간선의 비용을 c로 바꾼다
# 2. u 에서 v 로 가는 단순 경로에 존재하는 비용 중 가장 큰 것을 출력한다

# 트리에서 임의의 두 정점 사이의 간선 중에서 최대값을 구해야 함
# 트리를 선형화 해서 세그먼트 트리로 최대값 바로 뽑아오겠다
# 6
# 1 2 1
# 2 4 1
# 2 5 2
# 1 3 1
# 3 6 2
# 1
# 2 5 5
# TC
# 6
# 1 2 3
# 1 3 4
# 2 5 5
# 3 4 6
# 3 6 7
# 6
# 2 1 1
# 2 1 2
# 2 1 3
# 2 1 4
# 2 1 5
# 2 1 6

# 현재 코드의 문제점 lca 보다 높은 조상인 head 로 점프 해버림
# lca 코드 다시 넣고
# 로직 변경 필요

import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
def minput(): return map(int, input().split())
output = []

def dfs(node, parent): # 트리 정보 초기화 (깊이, 부모)
    depth[node] = depth[parent] + 1

    for nxt, cost in adj_ls[node]:
        if nxt == parent:
            continue
        parents[nxt][0] = node
        dfs(nxt, node)
        subtree_size[node] += subtree_size[nxt]

def hld(node, parent):
    global group_id, seg_id
    adj_ls[node].sort(key=lambda x: subtree_size[x[0]], reverse=True) # adj_ls[u] : [[v1, w1], [v2, w2], ...]

    heavy = -1
    for nxt, cost in adj_ls[node]:
        if nxt == parent:
            continue
        heavy = nxt
        group[nxt] = group_id
        seg_id += 1
        id_arr[nxt] = seg_id
        hld(nxt, node)
        break

    for nxt, cost in adj_ls[node]:
        if nxt == parent or nxt == heavy:
            continue
        group_id += 1
        group[nxt] = group_id
        head[group_id] = nxt
        seg_id += 1
        id_arr[nxt] = seg_id
        hld(nxt, node)

def query(left, right):
    left += 1
    right += 1
    result = -int(1e9)

    while left < right:
        if left % 2:
            result = max(result, seg_tree[left])
            left += 1
        if right % 2:
            right -= 1
            result = max(result, seg_tree[right])
        left //= 2
        right //= 2

    return result 

def update_tree(id, value):
    seg_tree[id] = value

    while id > 1:
        id //= 2
        seg_tree[id] = max(seg_tree[id*2], seg_tree[id*2+1])

N = int(input())
logN = (N-1).bit_length()
size = 2 ** logN
adj_ls = [[] for _ in range(N+1)] 

seg_tree = [0] * size * 2 # v: 해당 정점으로 들어오는 간선의 크기 저장
id_arr = [0] * (N+1) # i: 정점 v: 세그먼트트리인덱스 tree_id[1] = x | 1번 정점은 세그먼트 트리 1번 인덱스를 가리킴
seg_id = size

edges = [[] for _ in range(N)]
for i in range(N-1):
    u, v, w = minput()
    edges[i+1] = [u, v, w]
    adj_ls[u].append([v, w])
    adj_ls[v].append([u, w])

group_id = 1
subtree_size = [1] * (N+1) # 각 노드가 루트일 때 서브트리 사이즈
subtree_size[0] = 0
depth = [0] * (N+1) # 노드 깊이
parents = [[0]*logN for _ in range(N+1)] # 희소테이블 부모저장
group = [0] * (N+1) # hld 체인은 최대 N개
head = [0] * (N+1) # 각 그룹의 헤드

dfs(1, 0)
group[1] = group_id
id_arr[1] = seg_id
head[1] = 1
hld(1, 0)

for k in range(1, logN):
    for i in range(1, N+1):
        parents[i][k] = parents[parents[i][k-1]][k-1]

for edge in edges[1:]:
    u, v, w = edge
    # u 가 더 깊은 노드로 설정
    if depth[u] < depth[v]:
        u, v = v, u
    seg_tree[id_arr[u]] = w

for i in range(size-1, 0, -1):
    seg_tree[i] = max(seg_tree[i*2], seg_tree[i*2+1])

Q = int(input())
for _ in range(Q):
    q, a, b = minput()
    if q == 1:
        u, v, w = edges[a]
        if depth[u] < depth[v]:
            u, v = v, u
        update_tree(id_arr[u], b)
    else:
        if a == b:
            output.append(str(0))
            continue
        if depth[a] < depth[b]:
            a, b = b, a

        result = -int(1e9)
        x, y = a, b
        # lca 찾기
        diff = depth[x] - depth[y]
        for k in range(logN):
            if diff & (1<<k):
                x = parents[x][k]
        if x == y:
            lca = x
        else:
            for k in range(logN-1, -1, -1):
                if parents[x][k] != parents[y][k]:
                    x = parents[x][k]
                    y = parents[y][k]
            lca = parents[x][0]

        while group[a] != group[b]:
            if group[a] == group[lca]:
                result = max(result, query(id_arr[lca], id_arr[a]))
                a = lca
            else:
                result = max(result, query(id_arr[head[group[a]]], id_arr[a]))
                result = max(result, seg_tree[id_arr[head[group[a]]]])
                a = parents[head[group[a]]][0] # 그룹의 헤드로 이동

            if depth[a] < depth[b]:
                a, b = b, a

        if a != b and group[a] == group[b]:
            result = max(result, query(id_arr[b], id_arr[a]))
        
        output.append(str(result))

sys.stdout.write('\n'.join(output))
# print(group)
# tc2
# 18
# 1 3 1
# 1 9 11
# 3 5 1 
# 5 7 1
# 17 5 1
# 4 5 3
# 14 17 1
# 13 17 1
# 9 2 1
# 18 9 10
# 8 9 1
# 6 8 5
# 15 6 1
# 16 18 7
# 12 16 1
# 16 11 1
# 10 16 1
# 1
# 2 8 12


# print(id_arr)
# print(subtree_size)
# print(depth)
# print(parents)
# print(group)
# print(head)
# print(seg_tree)


        
        # x, lca
        # while group[x] != group[lca]:
        #     result = max(result, query(id_arr[head[group[x]]], id_arr[x]))
        #     x = parents[head[group[x]]][0]
        # result = max(result, query(id_arr[lca], id_arr[x]))
        # while group[y] != group[lca]:
        #     result = max(result, query(id_arr[head[group[y]]], id_arr[y]))
        #     y = parents[head[group[y]]][0]
        # result = max(result, query(id_arr[lca], id_arr[y]))

# import sys, math
# sys.setrecursionlimit(int(1e6))
# input = sys.stdin.readline
# def minput(): return map(int, input().split())

# # 1. 서브트리의 크기를 측정한다
# # 2. 서브트리의 크기를 보고 HLD 로 그룹을 나눈다
# # 3. HLD 그룹별 세그먼트 트리를 구성한다
# # 4. 질의를 수행한다
# # 5. a, b 사이 간선 중 가장 큰 것 출력 (깊이 a > b)
# #    5-0: 해당 그룹의 세그먼트 트리 구간 합을 반환한다.
# #    5-1: a, b 그룹이 같으면 5-0 수행 후 종료
# #    5-2: a, b 그룹이 다르면 a 그룹의 헤드까지의 5-0 수행 후 결과에 더함. 헤드의 부모로 a 를 옮기며 결과에 해당 간선도 더함 

# def dfs1(node, parent, depth, dep, parents): # 서브트리 정점 수 계산
#     subtrees[node] = 1
#     depth[node] = dep
    
#     for nxt, cost in adj_ls[node]:
#         if nxt == parent:
#             continue
#         parents[nxt][0] = node
#         costs[nxt] = cost
#         dfs1(nxt, node, depth, dep+1, parents)
#         subtrees[node] += subtrees[nxt]


# def hld(node, prv):
#     global group_id, seg_id
#     adj_ls[node].sort(key=lambda x: subtrees[x[0]], reverse=True)
#     heavy = -1
#     for nxt, cost in adj_ls[node]:
#         if nxt == prv:
#             continue
#         # 제일 서브트리 많은 정점은
#         heavy = nxt
#         group[nxt] = group[node] # node 그룹에 포함
#         seg_id += 1 
#         seg_tree[seg_id] = costs[nxt]
#         seg_idx[nxt] = seg_id # seg tree 에 등록
#         hld(nxt, node)
#         break
    
#     for nxt, cost in adj_ls[node]:
#         if nxt == heavy or nxt == prv:
#             continue
#         group_id += 1
#         group[nxt] = group_id # 새 그룹 생성
#         head[group_id] = nxt
#         seg_id += 1
#         seg_tree[seg_id] = costs[nxt]
#         seg_idx[nxt] = seg_id # seg tree 에 등록
#         hld(nxt, node)

# def tree_update(id, value):
#     seg_tree[id] = value
#     while id > 1:
#         id //= 2
#         seg_tree[id] = max(seg_tree[id*2], seg_tree[id*2+1])

# def tree_query(l, r): # 구간 중 최대갑 반환
#     result = -int(1e9)
#     r += 1

#     while l < r:
#         if l % 2:
#             result = max(result, seg_tree[l])
#             l += 1
#         if r % 2:
#             r -= 1
#             result = max(result, seg_tree[r])
#         l //= 2
#         r //= 2

#     return result 

# def lca(s, e):
#     global logN
#     # e 가 깊도록
#     if depth[s] > depth[e]:
#         s, e = e, s
    
#     diff = depth[e] - depth[s]
#     for k in range(logN):
#         if diff & 1<<k:
#             e = parents[e][k]
    
#     if s == e:
#         return s
    
#     for k in range(logN-1, -1, -1):
#         if parents[s][k] != parents[e][k]:
#             s = parents[s][k]
#             e = parents[e][k]

#     return parents[s][0]
    
# def is_same_group(x, y):
#     if group[x] == group[y]:
#         return True
#     return False
    
# N = int(input()) # 정점 수 2~100,000 | 1번부터
# logN = int(math.log2(N)) + 1
# size = 2 ** logN
# edges = [[] for _ in range(N+1)]
# adj_ls = [[] for _ in range(N+1)]
# subtrees = [0] * (N+1) # 서브트리 정점 개수
# parents = [[0]*logN for _ in range(N+1)] # 각 정점의 부모정점 binary lifting
# costs = [0] * (N+1) # 자기 자신 노드로 오는 간선의 가중치 저장 1 -> 2 노드로 간다 그러면 2에 간선 가중치 저장 why? 트리 루트 부터 내려가면 뻗는건 여럿이지만 들어오는건 하나임
# depth = [0] * (N+1) # 정점 깊이
# head = [0]* (N+1) # 각 세그먼트 트리의 헤드
# group = [0] *(N+1)
# group_id = 1
# seg_idx = [0] * (N+1)
# seg_id = size
# seg_tree = [0] * 2 * size

# # print(seg_tree)

# for i in range(1, N):
#     u, v, w = minput()
#     edges[i] = [u, v, w]
#     adj_ls[u].append((v, w))
#     adj_ls[v].append((u, w))

# dfs1(1, 0, depth, 1, parents)
# group[1] = head[1] = 1
# seg_idx[1] = seg_id

# hld(1, 0)

# # 세그먼트 트리 초기화
# for i in range(size-1, 0, -1):
#     seg_tree[i] = max(seg_tree[i*2], seg_tree[i*2+1])
# # print(subtrees)
# # print(depth)
# # print(parents)
# # print(group)
# # print(costs)
# # print(seg_idx)
# # print(seg_tree)
# # print(seg_tree)
# M = int(input()) # 쿼리 수 1~100,000
# output = []
# for _ in range(M):
#     q, a, b = minput() 
#     # q == 1: a번 간선의 비용을 b로 변경 
#     # q == 2: a 에서 b 로가는 단순경로 최대비용 출력
#     if q == 1:
#         x, y, c = edges[a]
#         edges[a] = [x, y, b]
#         if depth[x] < depth[y]:
#             x, y = y, x
#         # 깊이가 높은 쪽에 간선이 저장됨 x 로 통일
        
#         tree_update(seg_idx[x], b)
    
#     else:
#         # 5. a, b 사이 간선 중 가장 큰 것 출력 (깊이 a > b)
#         #    5-0: 해당 그룹의 세그먼트 트리 구간 합을 반환한다.
#         #    5-1: a, b 그룹이 같으면 5-0 수행 후 종료
#         #    5-2: a, b 그룹이 다르면 a 그룹의 헤드까지의 5-0 수행 후 결과에 더함. 헤드의 부모로 a 를 옮기며 결과에 해당 간선도 더함 
#         lca_node = lca(a, b)
#         # print("lca", lca_node)
#         res = -int(1e9)
#         while not is_same_group(lca_node, a):
#             # print("A", a)
#             res = max(res, tree_query(seg_idx[head[group[a]]], a))
#             res = max(res, costs[head[group[a]]])
#             a = parents[head[group[a]]][0]
#             # print("A", a)
#         while not is_same_group(lca_node, b):
#             # print(b)
#             res = max(res, tree_query(seg_idx[head[group[b]]], b))
#             res = max(res, costs[head[group[b]]])
#             b = parents[head[group[b]]][0]
#         # tree query 는 left right 
#         # left 가 depth 가 낮으므로 b, a 순
#         # print(a, b)
#         if depth[a] < depth[b]: # 깊이가 큰 것을 a 로 변경
#             a, b = b, a 
#         res = max(res, tree_query(seg_idx[b], seg_idx[a]))

#         output.append(str(res))
#         # print(res)
# sys.stdout.write('\n'.join(output))
# 풀이 날짜 및 소요 시간
# 2025-04-04 ~ 2025-04-26

# 문제 요약
# 양방향 가중치 간선으로 임의의 두 정점을 이동가능한 트리에서 쿼리 해결
# 쿼리1. 특정 정점으로 이동하는 최단거리 * 인구수 합 출력
# 쿼리2. 특정 정점의 인구수 증가

# 입력 범위 및 조건
# 정점 수, 쿼리 수 최대 60,000

# 풀이 방법 및 시간, 공간복잡도 계산
# 오일려경로 테크닉 + 리루팅(누적합) + 최소 공통 조상 + sqrt(N) 업데이트마다 갱신
# 쿼리1 리루팅으로 전부 구해두기
# 인구수 증가 시 LCA 로 최단거리 계산 후 더해서 출력
# 인구수 증가 쿼리가 sqrt(N)개 쌓이면 리루팅으로 다시 전체 갱신

# 혹은
# 센트로이드

# 오류 및 최적화 기록
# 1. 런타임 에러 -> set recursion ( 파이썬 재귀 깊이 수정 )
# 2. 재귀 dfs 불가능 ( 메모리 초과 ) -> 반복문 으로 수정
# 3. print -> output join 으로 한번에 출력 수정
# 4. dfs 인접리스트 순회 인덱스 기록 ( 재귀보다 3~4배 이상 걸림 )
# 5. for break 문 -> if + 인덱스 조회 수정 ( 재귀와 비슷한 속도로 나옴, for break 보다 2배 빨라짐 )

# 코드 작성
import sys
sys.setrecursionlimit(int(10**6))
_input = sys.stdin.readline
def minput(): return map(int, _input().split())

def _dfs1():
    global time
    cur = 1
    pre = 0
    d = 1
    l = 0

    time += 1
    Ein[cur] = time
    depth[cur] = d
    dist[cur] = l
    par[cur][0] = pre
    visited = [False] * (60_001)
    visited[cur] = True

    stack = [[cur, d, l, 0]]
    while stack:
        cur, d, l, vi = stack[-1]

        if vi < len(adj_ls[cur]):
            nxt, cost = adj_ls[cur][vi]
            stack[-1][3] += 1
            if visited[nxt]:
                continue
            visited[nxt] = True
            time += 1
            Ein[nxt] = time
            depth[nxt] = d+1
            dist[nxt] = l+cost
            par[nxt][0] = cur
            stack.append([nxt, d+1, l+cost, 0])
        else:
            if stack:
                cur, d, l, vi = stack.pop()
                Eout[cur] = time


def _dfs2():
    global total_pop
    cur = 1
    visited = [False] * (60_001)
    visited[cur] = True
    sub_pops[cur] = pops[cur]
    stack = [[cur, 0, 0, 0]] # 현재노드, 부모노드, 거리

    while stack:
        cur, pre, l, vi = stack[-1]
        # print(stack)
        if vi < len(adj_ls[cur]):
            nxt, cost = adj_ls[cur][vi]
            stack[-1][3] += 1
            if visited[nxt]:
                continue
            visited[nxt] = True
            sub_pops[nxt] = pops[nxt]
            stack.append([nxt, cur, cost, 0])

        else:
            if stack:
                cur, pre, cost, vi = stack.pop()
                sub_pops[pre] += sub_pops[cur]

                # s1 = nxt 의 서브트리가 cur 로 가는 비용
                s1 = sub_pops[cur] * cost
                s2 = (total_pop - sub_pops[cur]) * cost
                i = Ein[cur]
                o = Eout[cur]
                fest[1] += s1 
                # 리루팅
                fest[i] += (s2 - s1) # i에서 축제가 열린다 치면 루트로 가는 s1 은 돌려받고 루트에서 오는 s2 는 더해줘야 함
                fest[o+1] -= (s2 - s1) # 누적합이 적용될 구간 밖은 다시 빼주기


def lca(a, b):
    if depth[a] < depth[b]: # a 가 깊도록
        a, b = b, a 
    
    diff = depth[a] - depth[b]
    for k in range(logN):
        if diff & (1<<k):
            a = par[a][k]

    if a == b:
        return b
    
    for k in range(logN-1, -1, -1):
        if par[a][k] != par[b][k]:
            a = par[a][k]
            b = par[b][k]
    return par[a][0]

# 트리정보 정점, 간선, 인구
N = int(_input())
max_N = max(N, 60_000)
logN = (max_N).bit_length()
sqrtN = int(max_N ** 0.5)
pops = [0] * (max_N+1) # 깐프 인구 수
idx = 1
for v in minput():
    pops[idx] = v
    idx += 1
total_pop = sum(pops)
adj_ls = [[] for _ in range(max_N+1)] # 간선 정보
depth = [0] * (max_N+1) # 트리 깊이
dist = [0] * (max_N+1) # 루트로부터 거리
fest = [0] * (max_N+2) # 축제 비용
sub_pops = [0] * (max_N+1) # 서브트리 인구수

for _ in range(N-1):
    a, b, c = minput()
    adj_ls[a].append((b, c))
    adj_ls[b].append((a, c))

# 오일러경로
time = 0
Ein = [0] * (max_N+1)
Eout = [0] * (max_N+1)

# LCA 희소 테이블 binary lifting
par = [[0]*logN for _ in range(max_N+1)]

# 오일러 경로 초기화 dfs1 ett
# dfs1(1, 0, 1, 0)
_dfs1()
# 축제 비용 초기화 dfs2 rerooting 
# dfs2(1, 0)
_dfs2()
for i in range(1, max_N+1): # 누적합 로직
    fest[i] += fest[i-1]

# 희소테이블 초기화
for j in range(1, logN):            
    for i in range(1, max_N+1):
        par[i][j] = par[par[i][j-1]][j-1]

# 쿼리 수행
arr = []
output = []
Q = int(_input())
for _ in range(Q):
    query = tuple(minput())
    if query[0] == 1:
        result = fest[Ein[query[1]]]
        for v, g in arr:
            # 인구수 증가분만큼 적용
            lca_node = lca(query[1], v)
            result += (dist[query[1]] + dist[v] - 2 * dist[lca_node]) * g
        # print(result)
        output.append(str(result))
    else:
        # 쿼리 = 번호, 정점, 인구증가분
        arr.append((query[1], query[2]))

        # 루트N 마다 갱신 
        if len(arr) == sqrtN:
            for v, g in arr:
                pops[v] += g
            fest = [0] * (max_N+2)
            total_pop = sum(pops)
            # dfs2(1, 0)
            _dfs2()
            for i in range(1, max_N+1):
                fest[i] += fest[i-1]
            arr.clear()
print("\n".join(output))



# def dfs1(cur, pre, d, l):
#     global time
#     time += 1
#     Ein[cur] = time
#     depth[cur] = d
#     dist[cur] = l
#     par[cur][0] = pre

#     for nxt, cost in adj_ls[cur]:
#         if nxt == pre: 
#             continue
#         dfs1(nxt, cur, d+1, l+cost)
        
#     Eout[cur] = time


# def dfs2(cur, pre):
#     global total_pop
#     sub_pops[cur] = pops[cur]

#     for nxt, cost in adj_ls[cur]:
#         if nxt == pre:
#             continue
#         dfs2(nxt, cur)
#         sub_pops[cur] += sub_pops[nxt]

#         # s1 = nxt 의 서브트리가 cur 로 가는 비용
#         s1 = sub_pops[nxt] * cost
#         s2 = (total_pop - sub_pops[nxt]) * cost
#         i = Ein[nxt]
#         o = Eout[nxt]
#         fest[1] += s1 
#         # 리루팅
#         fest[i] += (s2 - s1) # i에서 축제가 열린다 치면 루트로 가는 s1 은 돌려받고 루트에서 오는 s2 는 더해줘야 함
#         fest[o+1] -= (s2 - s1) # 누적합이 적용될 구간 밖은 다시 빼주기
# print(depth)
# print(dist)
# print(sub_size)
# print(Ein)
# print(Eout)
# print(sub_pops)
# print(fest[:7])
# print(par)
### 축제
# 루트를 기준으로 delta 탐색으로 축제 지점까지 비용을 계산할 수 있다.
# 처음 dfs 돌려서 서브트리수, 부모 등등 초기화시키고 hld 돌려서 체인 나눈다..
# 1번이니까 N 두번 돌려도 괜춘
# 
# 사람 수가 변경됐을 때 루트를 빠르게 업데이트하려면?
# 루트까지의 구간 간선총합 * 인구수 변화 를 더하면 바로 업데이트 가능 (hld + 세그먼트트리로 log^2 N 에 가능)
# 루트에서 축제 지점까지 비용 계산 은 순수하게 N 이 걸림..
# 다중 루트 전략
# 루트를 log2 N 개 두고 60000일 때는 16개 정도  꼭 16개가 아니어도 됨
# 루트로부터 너무 멀어지면 체인을 끊고 새로 만드는 거임 그리고 새 체인의 head 를 루트로 만듦
# 인구수 업데이트 된 노드로 부터 전파를 받아야 하는데 업데이트 사실은 구간 질의로 간선 총합 바로 나오기 떄문에
# log^2 N * 루트 수 = 대략 4,000 ( 체인 타고 가니까 로그 제곱 N )
# 16개인 이유가 60000 이 일자형이면 대략 3800개 마다 끊는거임 그래서 질의마다 16개 중에 제일 가까운애 찾고 최대 3800깊이 연산을 해야함
# 걍 체인 헤드 헤드 타고 올라가서 루트면 거기서 부터 업데이트 시키기
# 그러면 대략 8,000 연산 * 60,000 질의 480,000,000 대략 pypy 5초? pyhton 48초?????????

# N 1~60,000
# N 개의 정점에 각각 Gi 명의 깐프가 살고 있다
# N-1 개의 간선으로 임의의 두 정점의 이동이 가능하도록 되어있다.
# 간선의 길이 L 1~1,000
# Q 이벤트 발생 1~60,000
# 이벤트 1 : vi 정점에서 축제가 열린다. 
#           모든 깐프는 해당 정점으로 이동하며 이때 발생하는 비용(거리의 합)을 출력. 
#           돌아가는 길에는 비용이 발생하지 않는다
# 이벤트 2 : vi 정점에서 gi 명이 더 태어난다.

# 1번 루트로 하고 전체 거리 계산
# 루트를 옮길 때 비용 계산해서
# 전체 정점에서 자기가 루트일 때 비용 저장
# 쿼리 1 - O(1) 에 처리
# 쿼리 2 - 누적해두었다가 한번에 업데이트 O(N) dfs 2번 돌아야 하므로

# HLD를 위한 전처리 및 축제 비용 계산
# import sys
# input = sys.stdin.readline
# def minput(): return map(int, input().split())

# def dfs(node, parent): # 트리 정보 초기화
#     depth[node] = depth[parent] + 1
#     parents[node][0] = parent

#     for nxt, cost in adj_ls[node]:
#         if nxt == parent:
#             continue
#         dist[nxt] = dist[node] + cost
#         dfs(nxt, node)
#         subtree_size[node] += subtree_size[nxt]

# def hld(node, parent, d):
#     global group_id, seg_id
    
#     heavy = -1
#     for nxt, cost in adj_ls[node]:
#         if nxt == parent:
#             continue 
#         if d > 3750:
#             break
#         heavy = nxt
#         group[nxt] = group[node]
#         seg_id += 1
#         id_arr[nxt] = seg_id
#         segtree_pop[seg_id] = Gs[nxt]
#         segtree_dist[seg_id] = cost
#         hld(nxt, node, d+1)
#         break

#     for nxt, cost in adj_ls[node]:
#         if nxt == parent or nxt == heavy:
#             continue
#         group_id += 1
#         group[nxt] = group_id
#         head[group_id] = nxt
#         seg_id += 1
#         id_arr[nxt] = seg_id
#         segtree_pop[seg_id] = Gs[nxt]
#         segtree_dist[seg_id] = cost
#         hld(nxt, node, 0)

# def update_pop(idx, inc):
#     segtree_pop[idx] += inc
#     while idx > 1:
#         idx //= 2
#         segtree_pop[idx] += inc

# def query(left, right):
#     res = 0
#     right += 1

#     while left < right:
#         if left % 2:
#             res += segtree_sum[left]
#             left += 1
#         if right % 2:
#             right -= 1
#             res += segtree_sum[right]
#         left //= 2
#         right //= 2

#     return res

# def get_lca(a, b):
#     if depth[a] < depth[b]:
#         a, b = b, a
#     diff = depth[a] - depth[b]
#     for k in range(logN):
#         if diff & (1<<k):
#             a = parents[a][k]
    
#     if a == b:
#         return a
    
#     for k in range(logN-1, 0, -1):
#         if group[a][k] != group[b][k]:
#             a = parents[a][k]
#             b = parents[b][k]
    
#     return parents[a][0]


# N = int(input())
# logN = (N-1).bit_length()
# Gs = [0] + list(minput())
# adj_ls = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     x, y, l = minput()
#     adj_ls[x].append((y, l))
#     adj_ls[y].append((x, l))

# # 총합
# total_cost = [0] * (N+1) # 각 정점이 루트일 때 비용
# # 트리 정보
# subtree_size = [1]*(N+1) # 정점마다 서브트리 크기
# depth = [0]*(N+1) # 정점의 깊이
# parents = [[0] * logN for _ in range(N+1)] # 부모 희소테이블 
# dist = [0]*(N+1) # 루트에서 각 정점까지 거리
# subtree_size[0] = 0
# # hld 정보
# group_id = 0
# group = [0]*(N+1) # 각 정점에 대한 그룹넘버
# head = [0]*(N+1) # 각 그룹에 대한 헤드넘버
# multiple_roots = [1] # 체인 길이가 3750 을 넘어서면 새로운 체인으로 만들고 헤드를 또다른 root 로 지정 최대 16개가 등록될 듯
# # 세그먼트트리
# size = 2 ** logN
# seg_id = size
# id_arr = [0]*(N+1) # 각 정점의 세그트리에서 인덱스
# segtree_pop = [0]*2*size # 인구 수 ( 필요없을 지도 )
# segtree_dist = [0]*2*size # 간선 가중치
# segtree_sum = [0]*2*size # 간선 가중치 x 인구 수 합계

# id_arr[1] = seg_id
# group[1] = group_id
# head[group_id] = 1
# dfs(1, 0)
# segtree_pop[seg_id] = Gs[1]
# # segtree_dist[seg_id] = 0
# # segtree_sum[seg_id] = 0
# hld(1, 0, 0)

# for i in range(1, N+1):
#     print(i)
#     print(dist[i] * Gs[i])
#     segtree_sum[id_arr[i]] = segtree_dist[id_arr[i]] * subtree_size[i]
# for i in range(size-1, 0, -1):
#     segtree_sum[i] = segtree_sum[i*2] + segtree_sum[i*2+1]

# print(Gs)
# print("subtree_size", subtree_size)
# print("depth", depth)
# print("parents", parents)
# print("dist", dist)

# print("group", group)
# print("head", head)
# print("multiple_roots", multiple_roots)
# print("id_arr", id_arr)
# print("segtree_pop", segtree_pop)
# print("segtree_dist", segtree_dist)
# print("segtree_sum", segtree_sum)

# Q = int(input())
# for _ in range(Q):
#     q = tuple(minput())
#     if q[0] == 1:
#         fest_node = q[1]
#         total_cost = segtree_sum[]
#     else:
#         node = q[1]
#         Gs[node] += q[2]
#         segtree_sum[id_arr[node]] = dist[node] * Gs[node]
#         while node > 1:
#             node //= 2
#             segtree_sum[node] = segtree_sum[node*2] + segtree_sum[node*2+1]


# output = []



# import sys
# from collections import defaultdict
# input_ = sys.stdin.readline
# def minput(): return map(int, input_().split())

# def dfs1(node, parent, subtree_sum, dist, Gs, adj_ls):
#     subtree_sum[node] = Gs[node]

#     for nxt, w in adj_ls[node]:
#         if nxt == parent:
#             continue
#         dist[nxt] = dist[node] + w
#         dfs1(nxt, node, subtree_sum, dist, Gs, adj_ls)
#         subtree_sum[node] += subtree_sum[nxt]

# def dfs2(node, parent, subtree_sum, total_cost, total_G, adj_ls):
#     for nxt, w in adj_ls[node]:
#         if nxt == parent:
#             continue
#         # 부모 -> 자식 방향으로 루트가 변경될 때
#         # 인구수.. 부모방향으로 왔던 자식들은 비용이 없어져야되고
#         # 부모 방향에서 가는 인구들은 거리 비용이 추가되어야함
#         # 지금가려는 서브트리 stG1, 부모에서 뻗은 다른 서브트리 합을 stG2 라하면
#         # total_cost 에서 -stG1*w + stG2*w 인데
#         # stG2 = totalG-stG1이니까
#         # => -stG1*w + (totalG-stG1)*w
#         # => (totalG - 2 stG1) * w
#         # 여기서 stG1 = subtree_sum[nxt] 
#         total_cost[nxt] = total_cost[node] + (total_G - 2*subtree_sum[nxt]) * w
#         dfs2(nxt, node, subtree_sum, total_cost, total_G, adj_ls)

# N = int(input_())
# adj_ls = defaultdict(list)
# Gs = [0] + list(minput())  # 1-indexed
# dist = [0]*(N+1) # 루트(1번노드) 에서 각 노드까지의 거리
# subtree_sum = [0]*(N+1) # 각 서브트리의 합
# total_cost = [0]*(N+1) # 각 노드의 총 비용
# total_G = sum(Gs) # 총 인구수

# for _ in range(N-1):
#     x, y, l = minput()
#     adj_ls[x].append((y, l))
#     adj_ls[y].append((x, l))

# dfs1(1, 0, subtree_sum, dist, Gs, adj_ls)
# total_cost[1] = sum(Gs[i] * dist[i] for i in range(1, N+1))

# dfs2(1, 0, subtree_sum, total_cost, total_G, adj_ls)
# # print(dist)
# # print(total_cost)
# # print(subtree_sum)
# Q = int(input_())
# is_update = False
# update_list = defaultdict(int)
# lazy_cnt = 0
# lazy_max = 3_800

# for _ in range(Q):
#     event_info = list(minput())
#     if event_info[0] == 1:
#         if lazy_cnt == lazy_max:
#             for node_update in update_list:
#                 Gs[node_update] += update_list[node_update]
#             dist = [0]*(N+1) # 루트(1번노드) 에서 각 노드까지의 거리
#             subtree_sum = [0]*(N+1) # 각 서브트리의 합
#             total_cost = [0]*(N+1) # 각 노드의 총 비용
#             total_G = sum(Gs) # 총 인구수
#             dfs1(1, 0, subtree_sum, dist, Gs, adj_ls)
#             total_cost[1] = sum(Gs[i] * dist[i] for i in range(1, N+1))
#             dfs2(1, 0, subtree_sum, total_cost, total_G, adj_ls)

#             lazy_cnt = 0
#             update_list.clear()

#         fest_idx = event_info[1] # 축제 장소(노드)
#         result = total_cost[fest_idx]
#         for node_update in update_list:
#             result += update_list[node_update] * ()
#     else:
#         update_list[event_info[1]] += event_info[2]
        # Gs[event_info[1]] += event_info[2]
        # is_update = True

### 시간초과
### 60000 쿼리 60000노드 거리계산 (약 100만) 
# import sys, math
# from collections import defaultdict
# input_ = sys.stdin.readline
# def minput(): return map(int, input_().split())

# def dfs(node, parent, depth, cost, dist, parents):
#     dist[node] = cost
#     depth[node] = depth[parent] + 1
#     parents[node][0] = parent
    
#     for nxt, w in adj_ls[node]:
#         if nxt == parent:
#             continue
#         parents[nxt][0] = node
#         dfs(nxt, node, depth, cost+w, dist, parents)

# def set_parents(N, size, parents):
#     for i in range(1, size):
#         for j in range(1, N+1):
#             # node j 의 2^i 번째 조상은 (node j 의 2^(i-1) 조상)의 2^(i-1) 번째 조상
#             # node A 의 4 번째 조상은 (node A 의 2번째 조상)의 2번째 조상
#             parents[j][i] = parents[parents[j][i-1]][i-1]

# def get_lca_node(s, e, size, depth, parents):
#     # e 의 깊이가 더 크게
#     if depth[s] > depth[e]:
#         s, e = e, s

#     diff = depth[e] - depth[s]
#     for k in range(size):
#         if diff & (1 << k):
#             e = parents[e][k]
    
#     if s == e:
#         return s
    
#     for k in range(size-1, -1, -1):
#         # 루트에서부터 내려오면서 부모가 다르면 s, e 업데이트
#         if parents[s][k] != parents[e][k]:
#             s = parents[s][k]
#             e = parents[e][k]

#     return parents[s][0]

# def get_distance(s, e, size, dist, depth, parents):
#     lca_node = get_lca_node(s, e, size, depth, parents)
#     return dist[s] + dist[e] - dist[lca_node] * 2

# N = int(input_())
# INF = int(1e9)
# adj_ls = defaultdict(list)
# Gs = [0] + list(minput())  # 1-indexed
# dist = [0]*(N+1)
# size = int(math.log2(N)) + 1 # LCA binary lifting size
# parents = [[0]*size for _ in range(N+1)] # 2*n 조상
# depth = [0]*(N+1) # 각 노드의 깊이

# for _ in range(N-1):
#     x, y, l = minput()
#     adj_ls[x].append((y, l))
#     adj_ls[y].append((x, l))

# # dist 초기화
# dfs(1, 0, depth, 0, dist, parents)

# # parents 초기화 binary lifting
# set_parents(N, size, parents)
# Q = int(input_())
# for _ in range(Q):
#     event_info = list(minput())
#     if event_info[0] == 1:
#         result = 0
#         fest_idx = event_info[1] # 축제 장소(노드)
#         # 최소공통조상을 찾는다
#         # dist : root 에서 a 까지의 거리
#         # a 에서 b 로 가는 거리
#         # dist[a] + dist[b] - dist[lca(a, b)] * 2 로 거리를 구한다 
#         for i in range(1, N+1):
#             d = get_distance(i, fest_idx, size, dist, depth, parents)
#             result += d * Gs[i]
#         print(result)
#     else:
#         Gs[event_info[1]] += event_info[2]

########## 시간초과
########## N ~ 60_000
# import sys
# input_ = sys.stdin.readline
# def minput(): return map(int, input_().split())

# N = int(input_())
# INF = int(1e9)
# graph = [[INF]*(N+1) for _ in range(N+1)]
# Gs = [0]*(N+1)

# for idx, num in enumerate(minput()):
#     Gs[idx+1] = num

# for _ in range(N-1):
#     x, y, l = minput()
#     graph[x][y] = l
#     graph[y][x] = l

# for mid in range(1, N+1):
#     for a in range(1, N+1):
#         for b in range(1, N+1):
#             if a == b:
#                 graph[a][b] = 0
#                 continue
#             graph[a][b] = min(graph[a][b], graph[a][mid]+graph[mid][b])

# Q = int(input_())
# for _ in range(Q):
#     event_info = list(minput())
#     if event_info[0] == 1:
#         result = 0
#         fest_idx = event_info[1]
#         for node in range(1, N+1):
#             result += Gs[node] * graph[node][fest_idx]
#         print(result)
#     else:
#         Gs[event_info[1]] += event_info[2]

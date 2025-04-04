# N 개의 정점 1~100,000
# M 개의 길 (사이클 없음) 0~N-1
# 길이가 L 인 N-M-1 개의 새로운 길을 만들려고 한다 1~10000 (L:새 길, T:기존 길)
# 두 정점 을 오가는데 드는 최대 시간이 최소가 되도록 길을 만들어야 한다
# 두 빌라봉을 오가는데 드는 최대 시간을 출력

# 어느 것을 트리의 루트로 두느냐.
# 각 집합에서 트리의 루트를 만듦
# 그리고 하나 씩 전체 트리의 루트로 가정하고 자식으로 이어봄
# 트리 붙이고 루트찾고 붙이고 루트 찾고
# 두 정점을 오가는데 드는 최대 시간을 알기 위해서는 루트에서 가장 깊은 거 두번째로 깊은 거 두 거리의 합

# 간선 저장
# 트리 루트 심사
# 트리 정보 업데이트

# 트리의 지름
# 임의의 지점 x 에서 가장 먼 노드 a 찾기
# 노드 a 에서 가장 먼 노드 b 찾기 
# a ~ b 가 트리의 지름
# 트리의 중점은 당연히 a ~ b 사이에 있겠지?

# 지름이 가장 큰 트리 중심에 나머지 트리 중심 이어 붙이기
# 가장 큰 지름은
# 가장 큰 트리의 지름
# 가장 큰 트리의 반지름 + L + 다른 트리의 반지름
# L + 다른 트리의 반지름 + L + 또다른 트리의 반지름
import sys
from collections import deque, defaultdict
def minput(): return map(int, sys.stdin.readline().split())

N, M, L = minput()
max_N = 100_001
adj_ls = defaultdict(list)
tree_nodes = [[] for _ in range(max_N)]
tree_nums = [0]*max_N # 각 노드 트리번호
tree_dias = [0]*max_N # 트리 지름
tree_rads = [0]*max_N # 트리 반지름
visited = [0]*max_N
dfs_cnt = 0 # dfs visited 세대 구분

# 간선 정보 저장 - 인접 리스트
for _ in range(M):
    A, B, T = minput()
    adj_ls[A].append((B, T))
    adj_ls[B].append((A, T))

# 가장 먼 노드 찾기
def dfs(node, v):
    visited[node] = v
    stack = [(node, 0)]
    y = 0
    cost = 0
    dia_nodes = []

    while stack:
        now, dist = stack[-1]
        
        for nxt, d in adj_ls[now]:
            if visited[nxt] == v:
                continue
            visited[nxt] = v
            stack.append((nxt, dist+d))
            break
        else:
            n, c = stack.pop()
            # print(n)
            if cost < c:
                y = n
                cost = c
                dia_nodes = [(n, c)]
                for s in stack:
                    dia_nodes.append(s)
                

    return y, cost, dia_nodes

# 트리 그룹화
tree_num = 0
for node in range(N):
    if tree_nums[node]:
        continue
    tree_num += 1 # 트리번호는 마지막으로 부여한 트리번호로 남아있음
    
    q = deque()
    q.append(node)
    tree_nodes[tree_num].append(node) # 트리에 노드 저장
    tree_nums[node] = tree_num # 노드에 트리넘버 저장

    while q:
        now = q.popleft()
        for nxt, d in adj_ls[now]:
            if tree_nums[nxt]:
                continue
            q.append(nxt)
            tree_nodes[tree_num].append(nxt)
            tree_nums[nxt] = tree_num

# 트리 지름 및 중심 찾기
for idx in range(1, tree_num+1):
    # 임의의 정점 x
    x = tree_nodes[idx][0]

    # 정점이 하나면 넘어가기
    if not adj_ls[x]:
        continue
    
    # x 에서 가장 먼 a
    dfs_cnt += 1
    a, dummy, dummy2 = dfs(x, dfs_cnt)
    # a 에서 가장 먼 b
    dfs_cnt += 1
    b, tree_dia, arr = dfs(a, dfs_cnt)
    # a 와 b 사이의 거리 = 트리의 지름
    tree_dias[idx] = tree_dia
    tree_rads[idx] = tree_dia
    
    for node, dist in arr[1:]:
        tree_rads[idx] = min(tree_rads[idx], max(tree_dia-dist, dist))
    
# 결과에 필요한 데이터 추출
# 가장 큰 지름
# 가장 큰 반지름 + L + 두번째 큰 반지름
# 두번째 + 세번째 + 2L
tree_rads.sort(reverse=True)

# print(tree_num)
if tree_num >= 3:
    print(max(max(tree_dias),
            tree_rads[0] + L + tree_rads[1],
            tree_rads[1] + 2*L + tree_rads[2]
          ))
elif tree_num == 2:
    print(max(max(tree_dias),
            tree_rads[0] + L + tree_rads[1]
          ))
else:
    print(max(tree_dias))
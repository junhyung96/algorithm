# 풀이 날짜 및 소요 시간
# 2025-10-29 20:43 ~ HH:MM

# 문제 요약
# 인접행렬로 주어지는 그래프
# 도로를 수정해서 모든 도시가 연결될 수 있는가?
# 안된다면 -1을 출력
# 된다면 최소한으로 수정한 도로 개수 출력
# 수정 방법
# a-b, c-d 각각 간선으로 이어져있는 도시 2쌍, 총 4개의 도시를 선택해서 
# a-c, b-d 혹은 a-d, b-c 로 만들 수 있다.

# 입력 예제
# 5
# NYYNN
# YNYNN
# YYNNN
# NNNNY
# NNNYN

# 입력 범위 및 조건

# 풀이 방법 및 시간, 공간복잡도 계산
# 1. DFS
# DFS 로 돌면서 수정할 수 있는 도로개수보다 커지면 돌아오는 식으로 (약간의 백트래킹)
# 도로 개수 체크하면서 dfs 돌기
# a->b 로 가는데 for 문 탐색마다 50개를 체크해야한다면??.. 1번 도달하는데 2500연산 소요
# dfs 경로마다 2500 이 소요된다면.. 50^50 ㄷㄷ;

# 2. 집합
# 연결된 노드끼리 묶어서
# 5개 노드가 4개의 간선으로 연결되어있다.
# 3개의 노드가 3개의 간선으로 연결되어있다. 일 때
# 두번째 집합에서 1개간선을 수정하면 두 집합이 합쳐지므로 1개
# -- 노드개수-1 보다 간선수가 작으면 어차피 연결못하므로 -1 출력

# 코드 작성
import sys
_input = sys.stdin.readline
def minput(): return map(int, _input().split())

N = int(_input())

if N == 1:
    print(0)
    exit()

edges = [[0] * N for _ in range(N)]
edge_cnt = 0
for i in range(N):
    for j, info in enumerate(_input().rstrip()):
        if info == "N":
            continue
        edges[i][j] = 1
        edges[j][i] = 1
        edge_cnt += 1

edge_cnt //= 2
if edge_cnt < N-1:
    print(-1)
    exit()

unions = [[0, 0] for _ in range(N)] # [노드 수, 간선 수]
visitied = [False] * N
union_num = 0

stack = []
for i in range(N):
    if visitied[i]:
        continue
    
    visitied[i] = True
    unions[union_num][0] += 1
    stack.append(i)

    while stack:
        now = stack.pop()

        for nxt, connected in enumerate(edges[now]):
            if visitied[nxt] or not connected:
                continue
            stack.append(nxt)
            visitied[nxt] = True
            unions[union_num][0] += 1
            unions[union_num][1] += 1
    
    union_num += 1

for num in range(union_num):
    if unions[num][1] == 0:
        print(-1)
        exit()

print(union_num-1)
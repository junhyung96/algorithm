import sys, heapq
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N, M = minput()
# N 학생 수 3~10,000
# M 사랑 관계 수 N~100,000

# 조건
# 이미 성사된 사랑 관계는 포기할 수 없다
# K각 관계를 이루지 않도록 한다
# 포기할 수 있는 경우가 여러가지일 경우 애정도 합을 최소화한다

# 사랑 관계를 포기하도록 만든 애정도 합의 최솟값을 출력

 
result = 0
# 최소 스패닝 트리

# 트리
parents = [i for i in range(N+1)]
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

edges = []
for _ in range(M):
    a, b, c, d = minput()
    # 학생 a b, 애정도 c, 성사여부 d
    if d == 1:
        if find_parent(parents, a) != find_parent(parents, b):
            union_parent(parents, a, b)
    else:
        edges.append([c, a, b])

edges.sort(reverse=True)

for c, a, b in edges:
    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
    else:
        # print(a, b, "cost :", c)
        result += c
print(result)
# 트리에서 노드하나를 지운 후 리프노드의 개수 구하기

import sys, collections
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

# 트리정보 저장
# 이중리스트(자식노드 정보)
# dfs 순회하면서 자식없으면 리프 카운트 + 1


N = int(input_())
tree = [[] for _ in range(N)]
root_node = 0
result = 0

for idx, parent_id in enumerate(minput()):
    if parent_id == -1:
        root_node = idx
        continue

    tree[parent_id].append(idx)

deleted_node = int(input_())

stack = [root_node]
visited = collections.defaultdict(bool)
no_leaf = collections.defaultdict(bool)

while True:
    if stack:
        now = stack[-1]
        if now == deleted_node:
            stack.pop()
            continue
        for nxt in tree[now]:
            if nxt == deleted_node:
                continue
            if visited[str(now) + '-' + str(nxt)]:
                continue
            stack.append(nxt)
            visited[str(now) + '-' + str(nxt)] = True
            no_leaf[now] = True
            break
        else:
            if not no_leaf[stack.pop()]:
                result += 1

    if not stack:
        break

print(result)
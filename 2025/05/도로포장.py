# 풀이 날짜 및 소요 시간
# 2025-05-21 16:34 ~ HH:MM

# 문제 요약

# 입력 예제

# 입력 범위 및 조건

# 풀이 방법 및 시간, 공간복잡도 계산

# 코드 작성
import sys, heapq
_input = sys.stdin.readline
def minput(): return map(int, _input().split())
INF = 10**12

def dijkstra(n, k):
    h = [] # (비용, 포장횟수, 현재노드, 이전노드)
    heapq.heappush(h, (0, 0, 1, 0))
    dist = [[INF]*(k+1) for _ in range(n+1)]
    for i in range(k+1):
        dist[1][i] = 0
    
    while h:
        cost, cnt, cur, pre = heapq.heappop(h)
        if cur == n:
            return min(dist[n])
        
        ## 이거 한 줄로 시간초과 해결
        if cost > dist[cur][cnt]:
            continue

        for nxt, weight in adj_ls[cur]:
            if nxt == pre:
                continue
            # 포장 횟수 적은데 이미 방문했고 비용마저 작다면 갈 필요가 없다
            is_valid = True
            for c in range(cnt+1):
                if dist[nxt][c] < cost:
                    is_valid = False
            
            if not is_valid:
                continue
                    
            # 도로 포장 하기
            if cnt < k:
                if cost < dist[nxt][cnt+1]:
                    dist[nxt][cnt+1] = cost
                    heapq.heappush(h, (cost, cnt+1, nxt, cur))

            for c in range(cnt+1):
                if dist[nxt][c] < cost + weight:
                    is_valid = False
            
            if not is_valid:
                continue
                
            # 도로 포장 하지 않기
            if cost + weight < dist[nxt][cnt]:
                dist[nxt][cnt] = cost + weight
                heapq.heappush(h, (cost+weight, cnt, nxt, cur))

    return min(dist[n])


N, M, K = minput()
adj_ls = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = minput()
    adj_ls[a].append((b, c))
    adj_ls[b].append((a, c))

# print(dist_n)
print(dijkstra(N, K))
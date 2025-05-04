import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
# N : 실행중인 앱 수 1~100
# M : 필요한 메모리 크기 1~10,000,000

apps = list(minput()) 
# apps : 실행중인 앱 각각의 메모리 사용량
costs = list(minput())
# costs : 각 앱을 비활성화 했을 때 다시 활성화 시키는 비용


# 비용만 최소화되면 된다 M 보다 크거나 같은 최소 비용을 찾으면 종료
# ...
# N 개 배열만 두고 
# 덮어 씌우기
# 앱들을 비활성화시키고 해당 메모리크기 합에서 최소비용을 저장 어차피 그 크기보다 작은 것들은 해당 비용이 최소일 테니까
# M 을 넘어서는 순간 종료
# 10: 0
# 20: 3
# 30: 3 // 여기서 20: 3 이라는 정보는 필요가 없음
# 각 코스트 마다 확보가능한 최대메모리를 저장
q = deque()
cost_memory = [0] * 10_001
costs_ = []
for idx, cost in enumerate(costs):
    costs_.append([cost, idx])
costs_ = sorted(costs_)

for cost, idx in costs_:
    # print(cost, idx)
    for i in range(10_000, -1, -1):
    # for i in range(10_000, -1, -1):
        if cost_memory[i]:
            q.append(i)
    # 현재 cost : memory 최대값 저장
    
    while q:
        now = q.popleft()
        if cost + now > 10_000:
            continue
        cost_memory[cost+now] = max(cost_memory[cost+now], cost_memory[now] + apps[idx])
        
    cost_memory[cost] = max(cost_memory[cost], apps[idx])
    # print(cost_memory[:10])
for i in range(10_001):
    if cost_memory[i] >= M:
        print(i)
        break

# 코스트가 작은순으로 정렬
# 0 3 3 4 5
# 10 20 30 40 35
# 0 3 3 4 5
# 10 30 40 50 45



# ----------------------------------- 실패 ------------------------------------------------------------

# ------------------------ 이유 ----------------------------
# 메모리 사용량 후보군이 2의 지수곱으로 늘어나서 2의 100승 개가 생김 

# import sys
# input_ = sys.stdin.readline
# def minput(): return map(int, input_().split())


# N, M = minput()
# # N : 실행중인 앱 수 1~100
# # M : 필요한 메모리 크기 1~10,000,000

# apps = list(minput()) 
# # apps : 실행중인 앱 각각의 메모리 사용량
# costs = list(minput())
# # costs : 각 앱을 비활성화 했을 때 다시 활성화 시키는 비용

# # M 크기를 확보하기 위해 앱들을 비활성화해야 함
# # 비용이 최소인 경우의 비용을 출력

# # 메모리 마다 드는 비용의 최소를 계속 갱신
# # 특정 앱들을 종료시켰을 때 확보되는 메모리를 작은 것 부터 차례대로 최소인 비용을 갱신
# memory_cost = {}

# def end_app(app, cost):
#     exist_comb = list(memory_cost)
#     for comb in exist_comb:
#         find_target_memory(app+comb, memory_cost[comb]+cost)
        
#     find_target_memory(app, cost)
        
    

# def find_target_memory(app, cost):
#     if cost > 10_000_000:
#         return 
    
#     if memory_cost.get(app):
#         memory_cost[app] = min(memory_cost[app], cost)
#     else:
#         memory_cost[app] = cost

# # 1 앱 하나를 종료한다
# # 2 해당 크기의 메모리에 드는 비용이 이미 있는지 본다
# # 3 이미 있다면 최소인 것을 저장
# # 4 없다면 이미 있는 메모리에 해당 메모리 크기를 더한다 -> 2로 이동
# # fin. 이분탐색으로 M 보다 크거나 같은 메모리 확보를 위한 비용 출력

# for idx, app in enumerate(apps):
#     end_app(app, costs[idx])

# candis = sorted(list(memory_cost))
# s = 0
# e = len(candis)-1

# while s < e:
#     mid = (s+e)//2
    
#     if candis[mid] >= M:
#         e = mid
#     else:
#         s = mid + 1
        
# # print(candis, s)
# print(memory_cost[candis[s]])
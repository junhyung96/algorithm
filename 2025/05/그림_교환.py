# 풀이 날짜 및 소요 시간
# 2025-05-03 15:00 ~ HH:MM

# 문제 요약
# 그림 거래 규칙
# 1. 산 가격보다 크거나 같은 가격에 팔아야 함
# 2. 같은 그림을 두 번 이상 구매할 수 없음
# 2차원 배열이 주어지는데 graph[i][j] 라 하면
# j 번 예술가가 i 번 예술가에게 그림을 살 때의 가격
# 1번 아티스트가 외부 상인에게서 0원에 그림을 사왔다. 그 친구 아티스트들에게 그림을 팔려고한다.
# 위 조건을 만족하는 거래만 이루어질 때 그림을 소유했던 총 사람의 수 최대값을 출력하라

# 입력 범위 및 조건
# N 2 ~ 15
# 그림가격 0 ~ 9
# 메모리 128MB, 시간 2초

# 풀이 방법 및 시간, 공간복잡도 계산
# 3
# 022
# 101
# 110
# 입력이 다음과 같을 때
# 1번이 외부 상인에게서 0원에 사고
# 2번이 1번에게서 2원에 사면
# graph[2][x] 가 2보다 크거나 같은 값이 없으므로 x는 존재하지 않는다
# 따라서 1번과 2번만이 소유했으므로 총 2명

# 1번이 14명에게 팔고 14명이 13명에게 팔고 15! 팩토리얼수만큼 1조 3000억
# 크거나 같은 사람을 구매자로 택할 때
# 15명이 전부 1원에 사고 팔면
# 어느 것을 우선순위로 두고 다음 사람을 골라야 하는가?
# 크거나 같은 사람이 여럿일 때
# 그 다음 사람이 파는 최소값, 최대값

# b 는 a 에게서 graph[a][b] 에 산다
# b 는 x 에게 graph[b][x] 에 파는데 graph[a][b] 보다 크거나 같아야 한다
# 기준이 뭔가.
# graph[1][x] 에서 x 가 1로부터 사는 가격을 알 수 있다.
# graph[x][k] 에서 k 가 x로부터 사는 가격을 알 수 있다.
# 비트마스킹으로 소유자모임이 가지는 최소가격을 저장

# 비트마스킹을 bit[group][leaf] = price 로 해서
# 해당 그룹의 leaf 노드일 때 price 보다 작으면 추가 탐색 아니면 넘어가기

# 1 5 3 7 -> 6  같은 그룹이라면 말단 노드가 뭐든지 간에 6이 오니까 6의 가중치가 결정된다고 생각햇음
# 1 3 7 5 -> 6  그런데 7->6, 5->6, 3->6 은 엄연히 다른 값인데 왜 그렇게 생각했었지?? 
# 1 5 7 3 -> 6  생각회로가 굳어져서 이걸 말랑하게 하는 방법을 깨달아야 할듯


# 코드 작성
import sys
from collections import defaultdict
_input = sys.stdin.readline
def minput(): return map(int, _input().rstrip())

N = int(_input())
# graph = [[0] * (N+1)] + [[0] + list(minput()) for _ in range(N)]
graph = [list(minput()) for _ in range(N)]
bit_group = [defaultdict(dict) for _ in range(16)]
bit_group[1][1][0] = 0
# bit_group[그룹크기][그룹비트마스크][리프노드번호]

for i in range(1, N):
    bit_group[2][1<<0|1<<i][i] = graph[0][i]
# print(bit_group[2])

for i in range(3, N+1):
    for group in bit_group[i-1]:
        for leaf in bit_group[i-1][group]:
            # print(group, leaf)
            for j in range(1, N):
                # j 에 대한 검증
                if group & 1<<j:
                    continue
                if graph[leaf][j] >= bit_group[i-1][group][leaf]:
                    if bit_group[i][group|1<<j].get(j):
                        bit_group[i][group|1<<j][j] = min(graph[leaf][j], bit_group[i][group|1<<j][j])
                    else:
                        bit_group[i][group|1<<j][j] = graph[leaf][j]

for i in range(1, 16):
    # print(bit_group[i])
    if bit_group[i]:
        continue
    else:
        print(i-1)
        break
else:
    print(i)


# stack = [[i, 1<<i, 1, 0, 1]] # 현재 아티스트, 소유자모임, 모임 명수, 최소가격, 탐색 인덱스
# 완전 탐색
# while stack:
#     # print(stack)
#     v, g, cnt, p, vi = stack[-1]
#     stack[-1][4] += 1
    
#     # 같은 아티스트면 넘어가기
#     if v == vi:
#         continue
#     # 인접 아티스트 다 탐색했는지
#     if vi < len(graph[v]):
#         # print(graph[v][vi])
#         # 이미 그룹에 포함된 아티스트 인지
#         if g & 1<<vi:
#             continue
#         # 현재 그룹이 산 그림의 가격이 
#         # 구매가격이 현재가격보다 크거나 같다면 고려할 필요가 있다.
#         if bit_mask[g|1<<vi].get(vi) and bit_mask[g&1<<vi][vi] <= p:
#             # print(bit_mask[g&1<<vi][vi])
#             continue
        
#         if graph[v][vi] >= p:
#             bit_mask[g&1<<vi][vi] = graph[v][vi]
#             stack.append([vi, g|1<<vi, cnt+1, graph[v][vi], 1])
#             result = max(result, cnt+1)
#     else:
#         # 다 탐색했으면 제거
#         stack.pop()
        
# print(result)

# times = 0
# for i in range(1, 17):
#     time = 1
#     for k in range(i):
#         time *= (16-k) 
#         time //= (k+1)
#     times += time*16
#     print(times, time)
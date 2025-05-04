# 풀이 날짜 및 소요 시간
# 2025-04-29 ~ 2025-05-01

# 문제 요약
# 길이가 L 인 통나무를
# K 개의 위치에서 자를 수 있다.
# 최대 C 번 자를 수 있을 때
# 가장 긴 조각을 작게 만들고
# 가장 긴 조각의 길이, 자르는 위치 중 제일 작은 것을 출력

# 입력 예제
# 9 2 1
# 4 5
# 9 길이의 나무를 4, 5 위치에서 자를 수 있는데 1번 자를 수 있다.
# 4에서 자르든 5에서 자르든 나무 조각은 4, 5 의 길이를 가짐
# 더 작은 위치는 4이므로 4를 택함

# 입력 범위 및 조건
# L 2~10^9
# k 1~10,000

# 풀이 방법 및 시간, 공간복잡도 계산
# 가장 긴 길이 X 에 대한 이분 탐색으로 검증
# 자를 수 있는 위치마다 다 자르고
# 뒤에서부터 앞으로 오면서 X 값보다 작거나 같은 만큼 더해서 붙이고 자른 횟수를 저장
# 가능하다면 이분탐색으로 X 값을 낮춤

import sys
_input = sys.stdin.readline
def minput(): return map(int, _input().split())
INF = int(1e9)

def getMaxLength(n, c):
    s = 0
    e = 1_000_000_000
    max_l = 0
    first_cut = e

    while (s < e):
        mid = (s + e) // 2
        # print(s, e, mid)

        partial_length = 0
        cut_cnt = 0
        last_cut_idx = 0

        for k in range(n-1, -1, -1):
            if lengths[k] > mid:
                cut_cnt = INF
                break

            if partial_length + lengths[k] > mid:
                partial_length = 0
                cut_cnt += 1
                last_cut_idx = k
            
            partial_length += lengths[k]

        if cut_cnt > c:
            s = mid+1
        else:
            e = mid
            max_l = mid
            if cut_cnt == c:
                first_cut = cuts[last_cut_idx]
            else:
                first_cut = cuts[0]


    return max_l, first_cut

L, K, C = minput()
cuts = set(minput())
cuts.add(L)
cuts = sorted(list(cuts))
n = len(cuts)
lengths = [0] * n
lengths[0] = cuts[0]
for i in range(1, n):
    lengths[i] = cuts[i] - cuts[i-1]
# print(lengths)
max_l, first_cut = getMaxLength(n, C)
print(max_l, first_cut)




# 풀이 방법 및 시간, 공간복잡도 계산

# 이분탐색을 위해선 이분탐색의 일정한 조건이 필요함
# 가장 긴 나무 조각을 어떤 기준으로 자를 것이냐?
# 가장 긴 조각(a)을 
# 자를 수 있는 회수(b)에 근거해
# 자를수 있는 위치가 큰 쪽에서부터
# 최소 (a/b+1) 길이를 갖는 위치를 골라 자른다.

# 한 번 자르면 b-- 가 되고
# 가장 긴 조각이 뭔지를 알아야 함. 
# heapq 에 넣고 가장 긴 구간을 뽑아온다?
# heapq 에서 가장 긴 구간을 뽑아서 이분 탐색을 진행
# 없다면 그게 가장 긴 길이임
# 횟수가 남았다면 젤 앞에거 자르고 출력하고 리턴
# 이 로직이 맞다는 근거? 가.. 없다.. 검증.. 불확실함..

# 같은 길이인 구간이 여러개 있다면 어떤 순서로 잘라야 하는가?
# 앞에서 부터
# why? 마지막으로 꺼냈다고 생각했을 때 자를 수 있는 경우가 여럿이라면 구간의 시작점이 최소인 곳 부터 잘라야 함

# 10을 i개의 위치에서 자른다.. (i는 1~9)
# 최선의 방법으로 최대가 되는 막대의 길이는??
# x 는 이분탐색으로 logN 시간에 찾을 수 있음.   x를 찾을 때 조건에 맞는 한 최대한 큰 것으로 y > 0 이고 x 가 가능한 것이 여럿일 때
# i = x | x * i + y | y <= x  
# i = 1 | 5 * 1 + 5
# i = 2 | 
# 찾았다면.. 
# 자를 수 있는 위치가 해당 최대 크기의 경계에 좌우 둘다 존재한다면 어떤 것을 골라서 잘라야 하는가?
# 10 ? 3
# 10의 길이를 3번 잘라야 함 1 + 3 + 3 + 3 이 최선일 때
# 최대 길이는 3 하지만 자르는 위치가 저렇게 주어지지 않음
# 0 1 2 3 4 5 6 7 8 9 10
# 0 1     4     7     10 이 최선
# 0 1     4   6   8   10 으로 주어진다면?
# 0       4   6   8   10 => 4 2 2 2 
# 0 1     4   6       10 => 1 3 2 4
# 0 1     4 5     8   10 이라면?
# 0 1     4 5     8   10 => 


# 코드 작성
# import sys, heapq
# _input = sys.stdin.readline
# def minput(): return map(int, _input().split())

# def find_cut(a, b): # 자를 위치 찾기
#     # print("fc", a, b)
#     s = 0 
#     e = len(arr)-1
#     while s < e:
#         mid = (s+e)//2
#         if arr[mid] < a:
#             s = mid + 1
#         elif arr[mid] >= b:
#             e = mid
#         else:
#             s = mid + 1

#     return s

# def find_length(counts, l): # 자를 길이 찾기
#     # l = x * counts + y
#     # 조건 1. x * counts < l
#     # 조건 2. y <= x
#     # 조건 3. y > 0
#     xs = 1
#     xe = l
#     if counts * 2 >= l:
#         return 1

#     # print("l = ", l, " counts = ", counts)
#     while xs < xe:
#         mid = (xs + xe)//2
#         # print(xs, xe, " x = ", mid)
#         xi = mid*counts
#         if xi < l:
#             if l-xi > 0 and l-xi <= mid:
#                 xe = mid
#             else:
#                 xs = mid + 1
#         else:
#             xe = mid
                
#     return xs

# L, K, C = minput()
# arr = set(minput())
# arr.add(L)
# arr.add(0)
# arr = sorted(list(arr))
# h = [] # [구간 길이, 시작점, 끝점]
# heapq.heappush(h, (-L, 0, L)) # 최대값을 꺼내야 하므로 음수로 저장, 구간길이가 같다면 앞부분을 잘라야하기 때문에 시작점, 끝점은 양수로
# cut_limit = min(C, len(arr)-2)
# remain_cut = cut_limit
# had_cut = {}
# max_l = 0
# first_cut = L

# # 종료 시점
# # 1. 자를 수 있는 횟수를 소진했을 때
# # 2. 힙에 남은 구간이 없을 때 - 자를 수 있는 구간이 없다면 힙에서 제거되기 때문에 다 자른 후에는 종료 
# while h: 
#     if remain_cut == 0:
#         break
#     # 1. 가장 긴 구간을 꺼낸다
#     l, s, e = heapq.heappop(h)
#     l *= -1
#     # print("#1 pop ", l, s, e)
#     # 2. 자를 수 있는 횟수에 근거해 잘라야할 최선의 길이를 찾는다.
#     best_length = find_length(remain_cut, l)
#     # print("#2 best length ", best_length)

#     # 3. 자를 수 있는 위치를 찾는다.
#     t = find_cut(s, e-best_length)
#     # print("#3 find t ", t, arr[t])
#     if had_cut.get(arr[t]):
#         arr.pop(t)
#         t = find_cut(s, e-best_length)

#     if t == 0 or t == len(arr)-1:
#         t = find_cut(e-best_length, e)
#     # print("#3 find t ", t, arr[t])

#     # 4-1. 자를 수 있는 위치가 있다면
#     if t != 0 or t != len(arr)-1:
#         # print("#4-1")
#         had_cut[arr[t]] = True
        
#         # 5. 자른 후 생긴 두 구간을 힙에 넣는다.
#         heapq.heappush(h, (s-arr[t], s, arr[t]))
#         heapq.heappush(h, (arr[t]-e, arr[t], e))
#         # print(h)
#     # 4-2. 자를 수 있는 위치가 없다면
#     else:
#         max_l = max(l, max_l)
#         if s == 0:
#             first_cut = min(first_cut, e)
#         else:
#             first_cut = min(first_cut, s)
#         # 6. 최대 길이 및 처음 자른 위치를 갱신한다.
#     remain_cut -= 1

# while h:
#     l, s, e = heapq.heappop(h)
#     l *= -1
#     max_l = max(l, max_l)
#     if s == 0:
#         first_cut = min(first_cut, e)
#     else:
#         first_cut = min(first_cut, s)
#     # 6. 최대 길이 및 처음 자른 위치를 갱신한다.
# print(max_l, first_cut)




# 풀이 방법 및 시간, 공간복잡도 계산
# 가장 긴 나무토막 사이를 잘라야 자를 수 있음
# 1 ---------------------------------- L
#        \           \          \
# [나무토막 길이, 시작점, 끝점] 을 두고
# 시작점 끝점 사이에 존재하는 위치 중 중앙에 있는 걸로 자르면?
# 자른다? -> 붙인다? 다잘라놓고 붙인다면?
# 자르는 횟수 + 1 = 토막 갯수
# 처음에 다 잘라서 heapq 에 넣고
# 조각 길이가 작은 것, 자르는 위치가 나중인 것 순으로 꺼내서
# 붙이고 다시 넣기
# ========= 작은 것 순으로 꺼내면 연속된 나무조각만 붙일 수 있는데 어떻게 처리할지?
# 연속된 두 조각의 합이 가장 작을 때 이어 붙인다.
# 10 길이를 10개로 쪼개서 붙이면 너무 복잡해짐
# 1번 자른다 했을 떄 5 5 를 만들어야하는데
# 2 2 2 2 2 => 2 4 4 => 6 4 로 만들어짐
# 1 짜리 10개를 5 5 씩 맞추는 로직을 작성하는거 보다 자르는게 더 쉽지않을까?

# 코드 작성






# ==================================================
# import sys
# _input = sys.stdin.readline
# def minput(): return map(int, _input().split())

# def build_tree(size):
#     for i in range(size-1, 0, -1):
#         l = seg_tree[i*2]
#         r = seg_tree[i*2+1]
#         if l[0] > r[0]:
#             seg_tree[i] = [r[0], r[1], r[2], r[3]]
#         elif l[0] < r[0]:
#             seg_tree[i] = [l[0], l[1], l[2], l[3]]
#         else:
#             if l[1] < r[1]:
#                 seg_tree[i] = [r[0], r[1], r[2], r[3]]
#             else:
#                 seg_tree[i] = [l[0], l[1], l[2], l[3]]

# def update_tree(i):
#     while i > 1:
#         i //= 2
#         l = seg_tree[i*2]
#         r = seg_tree[i*2+1]
#         if l[0] > r[0]:
#             seg_tree[i] = [r[0], r[1], r[2], r[3]]
#         elif l[0] < r[0]:
#             seg_tree[i] = [l[0], l[1], l[2], l[3]]
#         else:
#             if l[1] < r[1]:
#                 seg_tree[i] = [r[0], r[1], r[2], r[3]]
#             else:
#                 seg_tree[i] = [l[0], l[1], l[2], l[3]]

# L, K, C = minput()
# arr = sorted(list(set(list(minput())+[L])))
# # print(arr)
# logN = (10000).bit_length()
# size = 2**logN
# INF = int(1e9)
# seg_tree = [[INF, 0, 0, 0] for _ in range(size * 2)] # [두 나무조각의 합, 리프노드 위치, 왼쪽조각, 오른쪽조각]
# pieces = [0] * 10001
# bonded = [False] * 10001
# cur = 0

# num_of_pieces = 0
# for i, cut in enumerate(arr):
#     pieces[i] = cut- cur
#     num_of_pieces += 1
#     cur = cut

# for i in range(10000):
#     if pieces[i+1]:
#         seg_tree[size+i] = [pieces[i] + pieces[i+1], i, i-1, i+1]
#     else:
#         break

# build_tree(size)

# # K 개 위치 C 번 자를 수 있다
# # 실제로 자를 수 있는 횟수는
# # 자를수 있는 횟수, 자를 수 있는 위치의 개수 중 최소값
# cuts = min(C, len(arr)-1)

# # 자를 수 있는 위치보다 자를 수 있는 횟수가 많은 경우 다 자름
# if K <= C:
#     print(max(pieces), arr[0])
# else:
#     # cuts 만큼 자르는데
#     # cuts 만큼 자르면 cuts+1 개의 나무조각이 만들어짐
#     while num_of_pieces > cuts+1:
#         # print("pieces ", num_of_pieces, "cuts ", cuts)
#         # print(seg_tree[size:size+10])
#         # 최소합 나무조각 2개 합치기
#         length, idx, left, right = seg_tree[1]
#         # print(seg_tree[1])
#         bonded[idx] = True
#         pieces[idx] = length
#         pieces[idx+1] = length
#         seg_tree[size+idx] = [INF, 0, 0, 0]
#         if left >= 0:
#             seg_tree[size+left][0] = pieces[left] + pieces[idx]
#             seg_tree[size+left][3] = right
#             update_tree(size+left)
#         if seg_tree[size+right][0] != INF:
#             seg_tree[size+right][0] = pieces[idx+1] + pieces[right+1]
#             seg_tree[size+right][2] = left 
#             update_tree(size+right)

#         update_tree(size+idx)
#         num_of_pieces -=1 
    
#     result = [max(pieces), 0]
#     for i in range(10001):
#         if not bonded[i]:
#             result[1] = arr[i]
#             break
#     print(*result)

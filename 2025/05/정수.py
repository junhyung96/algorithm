# 풀이 날짜 및 소요 시간
# 2025-05-08 14:10 ~ 2025-05-16 17:50

# 문제 요약
# 정수 N, K 가 주어짐
# 다음 조건을 만족하는 수를 출력
# N 보다 크거나 같은 정수 중
# 서로 다른 K 개의 수로 이루어진 수 중
# 가장 작은 수

# 입력 예제
# 47 1 // 55
# 12364 3 // 12411
# 7 3 // 102

# 입력 범위 및 조건
# N 1~10^18
# K 1~10

# 풀이 방법 및 시간, 공간복잡도 계산
# 서로다른 K개의 수를 선택하는 방법.
# 우선 현재 입력된 N 이 조건을 만족하는지
# 조건을 만족하지 않는다면
# 1. 자리 수를 바꾸어야만 하는지
#    9999 2 처럼 무조건 10000 이상으로 자리수가 늘어나거나
#    7 3 처럼 세자리수가 되기위해선 100 이상으로 자리수가 늘어나거나
#    29888 5 처럼 298?? 남은 수로 더 이상 크게 못만들 때 ( 현재 수를 기준으로 채워나가다가 K 가 제시된 것 보다 작게 나오면 )
# 2. 가장 큰 자리수가 변경되야 하는지
#    12300 1 처럼 하나의 수로 표현하기 위해선 11111 은 안되니 22222가 되어야 함
# 자리 수가 늘어나든 그대로든 기준이 되는 수가 있어야 함
# 7 3 이면 N의 자리수 보다 K 가 크므로 3자리수 100을 기준으로 두고 100 보다 크거나 같은으로 시작
# 12364 3 이면 N의 자리수가 K 보다 크므로 12364를 그대로 기준으로 두고 시작
# 가장 큰 자리수의 값을 우선적으로 선점
# 그다음 자리수를 순차적으로 탐색
# 기준이 되는 수보다 크거나 같은 

# N 과 K 로 기준이 되는 수를 만들고
# 기준이 되는 수가 조건을 만족하는지 검증한 후
# 조건에 맞는 수를 만들어내기

# dfs 하면 어떨까?
# 가장 큰 자리수 부터 넣고 집합 만들고 

# 코드 작성
import sys
from collections import defaultdict
_input = sys.stdin.readline
def minput(): return map(int, _input().split())
max = 20
N, K = minput()
nth_power = [0] * max
for i in range(max):
    nth_power[max-1-i] = 10 ** (i)

# 재귀 함수. 조건에 맞는 수를 반환
# 재귀 로직
# 함수 - 자리수 찾아서 반환 - 큰 수 찾아서 반환

def find_num(id, bit_mask, is_big):
    # print(id, bit_mask, is_big)
    # print(dp[id-1][bit_mask][is_big])
    cnt = 0
    for i in range(10):
        if bit_mask & 1<<i:
            cnt += 1
    
    if cnt > K:
        return -1
    # print(cnt)
    pre = dp[id-1][bit_mask][is_big]

    # 끝에 도달했다면 해당 수를 반환
    if id == max:
        # print(dp[id-1][bit_mask][is_big])
        if cnt == K and pre >= N:
            return pre
        else:
            return -1
    
    s = num_N[id] if not is_big else 0
    
    
    # 첫 번째 자리수 찾기
    if num_N[id] == -1:
        f_num = find_num(id+1, bit_mask, is_big)
        if f_num != -1:
            return f_num
        # 기존 N 보다 자리수가 증가한 케이스 9999 2 처럼 4자리로는 더 이상 큰 수를 만들 수 없을 때
        s = 1
        bit_mask = bit_mask | 1<<1
        is_big = True
        # print(id, bit_mask, is_big)
        dp[id][bit_mask][is_big] = nth_power[id]
        f_num = find_num(id+1, bit_mask, is_big)
        if f_num != -1:
            return f_num
    # 이미 큰 수 일 때
    if is_big:
        # 횟수가 남아 있다면
        if cnt < K:
            # 1000234 를 만들어야 한다고 했을때
            if K-cnt < max-id:
                dp[id][bit_mask | 1<<0][is_big] = pre + 0 * nth_power[id]
                f_num = find_num(id+1, bit_mask | 1 << 0, is_big)
                if f_num != -1:
                    return f_num
            else:
                for i in range(10):
                    if bit_mask & 1<<i:
                        continue
                    else:
                        break
                dp[id][bit_mask | 1<<i][is_big] = pre + i * nth_power[id]
                f_num = find_num(id+1, bit_mask | 1 << i, is_big)
                if f_num != -1:
                    return f_num    
        # 남은 수가 없다면 사용한 수 중 가장 작은거
        else:
            for i in range(10):
                if bit_mask & 1<<i:
                    break
            
            dp[id][bit_mask | 1<<i][is_big] = pre + i * nth_power[id]
            f_num = find_num(id+1, bit_mask | 1 << i, is_big)
            if f_num != -1:
                return f_num
    else:
        for i in range(s, 10):
            if not is_big and i > num_N[id]:
                is_big = True
            dp[id][bit_mask | 1<<i][is_big] = pre + i * nth_power[id]
            f_num = find_num(id+1, bit_mask | 1 << i, is_big)
            if f_num != -1:
                return f_num

    return -1

num_N = [-1] * max
# dp[n번째 자리수][비트마스킹][큰 수인가] = 만들어진 수
dp = [[[0, 0] for _ in range(1<<10)] for _  in range(max)]
num = N
# 써야할 수의 개수보다 자리수가 적으면 10**(K-1) 로 변경
if num < 10**(K-1):
    num = 10**(K-1)
N = num
i = max-1
while num > 0:
    num_N[i] = num % 10
    num //= 10 
    i -= 1
# print(N)
# print(num_N)
print(find_num(0, 0, False))

# n = N
# length = 0
# while n > 0:
#     num[length][0] = n % 10
#     n //= 10
#     length += 1
# # print(length)
# arr = [[-1, 0, 0] for _ in range(20)] # arr[i] = [i번째 자리수, 사용했던 서로다른 수 비트마스킹, 사용한 수 개수]
# INF = 10**19
# result = 10**19
# find_num(arr, max(length, K)-1, False, K)
# if result == INF:
#     find_num(arr, max(length, K), False, K)
# print(result)
# def make_number(arr, K, length):
#     cnt = 0
#     is_big = False # 큰 수가 되었는가? 큰 자리수에서 변경이 있어서 이미 큰 수라 아랫자리수는 작은수들로만 채워도 됨
#     for i in range(17, -1, -1):
#         a, group = arr[i]
        
#         # K 자리순데 N 이 K 자리수보다 작은 자리수일 때
#         if a == -1 and i+1 == K:
#             arr[i][0] = 1
#             arr[i][1] = 1<<1
#             cnt += 1
#             is_big = True
#             continue
        
#         # n자리 수보다 큰 자리수 넘어가기
#         if a == -1 and i+1 > K:
#             continue
        
#         # print(i, arr[i], is_big)
#         # 큰 수가 아닐 때
#         if not is_big:
#             # 남아있을 때
#             if cnt < K:
#                 # 현재 자리수 보다 큰 사용하지 않은 수
#                 for num in range(a+1, 10):
#                     if not(arr[i+1][1] & (1<<num)):
#                         break
#                 else:
#                     num = a
#                 # 큰 수를 만들기 위해서
#                 # 13244 cnt
#                 # cnt 가 하나 남았으면 1을 2로 올려야 함
#                 # cnt 가 둘 이상이면 1 그대로 감
#                 # 13244 2 => 13311
#                 # 547 3 => 5??
#                 # print('a')
#                 if K-cnt == 1:
#                     # print('b')
#                     if i > 0 and arr[i][0] >= arr[i-1][0]:
#                         if not(arr[i+1][1] & 1<<arr[i][0]):
#                             arr[i][1] = arr[i+1][1] | 1<<arr[i][0]
#                             cnt += 1
#                             is_big = True
#                         else:
#                             arr[i][1] = arr[i+1][1]
#                     else:
#                         # i == 0 이거나 arr[i][0] 이 arr[i-1][0] 보다 작거나 같은은 경우
#                         # print(num)
#                         if num > arr[i][0]:
#                             is_big = True
#                         arr[i][0] = num
#                         if not(arr[i+1][1] & 1<<arr[i][0]):
#                             arr[i][1] = arr[i+1][1] | 1<<arr[i][0]
#                             cnt += 1
#                         else:
#                             arr[i][1] = arr[i+1][1]
#                 # 현재 그룹에 속하지 않는 최소값
#                 # 13399 2 => 14111
#                 # 13399 3 => 13411
                
#                 # K-cnt > 1 일 때
#                 else:
#                     # print('c')
#                     # 자리수에 압박을 받을 때 안받을 때
#                     # print(i, K, cnt)
                    
#                     if i+1 > K-cnt:
#                         if not (arr[i+1][1] & 1<<arr[i][0]):
#                             cnt += 1
#                             arr[i][1] = arr[i+1][1] | 1<<arr[i][0]
#                         else:
#                             arr[i][1] = arr[i+1][1]
#                     else:
#                         if i > 0 and arr[i][0] >= arr[i-1][0]:
#                             for num in range(a, 10):
#                                 if not(arr[i+1][1] & (1<<num)):
#                                     break
#                             else:
#                                 for num in range(10):
#                                     if not(arr[i+1][1] & (1<<num)):
#                                         break
#                                 j = i+1
#                                 while True:
#                                     arr[j][0] += 1
#                                     if arr[j][0] == 10:
#                                         arr[j][0] = 0
#                                         j += 1
#                                     else:
#                                         break
#                             # print(arr[i][0] ,"here", num)
#                             arr[i][0] = num
#                             if not (arr[i+1][1] & 1<<arr[i][0]):
#                                 cnt += 1
#                                 arr[i][1] = arr[i+1][1] | 1<<arr[i][0]
#                             else:
#                                 arr[i][1] = arr[i+1][1]
#                         else:
#                             is_valid = False
#                             if i > 0:
#                                 for num in range(10):
#                                     if not(arr[i+1][1] & 1<<num) and num >= arr[i-1][0]:
#                                         is_valid = True
#                                         break
#                             if is_valid:
#                                 for num in range(a, 10):
#                                     if not(arr[i+1][1] & (1<<num)):
#                                         break
#                                 # print(arr[i][0] ,"here", num)
#                                 arr[i][0] = num
#                                 cnt += 1
#                                 arr[i][1] = arr[i+1][1] | 1<<arr[i][0]
#                             else:
#                                 for num in range(a+1, 10):
#                                     if not(arr[i+1][1] & (1<<num)):
#                                         break
#                                 arr[i][0] = num
#                                 cnt += 1
#                                 arr[i][1] = arr[i+1][1] | 1<<arr[i][0]
#                                 is_big = True
                            
                            
                    
#             # 없을 때
#             else:
#                 for num in range(10):
#                     # 사용한 수 중 가장 작은 것
#                     if arr[i+1][1] & 1<<num:
#                         break
#                 # print(num)
#                 arr[i][0] = num
#                 arr[i][1] = arr[i+1][1]

#         # 이미 큰 수일 때
#         else:
#             # 남아 있을 때
#             if cnt < K:
#                 # print("remain cnt")
                
#                 used_min = -1
#                 for num in range(10):
#                     # 이미 사용한 숫자 지나가기
#                     if arr[i+1][1] & 1<<num:
#                         if used_min == -1:
                         
#                             used_min = num
#                         continue
#                     else: 
#                         break
#                 # print(i, used_min, num)
#                 # 남은 자리수에 맞춰서 작은 수부터 배치
#                 if K-cnt < i+1:
                    
#                     if used_min == -1:
#                         arr[i][0] = num
#                         arr[i][1] = arr[i+1][1] | 1<<num
#                         cnt += 1
#                     else:
#                         arr[i][0] = used_min
#                         arr[i][1] = arr[i+1][1]
#                 else:
#                     # 사용안한 수 중 가장 작은 수 사용하기
#                     arr[i][0] = num
#                     arr[i][1] = arr[i+1][1] | 1<<num
#                     cnt += 1
#             # 없을 때
#             else:
#                 # print("no cnt")
#                 for num in range(10):
#                     # 사용한 수 중 가장 작은 것
#                     if arr[i+1][1] & 1<<num:
#                         break
#                 # print(num)
#                 arr[i][0] = num
#                 arr[i][1] = arr[i+1][1]
#         print(cnt, arr[i])
#     # print(cnt)
#     if cnt < K:
#         return False
#     return True


# N, K = minput()
# arr = [[-1, 0] for _ in range(20)] # arr[i] = [i번째 자리수, 사용했던 서로다른 수 비트마스킹]

# cal_N = N
# i = 0
# while cal_N >= 1:
#     x = cal_N % 10
#     cal_N //= 10
#     arr[i][0] = x
#     i += 1

# length = i
# # print(length)
# while True:
# # for _ in range(2):
#     if make_number(arr, K, length):
#         break
#     answer = ""
#     for a in arr[::-1]:
#         if a[0] == -1:
#             continue
#         answer += str(a[0])
#     # print(answerdktk)
#     # print(arr)
#     is_big = False
#     for i in range(17, -1, -1):
#         if arr[i][0] == -1:
#             continue
#         if not is_big:
#             arr[i][0] += 1
#             arr[i][1] = 0
#             if i<17 and arr[i][0] == 10:
#                 arr[i+1][0] = 1
#                 arr[i+1][1] = 0
#                 arr[i][0] = 0
#                 arr[i][1] = 0
#             is_big = True
#         else:
#             arr[i][0] = 0
#             arr[i][1] = 0
#     # print("c", arr)
    
# # 정답 출력
# answer = ""
# for a in arr[::-1]:
#     if a[0] == -1:
#         continue
#     answer += str(a[0])
# print(answer)



            # if cnt < K:
            #     if arr[i][0] == -1:
            #         continue
            #     print(i, arr[i], cnt, K)
            #     if K-cnt == 1:
            #         # 현재 4 이고 7를 바라봐
            #         # 7 보다 크거나 같은 수를 이미 사용했다면 그대로 아니면 +1
            #         if i>0 and arr[i-1][0] > arr[i][0]:
            #             arr[i][0] += 1
            #             is_big = True
            #             arr[i][1] = arr[i+1][1] | 1<<arr[i][0]
            #             cnt += 1
            #         else:
            #             arr[i][1] = arr[i+1][1]
            #             if not (arr[i+1][1] & 1<<arr[i][0]):
            #                 arr[i][1] = arr[i+1][1] | 1<<arr[i][0]
            #                 cnt += 1
            #     else:
            #         # 횟수가 남았을 때
            #         # 현재 수 보다 같거나 큰 사용하지 않은 수 
            #         # 현재 수가 9라면 그냥 9를 써야함
            #         # 2 4 6 이런식이면
            #         # cnt 가 2 남았다 근데 이미 4, 6은 썼음
            #         # 2쓰면서 cnt 1개 쓰고 
            #         if i>0 and arr[i-1][0] > arr[i][0]:
            #             arr[i][0] += 1
            #             is_big = True
            #             arr[i][1] = arr[i+1][1] | 1<<arr[i][0]
            #             cnt += 1
            #         else:
            #             arr[i][1] = arr[i+1][1]
            #             if not (arr[i+1][1] & 1<<arr[i][0]):
            #                 arr[i][1] = arr[i+1][1] | 1<<arr[i][0]
            #                 cnt += 1
            #         # 남은 자리수 cnt 비교해서 작은수부터 차례대로 채워야함
            #         # 하지만 아직 큰 수가 아님
            #         arr[i][1] = arr[i+1][1] | 1<<arr[i][0]
            #         if not (arr[i+1][1] & 1<<arr[i][0]):
            #             cnt += 1
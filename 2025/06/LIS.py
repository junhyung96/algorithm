# 풀이 날짜 및 소요 시간
# YYYY-MM-DD HH:MM ~ HH:MM

# 문제 요약

# 입력 예제

# 입력 범위 및 조건

# 풀이 방법 및 시간, 공간복잡도 계산
# 3 1 2 => 3, 3-1, 3-1-2
# 0 1 2 => 1, 1-2
# 0 0 2 => 2
# 각각의 최장길이 구하기
# 1 1 2 
# 1 2
# 1
# 합계 8

# 코드 작성
import sys
_input = sys.stdin.readline
def minput(): return map(int, _input().split())

def binary_search(arr, value):
    e = len(arr)-1
    s = 0
    while s < e:
        mid = (s+e) // 2
        if arr[mid] >= value:
            e = mid
        else:
            s = mid+1

    return s 


T = int(_input())
output = []

for tc in range(1, T+1):
    N = int(_input())
    arr = [0] + [int(_input()) for _ in range(N)]
    # 가장 긴 부분 수열 마지막 원소
    elements = [[0] for _ in range(N+1)]

    cnt = 0
    max_cnts = [0] * (N+1) # max_cnts[i] = i번째 수로 시작하는 부분수열을 갱신하면서 cnt 더해주기
    # 3 1 2 부분수열 3 => 3-1 => 3-1-2 
    # max_cnts[i] = 1 => 1 => 2 
    # cnt += 1, cnt += 1, cnt += 2
    for i in range(1, N+1):
        num = arr[i]
        for j in range(1, i+1):
            # 이분 탐색으로 elements 에 들어갈 곳 찾기
            if i == j:
                elements[j].append(num)
                max_cnts[j] = 1
                cnt += 1
                continue

            if elements[j][-1] == num:
                continue
            
            if elements[j][-1] < num:
                elements[j].append(num)
                max_cnts[j] += 1
                cnt += max_cnts[j]
                continue

            idx = binary_search(elements[j], num)
            # print(idx)
            elements[j][idx] = num
            cnt += max_cnts[j]

    # print(elements)
    # print(max_cnts)
    output.append("Case #" + str(tc) + ": " + str(cnt))

print("\n".join(output))
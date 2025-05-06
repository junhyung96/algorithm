# 풀이 날짜 및 소요 시간
# 2025-05-06 21:24 ~ HH:MM

# 문제 요약
# N 개의 병이 있다
# 각 병에는 몇 % 용액 몇 L 가 들어있는지 적혀있다.
# N 개의 병 중 몇 개를 골라 M % 용액을 만드려고 한다
# 최대 몇 L 를 얻을 수 있는지 출력하라 ( 병 하나를 통째로 써야 하는건 아니다 )
# 오차 허용 10^-2 까지

# 입력 예제
# 2 50
# 0 20
# 100 30
# // 40.00

# 입력 범위 및 조건
# N 1 ~ 50
# M 0 ~ 100
# 용액의 양 : 1 ~ 1000

# 풀이 방법 및 시간, 공간복잡도 계산
# 용액 농도 순으로 정렬해서
# 양쪽 끝 인덱스 두개를 시작점으로 해서
# 섞어서 M % 용액을 만들고 다쓰면 포인터를 옮기는 식으로

# 현재 코드가 틀린 이유
# 많은 양을 만들어야함
# 최대한 농도차가 적은걸로 많은 양을 소모시키는게 최적임

# 코드 작성
import sys
_input = sys.stdin.readline
def minput(): return map(int, _input().split())

N, M = minput()
solutions = [list(minput()) for _ in range(N)]
solutions.sort()

def make_solution(l, r, M):
    # 1. 0 <= l, r < N
    # 2. conc_l < M, conc_r > M
    # 3. l != r
    # 만족하는 경우에만 호출
    conc_a, vol_a = solutions[l]
    conc_b, vol_b = solutions[r]

    # M = (conc_a * vol_a + conc_b * X) / (vol_a +  X)
    # M = (conc_a * Y + conc_b * vol_b) / (Y +  vol_b)
    # 위 식을 만족하는 X 혹은 Y 가 있다면 그것을 반환
    b_X = (M*vol_a - conc_a*vol_a) / (conc_b - M)
    a_Y = (M*vol_b - conc_b*vol_b) / (conc_a - M)

    # 한 쪽이 넘치는 경우
    if b_X > vol_b: 
        return a_Y, vol_b
    if a_Y > vol_a:
        return vol_a, b_X
    # 같은 양일 경우
    else:
        return a_Y, b_X

# N == 1
if N == 1:
    if solutions[0][0] == M:
        print(solutions[0][1])
    else:
        print(0)
    exit()

# N >= 2

# 두 포인터
l = -1
r = 0
for i in range(1, N):
    l += 1
    r += 1
    if solutions[i][0] >= M:
        break
# print(l, r)
result = 0.0

while True:
    if l < 0 and r >= N:
        break

    usage_A, usage_B = 0, 0
    # M 을 만들 수 있는 농도가 다른 두 용액
    if l != r and l >= 0 and r < N and solutions[l][0] < M and solutions[r][0] > M:
        usage_A, usage_B = make_solution(l, r, M)
        # print(l, r, usage_A, usage_B)
        solutions[l][1] -= usage_A
        if solutions[l][1] == 0:
            l -= 1

        solutions[r][1] -= usage_B
        if solutions[r][1] == 0:
            r += 1

    # M 인 용액
    while l >= 0 and solutions[l][0] == M:
        usage_A += solutions[l][1]
        l -= 1
    while r < N and solutions[r][0] == M:
        usage_B += solutions[r][1]
        r += 1
    
    if usage_A == 0 and usage_B == 0:
        break

    result += usage_A + usage_B
    

print(round(result, 14))

# import sys
# _input = sys.stdin.readline
# def minput(): return map(int, _input().split())

# def make_solution(l, r, M):
#     conc_a, vol_a = solutions[l]
#     conc_b, vol_b = solutions[r]
    
#     if conc_a > M and conc_b > M:
#         return False, 0, 0
#     elif conc_a < M and conc_b < M:
#         return False, 0, 0
#     elif conc_a == M and conc_b != M:
#         return True, vol_a, 0
#     elif conc_a != M and conc_b == M:
#         return True, 0, vol_b
#     elif conc_a == M and conc_b == M:
#         return True, vol_a, 0
    
#     if l >= r:
#         return False, 0, 0
#     # a 용액, b 용액 사용량을 어떻게 측정해야 하나
#     # 한 쪽 용액을 무조건 다 쓸 수 밖에 없다
#     # M = (conc_a * vol_a + conc_b * X) / (vol_a +  X)
#     # M = (conc_a * Y + conc_b * vol_b) / (Y +  vol_b)
#     # 위 식을 만족하는 X 혹은 Y 가 있다면 그것을 반환
#     b_X = (M*vol_a - conc_a*vol_a) / (conc_b - M)
#     a_Y = (M*vol_b - conc_b*vol_b) / (conc_a - M)
#     # print(a_Y,b_X)
#     # A 를 다 썼을 떄 B 의 양이 많다면
#     # B 의 양을 다 썼을 떄 A 를 반환
#     if b_X > vol_b: 
#         return True, a_Y, vol_b
#     if a_Y > vol_a:
#         return True, vol_a, b_X
#     if a_Y == vol_a and b_X == vol_b:
#         return True, a_Y, b_X
    
# N, M = minput()
# solutions = [list(minput()) for _ in range(N)]
# solutions.sort()

# # 두 포인터
# l = 0
# r = N-1

# result = 0.0

# while l <= r:
# # for _ in range(3):
#     # print(l, r)
#     is_possible, usage_a, usage_b = make_solution(l, r, M)
    
#     if not is_possible:
#         break

#     solutions[l][1] -= usage_a
#     solutions[r][1] -= usage_b
#     result += usage_a + usage_b
#     # print (solutions[l], solutions[r])
#     if solutions[l][1] == 0:
#         l += 1
#     if solutions[r][1] == 0:
#         r -= 1

# print(round(result, 14))
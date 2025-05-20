# 풀이 날짜 및 소요 시간
# 2025-05-20 21:53 ~ HH:MM

# 문제 요약
# N 개의 수 
# 쿼리 2가지
# 수 변경
# 구간 합 구하기

# 입력 예제
# 5 2 2
# 1
# 2
# 3
# 4
# 5
# 1 3 6
# 2 2 5
# 1 5 2
# 2 3 5

# 입력 범위 및 조건
# N 1 ~ 1,000,000
# M 1 ~ 10,000
# K 1 ~ 10,000

# 풀이 방법 및 시간, 공간복잡도 계산

# 코드 작성
import sys
_input = sys.stdin.readline
def minput(): return map(int, _input().split())

class FanwickTree():
    def __init__(self, size):
        self.size = size
        self.arr = [0] * (size+1)
    
    def update_tree(self, id, delta):

        while id <= self.size:
            self.arr[id] += delta
            id += (id & -id)

    def get_sum(self, id):
        tmp = 0

        while id > 0:
            tmp += self.arr[id]
            id -= id & (-id)
        
        return tmp

N, M, K = minput()
BIT = FanwickTree(N)
nums = [0] + [int(_input()) for _ in range(N)]

for i, v in enumerate(nums):
    if i == 0:
        continue
    BIT.update_tree(i, v)
    
for _ in range(M+K):
    q, a, b = minput()

    if q == 1:
        pre = nums[a]
        nums[a] = b
        BIT.update_tree(a, b-pre)
    else:
        
        print(BIT.get_sum(b) - BIT.get_sum(a-1))
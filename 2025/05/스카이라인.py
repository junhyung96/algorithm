# 풀이 날짜 및 소요 시간
# 2025-05-04 19:00 ~ 19:36

# 문제 요약
# N 개의 직사각형 모양의 건물이 주어짐. 같은 높이의 지면에 지어져있음
# 스카이라인. 건물 전체의 윤곽을 알고 싶다.
# 높이가 변하는 좌표와 그 높이를 출력해야 함
# 같은 좌표에 여러 건물이 있다면 제일 큰 높이가 해당 좌표의 높이가 됨

# 입력 예제
# 8
# 1 11 5
# 2 6 7
# 3 13 9
# 12 7 16
# 14 3 25
# 19 18 22
# 23 13 29
# 24 4 28

# 입력 범위 및 조건
# N 1 ~ 100000
# x좌표, 높이 1 ~ 10억

# 풀이 방법 및 시간, 공간복잡도 계산
# 완전이진트리에 정보 넣고 계산하기

# 코드 작성
import sys
from collections import defaultdict
_input = sys.stdin.readline
def minput(): return map(int, _input().split())

def update_tree(idx, value):
    seg_tree[idx] = value

    while idx > 1:
        idx //= 2
        seg_tree[idx] = max(seg_tree[idx*2], seg_tree[idx*2+1])

N = int(_input())
logN = (100000).bit_length()
size = 2 ** logN
seg_tree = [0] * 2 * size # [높이]
update_list = defaultdict(list) # update_list[입력좌표(왼쪽)] = [(오른쪽좌표, 높이), ...]
delete_list = defaultdict(list) # delete_list[제거좌표(오른쪽)] = [세그먼트트리에서의 좌표, ...]
seg_id = size

xs = []
for _ in range(N):
    l, h, r = minput()
    xs.append(l)
    xs.append(r)
    update_list[l].append((r, h))

xs.sort()
# log N * N * 2 
cur_h = 0
for i in xs:
    # 건물 정보 등록
    for r, h in update_list[i]:
        update_tree(seg_id, h)
        delete_list[r].append(seg_id)
        seg_id += 1

    # 건물 정보 삭제
    for r in delete_list[i]:
        update_tree(r, 0)

    # 현재 높이 이전 높이 비교 및 출력
    if cur_h != seg_tree[1]:
        cur_h = seg_tree[1]
        print(i, seg_tree[1], end=" ")
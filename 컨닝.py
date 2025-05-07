# 풀이 날짜 및 소요 시간
# YYYY-MM-DD HH:MM ~ HH:MM

# 문제 요약
# 시험 자리 배치
# 양옆과 대각선 위 두방향은 무조건 컨닝을 한다고 볼 때
# 주어진 책상 정보( 앉을 수 있으면 . 앉을 수 없으면 X )를 보고 최대 몇 명을 배치할 수 있는지 출력

# 입력 예제
# 4
# 2 3
# ...
# ...
# 2 3
# x.x
# xxx
# 2 3
# x.x
# x.x
# 10 10
# ....x.....
# ..........
# ..........
# ..x.......
# ..........
# x...x.x...
# .........x
# ...x......
# ........x.
# .x...x....

# 입력 범위 및 조건
# N, M 1 ~ 10
# 메모리 512MB, 시간 2초

# 풀이 방법 및 시간, 공간복잡도 계산
# 가로 행, 세로 열
# students[i][j] = i행에 학생들을 j 모양으로 배치한다
# i = 0, j = 21 (2진수 0000010101) 처럼 앉게 하겠다.
# i 다채우고 i+1 을 i 를 근거로 해서 다 채우는

# 방법 앉을 수 있는 자리에
# 컨닝이 불가능하도록 배치가 가능한 모든 조합을 만듬
# students[줄][조합] = 최대 인원
# 아래 과정을 반복
# students[i][조합] 을 순회하면서
# students[i+1][조합] 에 최대 인원을 갱신


# 코드 작성
import sys
from collections import defaultdict, deque
_input = sys.stdin.readline
def minput(): return map(int, _input().split())

def make_group():
    q = deque() # [그룹비트마스크, 탐색할 인덱스]
    q.append([0, 1])
    q.append([1, 1])
    group_people[1<<0] = 1
        
    while q:
        group, vi = q.popleft()
        if vi >= 10:
            continue

        # 연속된 자리는 피하기. 앉지 않는다만 추가
        if group and group & 1<<(vi-1):
            q.append([group, vi+1])
        # 이전 자리 배치 안했으면 앉는다, 앉지 않는다 두 선택지 모두 추가
        else:
            q.append([group, vi+1])
            q.append([group|1<<vi, vi+1])
            if group:
                group_people[group|1<<vi] = group_people[group] + 1
            else:
                group_people[group|1<<vi] = 1

def make_row_group(i):
    cur_row = graph[i] # 자리모양 ....X.....
    q = deque() # [그룹비트마스크, 탐색할 인덱스]
    if cur_row[-1] == "x":
        q.append([0, 1])
    else:
        q.append([0, 1])
        q.append([1, 1])
        students[i][1<<0] = 1
        
    while q:
        group, vi = q.popleft()
        if vi >= len(cur_row):
            continue

        if cur_row[-(vi+1)] == "x": # 비트마스크 모양으론 0이 오른쪽 첫번째니까 거꾸로 탐색
            q.append([group, vi+1])
        else:
            # 연속된 자리는 피하기. 앉지 않는다만 추가
            if group and group & 1<<(vi-1):
                q.append([group, vi+1])
            # 이전 자리 배치 안했으면 앉는다, 앉지 않는다 두 선택지 모두 추가
            else:
                q.append([group, vi+1])
                q.append([group|1<<vi, vi+1])
                if group:
                    students[i][group|1<<vi] = students[i][group] + 1
                else:
                    students[i][group|1<<vi] = 1
    
def set_max_people(i, M):
    for front_group in students[i-1]:
        for cur_group in students[i]:
            for cur in range(M):
                # 현재 그룹의 해당 자리에 학생이 앉아 있을 때
                if cur_group & (1 << cur):
                    # 대각선 왼쪽, 오른쪽 앞이 앉아 있다면 불가능한 경우
                    # 왼쪽은 cur+1 이고 cur < M 오른쪽은 cur-1 이고 cur >= 0
                    if (cur < M-1 and front_group & (1<<(cur+1))) or (cur > 0 and front_group & (1<<(cur-1))):
                        break
            else:
                students[i][cur_group] = max(students[i][cur_group], students[i-1][front_group] + group_people[cur_group])
                max_value[0] = max(max_value[0], students[i][cur_group])
    # front 그룹은 무조건 있게끔 설정해둠
    # if not students[i]: # 아무도 안앉았을때
    students[i][0] = 0
    for front_group in students[i-1]:
        students[i][0] = max(students[i][0], students[i-1][front_group])

T = int(_input())
group_people = {} # 띄워 앉았을 때 해당 그룹 명수
make_group()
for tc in range(T):
    N, M = minput()
    graph = [_input().rstrip() for _ in range(N)]
    students = defaultdict(dict)
    max_value = [0]
    
    idx = 0
    while True:
        if idx == N:
            break
        make_row_group(idx)
        
        for group in students[idx]:
            max_value[0] = max(max_value[0], students[idx][group])

        if students[idx]:
            break 
        idx += 1
    
    for i in range(idx, N):
        # i번째 행 group 만들고
        make_row_group(i)
        # i-1번째 행과 비교해서 최대값 갱신
        set_max_people(i, M)
    # print(students)
    print(max_value[0])
    del students

# T = int(_input())
# group_people = {} # 띄워 앉았을 때 해당 그룹 명수
# make_group()
# for tc in range(T):
#     N, M = minput()
#     graph = [_input().rstrip() for _ in range(N)]
#     students = defaultdict(dict)
#     max_value = [0]
    
#     make_row_group(0)
#     for group in students[0]:
#         max_value[0] = max(max_value[0], students[0][group])
    
#     for i in range(1, N):
#         # i번째 행 group 만들고
#         make_row_group(i)
#         # i-1번째 행과 비교해서 최대값 갱신
#         set_max_people(i, M)
    
#     print(max_value[0])
#     del students

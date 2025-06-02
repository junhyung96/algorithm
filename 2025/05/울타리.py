# 풀이 날짜 및 소요 시간
# 2025-05-19 12:41 ~ HH:MM

# 문제 요약
# N 개의 나무가 평면좌표 위에 존재한다.
# 정원을 직사각형 모양의 울타리로 감싸야 하는데
# 존재하는 나무 중 몇 그루를 잘라 만들어야한다.
# 울타리는 존재하는 나무를 잘라서 만들며 
# 각 나무는 잘랐을 때 만들 수 있는 울타리 길이가 주어진다.
# 최소한의 나무를 잘라 울타리를 만들 때 몇 그루를 잘라야 하는가

# 입력 예제
# 5
# 1 1 1
# 2 8 1
# 8 2 1
# 9 9 1
# 5 5 32

# 입력 범위 및 조건
# N 2 ~ 40
# 이외의 값은 1,000,000 이하의 자연수
# 2초 128MB

# 풀이 방법 및 시간, 공간복잡도 계산
# N 개 중 1개 혹은 2개의 나무를 택해 울타리를 만들 수 있는지
# 만들 수 있다면 최소 몇 그루가 필요한지를 계산하여 답을 도출하기

# 코드 작성
import sys
_input = sys.stdin.readline
def minput(): return map(int, _input().split())
MAX = int(1e6)

def set_tree_sections(n):
    for i in range(n):
        for j in range(i+1, n):
            tree_sections[str(i)+"+"+str(j)] = MAX
            
    if n <= 3:
        return 
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j, n):
                tree_sections[str(i)+"+"+str(j)+"+"+str(k)] = MAX
    if n <= 4:
        return
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    tree_sections[str(i)+"+"+str(j)+"+"+str(k)+"+"+str(l)] = MAX
            
N = int(_input())
trees = [list(minput()) for _ in range(N)] # [x좌표, y좌표, 잘랐을 때 만들 수 있는 울타리 길이]
output = MAX
tree_sections = {} # { 선택된 두 나무 인덱스 : 자르는 나무 최소 개수 } 
set_tree_sections(N)
# ex) 0번, 1번 나무를 기준으로 울타리 영역을 만들었을 때 2그루를 제거해야한다면 { "0-1" : 2 } 

# 1 그루만 남겨 울타리 만들기
# 무조건 만들 수 있으니까 N-1 개의 나무를 자르는 것
output = N-1

# N 그루 중 2그루를 택해 울타리 만들기
for tree_section in tree_sections:
    id_ls = list(map(int, tree_section.split("+")))
    min_x, min_y, max_x, max_y = MAX, MAX, 0, 0
    for id in id_ls:
        xi, yi, l = trees[id]
        if xi < min_x:
            min_x = xi
        if xi > max_x:
            max_x = xi
        if yi < min_y:
            min_y = yi
        if yi > max_y:
            max_y = yi

    trees_in_the_area = []
    trees_outside_the_area = []
    # 0. 영역 안 밖 트리 구별하기
    for id in range(N):        
        if id in id_ls:
            continue
        # 영역 안 (a, b), (c, d) 라 하면
        x, y, l = trees[id]
        if min_x <= x <= max_x and min_y <= y <= max_y:
            trees_in_the_area.append(trees[id])
        else:
            trees_outside_the_area.append(trees[id])
    
    # 영역 만들기 가능한지 탐색
    # 1. 해당 영역이 필요한 울타리 길이 구하기
    required_length = 2 * (max_x - min_x) + 2 * (max_y - min_y)
    possible_length = 0
    
    # 2. 영역 밖의 트리 모두 제거해서 만들 수 있는 울타리 길이 구하기
    tree_cnt = len(trees_outside_the_area)
    
    for tree in trees_outside_the_area:
        possible_length += tree[2]
    
    if required_length <= possible_length:
        tree_sections[tree_section] = tree_cnt
        continue
    
    # 3. 부족하면 영역 내의 나무 중 울타리 만들 수 있는 나무 큰거부터 한 개씩 제거
    trees_in_the_area.sort(key=lambda x: x[2], reverse=True)
    for tree in trees_in_the_area:
        possible_length += tree[2]
        tree_cnt += 1
        
        if required_length <= possible_length:
            tree_sections[tree_section] = tree_cnt
            break

    # print("new area")
    # print(i, j)
    # print(required_length, possible_length)
    # print(tree_sections[tree_section], tree_cnt)
    # 4. 다 안되면 해당 영역은 불가능
    
for tree_section in tree_sections:
    # print(tree_section, tree_sections[tree_section])
    if not tree_sections[tree_section]:
        continue
    if output > tree_sections[tree_section]:
        output = tree_sections[tree_section]
        
print(output)
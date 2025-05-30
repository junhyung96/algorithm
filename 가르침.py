# 풀이 날짜 및 소요 시간
# 2025-05-29 14:35 ~ HH:MM

# 백트래킹.. K개의 알파벳를 가르칠수 있으니
# K개의 알파벳 조합이 갖춰졌을 때만 배울 수 있는 단어 탐색하기

# 문제 요약
# 어떤 K 개의 글자(알파벳)을 가르쳐서 읽을 수 있는 단어의 최대 개수
# 모든 글자는 anta 로 시작해서 tica 로 끝난다 ( a, n, t, i, c ) 필수 포함

# 입력 예제
# 3 6
# anta  r  ctica
# anta  hello  tica
# anta  c  artica
# ans: 2

# 입력 범위 및 조건
# 1초 128M
# N 1 ~ 50
# K 0 ~ 26
# 단어 8 ~ 15

# 풀이 방법 및 시간, 공간복잡도 계산
# 입력을 anta tica 를 제외한 문자로 저장
# 문자에 들어가는 알파벳 과 그 수를 저장
# 가르칠 수 있는 글자 수를 내에서 조합을 맞춰서 최대 개수 구하기
# 
# a n t i c 를 제외한 알파벳 21가지 
# 단어의 길이 최대 15.. 접두, 접미 제외 7자
# 단어를 최대 26자까지 가르칠 수 있음
# ..
# 가르칠 수 있는 글자가 5보다 작으면 기본 anta, tica 를 읽을 수 없으므로 0 return
# 각 단어는 어떤 알파벳이 쓰였는지를 키로 하여 맵으로 저장.. 값은 숫자 1 (임의의숫자) 굳이 각 알파벳이 몇 번 쓰였는지 알 필요는 없음
# antarctica = { a: 1, n: 1, t: 1, r: 1, c: 1, i: 1}
# 
# 알파벳 조합을 모두 만들어서 구하기는.. 조합 200만개 N 50 개 비교 1억번 연산
# 

# 코드 작성
import sys
from collections import defaultdict
_input = sys.stdin.readline
def minput(): return map(int, _input().split())

def valid_check(stack):
    global K
    cnt = 0
    for word in words:
        if not word:
            continue
        if len(stack) < len(word):
            continue
        for alp in word:
            if not stack.get(alp):
                break
        else:
            cnt += 1
            
    return cnt

def dfs():
    global output, K, max_L
    stack = []
    visited = defaultdict(bool)
    
    for idx, al in enumerate(alphabet):
        stack = [[al, idx]]
        stack_dict = {}
        stack_dict[al] = 1
        visited[al] = True
        
        while stack:
            al, vi = stack[-1]
            
            if len(stack) == K or len(stack) == len(alphabet):
                # print(stack)
                cnt = valid_check(stack_dict)
                output = max(output, cnt)
            if vi+1 < len(alphabet) and len(stack)+1 <= K:
                stack[-1][1] += 1
                stack_dict[alphabet[vi+1]] = 1
                stack.append([alphabet[vi+1], vi+1])
            else:
                al, vi = stack.pop()
                del stack_dict[al]
        
        visited[al] = False

N, K = minput()
max_L = 0
alphabet = {}

# a n t i c 를 못배우면 읽을 수 있는 글자가 없음
if K < 5:
    print(0)
    exit()
K -= 5

is_exist = False
words = [{} for _ in range(N)]
for i in range(N):
    word = _input().rstrip()
    word = word[4:][:-4]
    for al in word:
        if al in 'antic':
            continue
        words[i][al] = 1
        alphabet[al] = 1
    if len(words[i]) <= K:
        is_exist = True
    max_L = max(max_L, len(words[i]))

if not is_exist:
    print(0)
    exit()

default_cnt = 0
output = 0
for word in words:
    if len(word) == 0:
        default_cnt += 1
        
alphabet = tuple(alphabet)

if K == 0:
    print(default_cnt)
else:
    dfs()
    print(output+default_cnt)
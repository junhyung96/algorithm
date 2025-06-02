# 풀이 날짜 및 소요 시간
# 2025-05-26 14:52 ~ 15:00

# 문제 요약

# 입력 예제
# 5
# aa
# ab
# bb
# cc
# cd

# 입력 범위 및 조건

# 풀이 방법 및 시간, 공간복잡도 계산

# 코드 작성
import sys
from collections import defaultdict
_input = sys.stdin.readline
def minput(): return map(int, _input().split())

N = int(_input())
words = [_input().rstrip() for _ in range(N)]
words_modified = []

for word in words:
    al_to_num = defaultdict(int)
    cnt = 0
    new_word = ""
    for al in word:
        if not al_to_num[al]:
            cnt += 1
            al_to_num[al] = cnt
        new_word += str(al_to_num[al])
    words_modified.append(new_word)

output = 0
for i in range(N):
    for j in range(i+1, N):
        if words_modified[i] == words_modified[j]:
            output += 1
            
print(output)  
            
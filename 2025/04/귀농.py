# 풀이 날짜 및 소요 시간
# 2025-04-28 15:07 ~ 14:20

# 문제 요약
# NxN 그래프 각 1x1 영역에는 -1000~1000의 값이 들어있다.
# 꼭지점 하나에서 만나는 직사각형 둘
# 직사각형에 존재하는 모든 값의 합이 같도록하는 경우의 수.

# 입력 범위 및 조건
# 입력 N = 1 ~ 50
# 시간 1초 메모리 256MB

# 풀이 방법 및 시간, 공간복잡도 계산
# 그래프영역 2500칸.. 
# 브루트포스, 누적합
# x,y 좌표 기준 연산량 x * y + (50 - x) * (50 - y)
# 50*50 전부 돌면 = 312만
# 대각선 2번 => 624만

# 코드 작성
import sys
from collections import defaultdict
_input = sys.stdin.readline
def minput(): return map(int, _input().split())

N = int(_input())
graph = [[0]*(N+1)] + [[0] + list(minput()) for _ in range(N)] 

# 누적합 배열
graph_sum = [[0] * 100 for _ in range(100)]
# 직사각형 합 정보
sums = defaultdict(int)

for i in range(N+1):
    for j in range(N+1):
        graph_sum[i][j] = graph[i][j]
        graph_sum[i][j] += graph_sum[i][j-1] + graph_sum[i-1][j] - graph_sum[i-1][j-1]

result = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        # 1. 왼쪽위, 오른쪽밑 대각선
        
        # i, j 에서 비교 a, b ~ i, j 에 존재하는 직사각형 합들을 구한 뒤
        for a in range(1, i+1):
            for b in range(1, j+1):
                if i == a and j == b:
                    sums[graph[i][j]] += 1
                else:
                    sums[graph_sum[i][j] - graph_sum[i][b-1] - graph_sum[a-1][j] + graph_sum[a-1][b-1]] += 1

        # i+1, j+1 ~ x, y 에 존재하는 직사각형의 합으로 같은 값 찾으면 count++
        for x in range(i+1, N+1):
            for y in range(j+1, N+1):
                result += sums[graph_sum[x][y] - graph_sum[x][j] - graph_sum[i][y] + graph_sum[i][j]]
        # 해당 좌표 끝나면 딕셔너리 초기화
        sums.clear()
        
        # 2. 오른쪽위, 왼쪽밑 대각선
        for a in range(1, i+1):
            for b in range(j, N+1):
                if i == a and j == b:
                    sums[graph[i][j]] += 1
                else:
                    sums[graph_sum[i][b] - graph_sum[i][j-1] - graph_sum[a-1][b] + graph_sum[a-1][j-1]] += 1

        for x in range(i+1, N+1):
            for y in range(1, j):
                result += sums[graph_sum[x][j-1] - graph_sum[x][y-1] - graph_sum[i][j-1] + graph_sum[i][y-1]]
        # 해당 좌표 끝나면 딕셔너리 초기화
        sums.clear()
        
        
print(result)   
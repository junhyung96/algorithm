// 풀이 날짜 및 소요 시간
// 2025-06-12 21:52 ~ HH:MM

// 문제 요약
// N 명의 후보가 있다
// 1번 후보가 당선되기 위해서
// 나머지 후보를 지지하는 사람을 매수해야 한다.
// 매수해야하는 사람의 수의 최솟값을 출력

// 입력 예제
// 3
// 5
// 7
// 7
// ans: 2
// 2, 3번 후보에게서 각각 1명씩 매수

// 입력 범위 및 조건
// 2초 128MB
// N 1 ~ 50
// 득표수 1 ~ 100

// 풀이 방법 및 시간, 공간복잡도 계산
// 모든 호부의 득표수를 우선순위 큐에 넣고
// 현재 득표수가 가장 많은 후보에게서 1표씩 꺼내오기
// 1번 후보가 가장 많으면 스탑

// 코드 작성
#include <iostream>
#include <queue>

using namespace std;

int main()
{
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    priority_queue<pair<int, int>> max_priority_queue;
    cin >> N;
    int votes[N];
    int tmp;
    int cur;
    for (int i=1; i<N+1; i++){
        cin >> tmp;
        if (i == 1) cur = tmp;
        max_priority_queue.push({tmp, i});
    }
    int index, vote;
    int output = 0;
    while (true){
        vote = max_priority_queue.top().first;
        index = max_priority_queue.top().second;
        
        if (index == 1) break;

        max_priority_queue.pop();
        max_priority_queue.push({vote-1, index});
        cur++;
        output++;

        if (cur > max_priority_queue.top().first) break;

    }
    cout << output;
    return 0;
}
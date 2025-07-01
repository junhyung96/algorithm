// 풀이 날짜 및 소요 시간
// 2025-06-11 14:12 ~ HH:MM

// 문제 요약
// N 개의 마을에 M 개의 간선이 있다.
// 어떤 A 마을에서 어떤 B 마을로 못 가는 경우는 없다.
// 주어진 마을 간 거리를 만족하는 최소 개수의 간선일 때 모든 간선의 합을 출력하라.
// 간선은 양방향으로 오가는 거리가 같다.

// 입력 예제
// 5
// 0 6 15 2 6
// 6 0 9 8 12
// 15 9 0 16 18
// 2 8 16 0 4
// 6 12 18 4 0

// 입력 범위 및 조건
// N 1 ~ 20
// 이동거리 1 ~ 2500
// 2초 128MB

// 풀이 방법 및 시간, 공간복잡도 계산
// 플로이드 워셜 알고리즘으로 최단 거리를 구하면서 
// 어떤 마을 K 를 경유해서 A 에서 B 로 이동하는 거리가 주어진 거리와 같을 경우
// A 에서 B 로 가는 직통 간선을 제거
// 거리를 구하다가 주어진 거리보다 작은 거리가 존재할 경우 만족하지 못하므로 -1 을 출력
// O(N^3) 인 플로이드 워셜에서 N 이 20 이므로
// 순회하는 배열의 크기는 400 총 64,000,000 연산 필요

// 코드 작성
#include <iostream>

using namespace std;

int main()
{
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // 입력 받기
    int N;
    cin >> N;
    int adj_m[N][N] = {};
    for (int i=0; i<N; i++){
        for (int j=0; j<N; j++){
            cin >> adj_m[i][j];
        }
    }

    // 최소 거리 구하기
    // k 마을을 경유해서 가는 A -> B 마을 이동
    int dist = 0;
    bool is_valid = true;
    for (int k=0; k<N; k++){
        for (int a=0; a<N; a++){
            for (int b=0; b<N; b++){
                if (a == b || a == k || b == k) continue;
                if (adj_m[a][k] == 0 || adj_m[k][b] == 0) continue;

                dist = adj_m[a][k] + adj_m[k][b];
                if (dist == adj_m[a][b]) {
                    // cout << "same at: " << a << " " << b << "\n";
                    adj_m[a][b] = 0;
                    adj_m[b][a] = 0;
                } else if (dist < adj_m[a][b]){
                    // cout << k << " small at: " << a << " " << b << "\n";
                    is_valid = false;
                }
                
            }  
            if (!is_valid) break;  
        }
        if (!is_valid) break;  
    }
    
    if (!is_valid) {
        cout << -1;
        return 0;
    }
    
    // 간선 총합 구하기
    int output = 0;
    for (int i=0; i<N; i++){
        for (int j=0; j<N; j++){
            output += adj_m[i][j];
            // cout << adj_m[i][j] << " "; 
        }
        // cout << "\n";
    }
    cout << output/2;

    return 0;
}
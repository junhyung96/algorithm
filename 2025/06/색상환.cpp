// 풀이 날짜 및 소요 시간
// 2025-06-18 14:18 ~ 15:08
// 2025-06-1

// 문제 요약
// 모든 색 중에서 대표적인 20가지 색상을 색생환이라한다.
// 시각적으로 구별하기 위해 인접한 색상을 쓰지 않는다고 할 때
// N 개의 색으로 이루어진 색상환에서 인접한 색이 없도록 
// 서로 다른 K 개의 수를 고르는 경우의 수를 1,000,000,003 (10억 3) 으로 나눈 나머지를 출력

// 입력 예제

// 입력 범위 및 조건
// 1초 128MB
// N 4 ~ 1000
// K 1 ~ N

// 풀이 방법 및 시간, 공간복잡도 계산

// DFS 조합 만들기
// head, cur 을 두고
// nxt 가 head 와 cur 에 인접하지 않다면 추가하고 넘어가기
// 조합 DFS 시간복잡도.. 
// 1000! / ( 500! * 500! )
// 경우의 수를 10억3 으로 나눈다는 시점에서 브루트포스 불가능

// 개수를 nCr 등과 같은 계산적으로 구할 수 있는가
// 10 개 중 3개를 골라야 한다고 생각해보자
// 1 2 3 4 5 6 7 8 9 10
// 1 s3 e9 / 3 s5 e7 / k=5~9 sk e9 5개 
// 1 s3 e9 / 7 s7 e7 / k=9 s9 e9 1개 
// 2 s4 e10
// 3 s5 e10
// 1000개 중 300개 언저리로 조합을 짜야 한다..
// 298개를 찍어두고 2개는 1~N 의 합으로 구함.
// 구간 크기에서 특정 개수를 선택하는 경우의 수는 메모이제이션 되지 않을까?
// 구간 크기에서 특정 개수를 선택하는 경우의 수는 패턴을 보이지 않을까?
// 100 개 중 30개를 선택 end - 2n
// s1 e42 / s3 e44 / ..... / 
// 42 44 46 48 50
// ...
// 92 94 96 98 100

// 다이나믹 프로그래밍
// K개를 고르는 경우의 수
// 어떻게 점화식을 세울 것이냐
// DP 배열에 무엇을 저장해야 하는가
// 0 1 2 3 4 5 6 7 8 9
// 10가지 색이 있다 치면
// 인접한 것은 선택할 수 없으니
// 3의 경우를 보면
// 2 미선택, 1 선택을 보고
// 3이 선택일 때 혹은 미선택일 때 K 개를 만족하는가
// 1001x1001 배열을 만든다.
// 앞자리가 선택일 때 미선택일 때
// 각 배열의 인덱스는 현재까지 선택된 개수를 뜻함
// selected[3][2] 는 3번 인덱스가 선택됐을 때 현재까지 선택된 색상이 2개일 때 경우의 수가 저장됨
// not_selected[3][2] 3번 인덱스 미선택 색상 2개 경우의 수
// seleceted[4], not_seleceted[4]를 채우기 위해선
// selected[3][0~1000], not_selected[3][0~1000] 을 돌면서 
// seleceted[4] 는 not_selected[3][0~1000] 를 보고 채우고
// not_seleceted[4] 는 selected[3][0~1000] 를 보고 채워넣음
// selected[a][b] 에서 b 의 순회는 1 ~ a+1 까지 a 가 0 번부터시작하는 인덱스이므로
// 이렇게 채웠을 때 마지막이 문제..
// a 가 end 일 때 start 가 선택된 경우 a 는 선택될 수 없음
// 방법 1.
// selected[3][2][0], slecetd[3][2][1] 3차원으로 만들어서 0번이 선택된지 아닌지를 계속해서 추적

// selected[x][1][0] 은 x 를 선택했을 때 1개니까 당연히 경우의수는 1
// selected[x][1][1] 은 x 를 선택했을 때 색상0 이 선택될 수 없으니 무조건 0
// not_selected[x][1][0] 은 x 를 미선택했을 때 1개니까 색상0 을 제외 경우 x-1 // 3일때 0, 1, 2, 3 중 0, 3 제외 1, 2가 각각 1개인 경우 
// not_selected[x][1][1] 은 x 를 미선택했을 때 1개니까 색상0 만 선택한 경우 1
// selected[x][1] 

// selected[3] 을 채울 때..
// ns[2][0] 0,1 다 선택안한 경우
// ns[2][1] 0,1 중 1개 선택
// ns[2][2] 0,1 중 2개 선택
// ns[2][3] 0,1 중 3개 선택
// 5 2 => 01234 // 0 2 \ 0 3 \ 1 3 \ 1 4 \ 2 4

// 코드 작성

#include <iostream>
#include <vector>

using namespace std;

int N, K;
long long output;
// selected[a][b][c] = 0번 색상이 c 상태일 때 \ 색상 a가 선택되었을 때 \ b 개의 색상이 선택된 경우의 수
// a = 색상 번호, b = 선택된 갯수, c = 1: 0번색상 선택, 0: 0번색상 미선택
long long selected[1000][1001][2];
long long not_selected[1000][1001][2];
static int DIVIDING_FACTOR = 1'000'000'003;

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> K;

    // 0번 인덱스 초기화 : 0번이 선택된 경우만
    selected[0][1][1] = 1;

    for (int i=1; i<N-1; i++){
        // 1 개만 선택되는 경우
        selected[i][1][0] = 1;
        not_selected[i][1][0] = i-1;
        not_selected[i][1][1] = 1;
        // 2 개 이상 선택되는 경우
        selected[i][2][0] += not_selected[i-1][1][0];
        selected[i][2][1] += not_selected[i-1][1][1];
        selected[i][2][0] %= DIVIDING_FACTOR;
        selected[i][2][1] %= DIVIDING_FACTOR;
        // j 의 의미 i-1 색상에서 j 개가 택해진 경우의 수
        for (int j=2; j<i+1; j++){
            // i 선택
            selected[i][j + 1][0] += not_selected[i-1][j][0];
            selected[i][j + 1][1] += not_selected[i-1][j][1];
            selected[i][j + 1][0] %= DIVIDING_FACTOR;
            selected[i][j + 1][1] %= DIVIDING_FACTOR;
            // i 미선택
            not_selected[i][j][0] += selected[i-1][j][0];
            not_selected[i][j][0] += not_selected[i-1][j][0];
            not_selected[i][j][1] += selected[i-1][j][1];
            not_selected[i][j][1] += not_selected[i-1][j][1];
            not_selected[i][j][0] %= DIVIDING_FACTOR;
            not_selected[i][j][0] %= DIVIDING_FACTOR;
            not_selected[i][j][1] %= DIVIDING_FACTOR;
            not_selected[i][j][1] %= DIVIDING_FACTOR;
        }
    }
    // N-1번 인덱스 초기화
    selected[N-1][1][0] = 1;
    not_selected[N-1][1][0] = N-2;
    not_selected[N-1][1][1] = 1;
    selected[N-1][2][0] += not_selected[N-2][1][0];
    selected[N-1][2][0] %= DIVIDING_FACTOR;
    for (int j=2; j<N; j++){
        // i 선택
        selected[N-1][j + 1][0] += not_selected[N-2][j][0];
        selected[N-1][j + 1][0] %= DIVIDING_FACTOR;
        // i 미선택
        not_selected[N-1][j][0] += selected[N-2][j][0];
        not_selected[N-1][j][0] += not_selected[N-2][j][0];
        not_selected[N-1][j][1] += selected[N-2][j][1];
        not_selected[N-1][j][1] += not_selected[N-2][j][1];
        not_selected[N-1][j][0] %= DIVIDING_FACTOR;
        not_selected[N-1][j][0] %= DIVIDING_FACTOR;
        not_selected[N-1][j][1] %= DIVIDING_FACTOR;
        not_selected[N-1][j][1] %= DIVIDING_FACTOR;
    }

    output += selected[N-1][K][0];
    output += selected[N-1][K][1];
    output += not_selected[N-1][K][0];
    output += not_selected[N-1][K][1];
    output %= DIVIDING_FACTOR;
    cout << output;

    return 0;
}
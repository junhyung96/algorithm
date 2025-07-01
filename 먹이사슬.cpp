// 풀이 날짜 및 소요 시간 
// 2025-07-01 16:00 ~

// 문제 요약
// 동물은 x 축 영역을 가짐
// 동물 A (x, y), 동물 B (a, b) 의 활동영역을 가진 동물이 있다고 했을 때
// x <= a, y >= b 이면서 x != a & y != b 이면 A 는 B 의 먹이사슬에서 상위에 있음
// 먹이사슬 집단의 최대 크기를 출력

// 입력 예제
// N
// for (N) { cin >> 동물번호, Left, Right }
// 7
// 1 2 4
// 3 1 5
// 4 7 8
// 6 9 10
// 2 6 10
// 5 5 7
// 7 3 4


// 입력 범위 및 조건
// N 1 ~ 500,000
// 좌표 1 ~ 1,000,000,000


// 풀이 방법 및 시간, 공간복잡도 계산
// 집단의 크기를 구해야 한다
// 영역이 큰 동물 (a, b) > (c, d)
// 영역이 큰 동물을 먼저 두고 그 영역에 포함되는 동물을 넣는다.
// 25만 x 25만 비교대조비용 시간초과
// LIS 인데
// 전깃줄과는 다른가.. 
// 영역의 크기별로 동물을 나눔
// 크기가 1, 2, ... 있다고 가정하면
// 1인 거에서 한개 골라서 채택함
// 그다음 크기에서 하나씩 순회하면서 1에 덮어씌울 수 있는지를 봄 ( 이분탐색, 그런데 덮을 수 있는게 여러개라면?.. )
// 그렇게 쭉쭉 해나가면
// 앞에 골랐던 거는 바뀌어도 상관이 없다 이미 그 친구가 포함된 집단의 크기가 큰 경우가 저장되어 있기 때문
// 집단 크기별 상태에서 예를 들어 1의 크기가 바뀌었는데 2의 크기가 그대로인 경우 추가 탐색이 필요하지 않으므로 종료
// 
// 일단은 해볼 것
// 우선순위 큐 원소 : (영역크기, 다음으로 대조해볼 영역크기, 동물번호)
// 영역이 가장 작은 집단을 큐에 다 넣음
// 영역 크기가 가장 큰 것을 꺼내어 다음 영역크기와 대조( 이때 이분탐색으로 탐색시작점 찾고 하나씩 대조해보다가 크기 벗어나면 종료 )
// 있으면 (영역크기+1, 대조해볼크기+1, 동물번호 변경)
// 없으면 (영역크기, 대조해볼크기+1, 동물번호 고정)
// 우선순위 큐에서 뽑았는데 해당 동물번호에 이미 크거나 같은 집단 크기가 저장되어있으면 그냥 큐에서 제거


// a, b 좌표에서
// 1. b 오름차순
// 2. b-a 오름차순 정렬
//
// 차례대로 리스트에 추가
// 현재 a 보다 크거나 같은거 뒤에 붙이기
// 작은게 없다 -> 마지막에 추가하기

// 코드 작성
#include <iostream>
#include <vector>
#include <array>
#include <algorithm>

using namespace std;

int N;
const int MAX_SIZE = 500'002;
const int MAX_VALUE = 1'000'000'001;
vector<array<int, 4>> animals;
vector<int> LIS(MAX_SIZE);


// 내림차순에서 같거나 큰거 중 가장 오른쪽 거 반환
int binary_search(int left, int right, const vector<int>& LIS, int target){
    while (left < right){
        int mid = (left + right) / 2;
        if (LIS[mid] >= target){
            left = mid+1;
        } else{
            right = mid;
        }
    }
    return left;
} 

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;
    for (int i=0; i<N; i++){
        int a, b, c;
        cin >> a >> b >> c;
        animals.push_back({c-b, b, c, a});
    }
    sort(animals.begin(), animals.end(), [](auto& x, auto& y) {
        if (x[2] != y[2]) return x[2] < y[2];
        return x[0] < y[0];
    });
    int pre_a = 0;
    int pre_b = 0;

    for (auto& x : animals) {
        if (pre_a == x[1] && pre_b == x[2]) continue;
        pre_a = x[1];
        pre_b = x[2];
        LIS[binary_search(0, MAX_SIZE-1, LIS, x[1])] = x[1];
    }
    for (int i=0; i<MAX_SIZE; i++){
        if (LIS[i] == 0) {
            cout << i;
            break;
        }
    }

    return 0;
}
// 풀이 날짜 및 소요 시간
// YYYY-MM-DD HH:MM ~ HH:MM

// 문제 요약

// 입력 예제    
// 3
// 1 0
// 5
// 4 2
// 1 2 3 4
// 6 0
// 1 1 9 1 1 1

// 입력 범위 및 조건

// 풀이 방법 및 시간, 공간복잡도 계산

// 코드 작성
#include <iostream>
#include <string>

using namespace std;

class queue {
    private:
        static const int MAX = 10'000;
        int arr[MAX];
        int idx[MAX];
        int frontCursor = 0;
        int rearCursor = 0;
    public:
        void push(int value, int index){
            arr[rearCursor] = value;
            idx[rearCursor] = index;
            rearCursor++;
        }
        void pop(){
            frontCursor++;
        }
        int frontValue(){
            return arr[frontCursor];
        }
        int frontIndex(){
            return idx[frontCursor];
        }
        int maxValue(){
            int tmp = 0;
            for (int i=frontCursor; i<rearCursor; i++){
                tmp = max(tmp, arr[i]);
            }
            return tmp;
        }
        bool empty(){
            return frontCursor == rearCursor;
        }
};

int main(){
    int tc;
    int N;
    int targetIndex;
    cin >> tc;

    for (int i=0; i<tc; i++){
        cin >> N >> targetIndex;
        int arr[N];
        int order = 0;
        queue q = queue();

        for (int j=0; j<N; j++){
            cin >> arr[j];
            q.push(arr[j], j);
        }
        
        while (!q.empty()){
            if (q.frontValue() == q.maxValue()){
                order++;
                if (q.frontIndex() == targetIndex){
                    cout << order << "\n";
                    break;
                }
                q.pop();
            } else {
                q.push(q.frontValue(), q.frontIndex());
                q.pop();
            }
        }

    }

    return 0;
}
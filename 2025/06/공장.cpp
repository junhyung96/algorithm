// 풀이 날짜 및 소요 시간
// 2025-06-08 15:31 ~ HH:MM

// 문제 요약
// 2N 개의 기계가 2열에 걸쳐 N개씩 배치되어있다
// 한 열의 하나의 기계는 다른 열의 하나의 기계와 케이블로 연결되어 있다.
// 기계의 순서는 동일하지 않다
// 기계는 식별번호가 있으며 케이블로 이어진 두 기계는 같은 식별번호를 가진다
// 같은 식별번호를 가진 기계를 잇는 케이블이 직선이라고 할 때 교차하는 선의 개수를 출력하라
// 2 3 1 5 4
//  \ \   X
// 1 2 3 4 5 
// 1 - 2, 1 - 3, 4 -5 
// 3 쌍

// 입력 예제
// 5
// 132 392 311 351 231
// 392 351 132 311 231
// ans: 3

// 입력 범위 및 조건
// 1초, 256MB
// N 1 ~ 500,000
// 식별번호 0 ~ 1,000,000

// 풀이 방법 및 시간, 공간복잡도 계산

// 교차하는 케이블 쌍의 개수를 구해야 한다.
// 교차하는지 어떻게 알 것인가?
// A열 132 392 311 351 231
// B열 392 351 132 311 231
// B 열을 기준으로 정보를 저장한다고 해보자.
// B열에는 A열에 같은 식별번호를 가진 기계의 위치를 저장해보자.
// B열 1 3 0 2 4
// 이 정보로 교차하는 쌍을 알 수 있는가?
// B열의 0번 인덱스 기계번호 392번은 A열의 1번 인덱스와 연결된다
// 0 과 1 을 알고 있고
// 0은 앞에 아무 기계도 없음을
// 1은 앞에 1 개의 기계가 있음을 알 수 있다.
// 인덱스를 기준으로 좌측에서 기계를 완성할 수 없으므로 A열의 0 번은 무조건 교차한다.
// 교차하는 케이블 한 쌍을 도출해냄 
// 위와 같은 방식으로 0 부터 N-1 까지 진행한다면 교차하는 케이블 쌍을 전부 구할 수 있다.
// 어떤 기계의 A, B 열에서의 위치와 해당하는 인덱스좌표의 좌측의 기계들이 우측으로 넘어가는 개수를 세기.
// 하지만 좌측 기계들을 모두 탐색해야하므롤 O(N^2) 의 시간복잡도를 가져 이 풀이방법은 사용할 수 없다.
// B열의 1번 인덱스 351번 기계를 보면 B1 - A3 으로 연결되어있다
// B 0 만 보면 된다. B 0-1 이므로 A1 < A3 이므로 1개 쌍은 좌측에서 연결되므로 교차하지 않음
// A3 = 좌측에 3개가 있는데 하나가 교차하지 않으므로 2개는 교차해야 한다.
// A 좌표를 보고 나보다 작은게 몇개 있는지 알아내야함.
// 최소값으로 세그먼트 트리 구성해서 나보다 작은 값이면 서브트리 개수 더하고 넘어가기 아니면 계속 탐색하기
// 기본적으로 썼던 l, r로 좁혀서 구간질의하는 쿼리를 짜고
// 서브트리 검증해서 교차쌍 개수 구하기
// 최솟값이 저장되어있다면 작을땐 큰게 포함되어있으므로 파고들어가야함
//                      클땐 넘어가면 됨
// 최대값이 저장되어있따면 작을땐 해당 서브트리 저장하고 넘어가면됨
//                      클땐 서브트리 파고들어가야함
// 결국 큰거 작은거 번갈아서 있으면 리프노드 다 타고 들어가야함 결국 O(logN) 보장못함
// 어떻게 원하는 값보다 작은값들이 몇 개 있는지를 O(logN)에 찾아낼 것인가
// 세그먼트 트리의 각노드엔 각 구간에 대한 배열을 저장 및 정렬
// 특정 값 보다 작은 게 몇 개인지 이분탐색으로 찾아냄
// 세그먼트트리 리프노드가 50만개 일때 깊이는 2 ^ 19 // 19층
// 층마다 500000만개의 정보가 있음 19log(500000)
// 

// bit_length 16
// 32 크기 배열 만들어야 하는데
// 15/2= 7/2= 3/2 = 1/2 = 0 count = 

// 코드 작성
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

int bit_length(int n){
    int res = 0;
    while (n > 0){
        n /= 2;
        res++;
    }
    return res;
}

int power(int num, int count){
    int res = 1;
    while (count > 0){
        count--;
        res *= num;
    }
    return res;
}

int query(int index, const vector<vector<int>>& tree, int size){
    // 0 부터 index 까지 탐색
    int l = size;
    int r = size + index;
    int target = tree[r][0];
    int res = 0;
    // cout << index << "\n";
    // cout << l << " " << r << "\n";
    while (l < r){
        if (l % 2) {
            // 로직 수행
            res += lower_bound(tree[l].begin(), tree[l].end(), target) - tree[l].begin();
            l++;
        }
        if (r % 2){
            r--;
            // 로직수행
            res += lower_bound(tree[r].begin(), tree[r].end(), target) - tree[r].begin();
            // cout << l << " " << r << " right " << res << "\n";

        }
        l /= 2;
        r /= 2;
    }

    return res;
}

int main()
{
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    //입력
    int N;
    cin >> N;

    unordered_map<int, int> A_arr;
    
    int tmp;
    for (int i=0; i<N; i++){
        cin >> tmp;
        A_arr[tmp] = i;
    }
    
    // 세그먼트 트리 초기화
    int size = power(2, bit_length(N-1));
    vector<vector<int>> seg_tree(2*size); // {nums...}

    for (int i=0; i<N; i++){
        cin >> tmp;
        seg_tree[size+i].push_back(A_arr[tmp]);
    }
    // // build_Tree
    for (int i=size-1; i>0; i--){
        seg_tree[i].resize(seg_tree[2*i].size() + seg_tree[2*i+1].size());
        merge(seg_tree[2*i].begin(), seg_tree[2*i].end(), seg_tree[2*i+1].begin(), seg_tree[2*i+1].end(), seg_tree[i].begin());
    }
    
    long long output = 0;
    for (int i=0; i<N; i++){
        output += i + seg_tree[size+i][0] - 2 * query(i, seg_tree, size);
    }
    cout << output/2 << "\n";

    return 0;
}

// 최소 최대를 이용한 코드
// #include <iostream>
// #include <unordered_map>

// using namespace std;

// int bit_length(int n){
//     int res = 0;
//     while (n > 0){
//         n /= 2;
//         res++;
//     }
//     return res;
// }

// int power(int num, int count){
//     int res = 1;
//     while (count > 0){
//         count--;
//         res *= num;
//     }
//     return res;
// }

// int get_max(int a, int b){
//     if (a > b){
//         return a;
//     }
//     return b;
// }

// int get_min(int a, int b){
//     if (a < b){
//         return a;
//     }
//     return b;
// }

// int get_counts(int target, int index, int tree[][3], int size){
//     if (index >= size){
//         if (tree[index][0] < target){
//             // cout << index << " value : " << tree[index][0] << "\n";
//             return tree[index][2];
//         }
//         else{
//             return 0;
//         }
//     }
//     int res = 0;
//     if (tree[index][1] < target) {
//         res += tree[index][2];
//     } else {
//         if (tree[index][0] < target){
//             res += get_counts(target, index*2, tree, size);
//             res += get_counts(target, index*2+1, tree, size);
//         }
//     }
//     return res;
// }

// int query(int index, int tree[][3], int size){
//     // 0 부터 index 까지 탐색
//     int l = size;
//     int r = size + index;
//     int target = tree[r][0];
//     int res = 0;
//     // cout << index << "\n";
//     // cout << l << " " << r << "\n";
//     while (l < r){
//         if (l % 2) {
//             // 로직 수행
//             res += get_counts(target, l, tree, size);
//             l++;
//         }
//         if (r % 2){
//             r--;
//             // 로직수행
//             res += get_counts(target, r, tree, size);
//             // cout << l << " " << r << " right " << res << "\n";

//         }
//         l /= 2;
//         r /= 2;
//     }

//     return res;
// }

// int main()
// {
//     ios_base :: sync_with_stdio(false);
//     cin.tie(NULL);
//     cout.tie(NULL);

//     //입력
//     int N;
//     cin >> N;

//     unordered_map<int, int> A_arr;
    
//     int tmp;
//     for (int i=0; i<N; i++){
//         cin >> tmp;
//         A_arr[tmp] = i;
//     }
    
//     // 세그먼트 트리 초기화
//     int size = power(2, bit_length(N-1));
//     int seg_tree[2*size][3] = {}; // {min, max, numbers}

//     for (int i=0; i<N; i++){
//         seg_tree[size+i][0] = 500'100;
//     }
//     for (int i=0; i<N; i++){
//         cin >> tmp;
//         seg_tree[size+i][0] = A_arr[tmp];
//         seg_tree[size+i][1] = A_arr[tmp];
//         seg_tree[size+i][2] = 1;
//     }
//     // build_Tree
//     for (int i=size-1; i>0; i--){
//         seg_tree[i][0] = get_min(seg_tree[2*i][0], seg_tree[2*i+1][0]);
//         seg_tree[i][1] = get_max(seg_tree[2*i][1], seg_tree[2*i+1][1]);
//         seg_tree[i][2] = seg_tree[2*i][2] + seg_tree[2*i+1][2];
//     }
    
//     int output = 0;
//     for (int i=0; i<N; i++){
//         // tmp =  query(i, seg_tree, size);
//         // cout << i << " " << seg_tree[size+i][0] << " cnt : " << i + seg_tree[size+i][0] - 2 * tmp << "\n";
//         output += i + seg_tree[size+i][0] - 2 * query(i, seg_tree, size);
//     }
//     // 연산
//     // cout << seg_tree[2][2] << " index2 cnt \n";
//     cout << output/2 << "\n";

//     return 0;
// }

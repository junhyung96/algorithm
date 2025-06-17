// 2025-06-16 16:18
// 요약
// 전봇대 A, B
// 두 전봇대 사이에는 전깃줄이 연결되어있고
// 합선의 위험이 있어 교차되는 전깃줄을 없애려고 한다.
// 교차하지 않도록 하기 위해 제거해야 하는 전깃줄의 최소 개수를 출력
// 없애야 하는 전깃줄의 A 전봇대에서의 위치를 오름차순으로 출력

// 제한
// 1초, 128MB
// 전깃줄의 수 1 ~ 100,000
// 전깃줄의 위치 1 ~ 500,000

// 풀이
// 가장 긴 증가하는 부분 수열 찾아서
// 뒤에서부터 하나씩 지워가면서 부분 수열에 속하지 않는 위치들 제거 및 출력
// 1 2 3 2 3 4 5 2 4 6 이 DP 부분수열이면
// 1 - - 2 3 4 5 - - 6 역으로 순회하면서 찾아가는 것                 

// DP 로 가장 긴 증가하는 부분 수열 찾기
// 현재 위치의 길이
// 자신보다 앞에 있는 작은 위치 중 가장 큰 위치의 길이 + 1
// 이 경우 O(N^2) 으로 시간초과
// LCA 같이 희소테이블로 해결이 가능한가?
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

int power(int num, int count) // get 2**x value
{
    int tmp = 1;
    while (count)
    {
        count--;
        tmp *= num;
    }
    
    return tmp;
}

int bit_length(int num)
{
    num--;
    int tmp = 0;
    
    while (num > 0)
    {
        num /= 2;
        tmp++;
    }

    return tmp;
}

void update_tree(int index, vector<int>& tree, int value){
    while (index > 0){
        tree[index] = max(tree[index], value);
        index /= 2;
    }
}

int query(int index, const vector<int>& tree, int size){
    int l = size;
    int r = size+index;
    int tmp = 0;

    while (l < r){
        if (l%2) {
            tmp = max(tree[l], tmp);
            l++;
        }
        if (r%2) {
            r--;
            tmp = max(tree[r], tmp);
        }
        l /= 2;
        r /= 2;
    }

    return tmp;
}

int main()
{
    
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    
    // 입력 받기
    // A - B 연결된 전깃줄이 연속된 형태로 주어지지 않기 때문에
    // A 가 정렬된 형태로 B 의 값을 저장하기
    vector<pair<int, int>> links_AB(N);

    for (int i=0; i<N; i++){
        cin >> links_AB[i].first >> links_AB[i].second;
    }

    sort(links_AB.begin(), links_AB.end());

    // 세그먼트 트리 초기화
    int leaf_size = power(2, bit_length(500000));
    vector<int> seg_tree(2*leaf_size);
    for (int i=0; i<N; i++) {
        update_tree(leaf_size + links_AB[i].second, seg_tree, query(links_AB[i].second, seg_tree, leaf_size)+1);
    }
    // 제거할 전깃줄 세기
    int count = 0;
    int max_L = seg_tree[1];
    vector<int> removed;
    for (int i=N-1; i>=0; i--){
        if (max_L == seg_tree[leaf_size+links_AB[i].second]) {
            max_L--;
        } else {
            count++;
            removed.push_back(links_AB[i].first);
        }
    }
    cout << count << "\n";
    sort(removed.begin(), removed.end());
    for (int removed_line: removed){
        cout << removed_line << "\n";
    }
    return 0;
}
// 풀이 날짜 및 소요 시간
// YYYY-MM-DD HH:MM ~ HH:MM

// 문제 요약

// 입력 예제

// 입력 범위 및 조건

// 풀이 방법 및 시간, 공간복잡도 계산

// 코드 작성
#include <iostream>
#include <vector>

using namespace std;

int power(int num, int count){
    int tmp = 1;
    while (count > 0){
        tmp *= num;
        count--;
    }
    return tmp;
}

int bit_length(int n){
    n--;
    int tmp = 0;
    while (n > 0){
        n /= 2;
        tmp++;
    }
    return tmp;
}

void update_tree(int index, int value, vector<int>& tree){
    while (index > 0){
        tree[index] = max(tree[index], value);
        index /= 2;
    }
}

int query(int index, const vector<int>& tree, int leaf_size){
    int left = leaf_size;
    int right = leaf_size+index;
    int tmp = 0;

    while (left < right){
        if (left % 2){
            // 쿼리 수행
            if (tmp < tree[left]){
                tmp = tree[left];
            }
            left++;
        }
        if (right % 2){
            right--;
            // 쿼리 수행
            if (tmp < tree[right]){
                tmp = tree[right];
            }
        }
        left /= 2;
        right /= 2;
    }

    return tmp;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    N;

    int leaf_size = power(2, bit_length(N));
    vector<int> seg_tree(2*leaf_size);
    
    for (int i=0; i < N; i++){
        int a;
        cin >> a;
        a--;
        update_tree(leaf_size+a, query(a, seg_tree, leaf_size)+1, seg_tree);
    }

    cout << seg_tree[1];

    return 0;
}
#include <iostream>
#include <set>

using namespace std;

int modify_angle(int num){
        if (num >= 360) num -= 360;
        if (num < 0) num += 360;
        return num;
    };
    
int N;
int prefix_sum[361];
int result = 0;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    cin >> N;
    
    for (int i=0; i<N; i++){
        int a, b;
        cin >> a >> b;
        
        a += 180;
        a %= 360;

        int tp = a+b;
        int tm = a-b;
        // cout << tm << " " << tp << "\n";
        if (tp < 0){
            tm += 360;
            tp += 360;
        } else if (tm < 0 && tp >= 0){
            tm += 360;
            prefix_sum[360]--;
            prefix_sum[0]++;
        } else if (tm >= 0 && tp < 360){
            
        } else if (tm < 360 && tp >= 360){
            tp -= 360;
            prefix_sum[360]--;
            prefix_sum[0]++;
        } else if (tm >= 360) {
            tm -= 360;
            tp -= 360;
        }
        prefix_sum[tm]++;
        prefix_sum[tp+1]--;
    }
    if (prefix_sum[0]) result++;
    for (int i=1; i<360; i++){
        prefix_sum[i] = prefix_sum[i-1] + prefix_sum[i];
        // cout << prefix_sum[i] << "\n";
        if (prefix_sum[i]){
            result++;
        }
    }

    cout << result;

    return 0;
}

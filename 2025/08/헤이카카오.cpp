#include <iostream>

using namespace std;

int time_per_round, base_prob, increase_prob;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> time_per_round >> base_prob >> increase_prob;
    // 총 시간 = sum (라운드시간 * 이전에 진 확률 * 이번에 이기는 확률)
    // 이전에 진 확률을 계속 넘겨줘야 함..
    int time = time_per_round;
    double win_prob = (double) base_prob / 100;
    double lose_prob = 1;
    double result = 0;
    bool break_ = false;

    cout << fixed;
    cout.precision(7);

    while (true){
        if (win_prob >= 1){
            win_prob = 1;
            break_ = true;
        }
        result += time * lose_prob * win_prob;
        // cout << time << " " << lose_prob << " " << win_prob << " " << result << "\n" ;
        if (break_) break;
        lose_prob *= (1 - win_prob);
        time += time_per_round;
        win_prob += win_prob * increase_prob / 100;
    }
    cout << result;

    return 0;
}
// 풀이 날짜 및 소요 시간
// YYYY-MM-DD HH:MM ~ HH:MM

// 문제 요약

// 입력 예제
// 5 ABC++DE++ 1 2 3 4 5

// 입력 범위 및 조건

// 풀이 방법 및 시간, 공간복잡도 계산

// 코드 작성
#include <iostream>
#include <string>
#include <stack>
#include <map>

using namespace std;

int main()
{
    int N;
    string postfix;
    stack<double> s;
    map<char, double> num_map;
    
    double tmp;
    cin >> N >> postfix;
    for (int i = 0; i < N; i++)
    {
        cin >> tmp;
        num_map[static_cast<char>(65+i)] = tmp;
    }

    for (int i=0; i<postfix.length(); i++){
        char value = postfix[i];
        if (value != '+' && value != '-' && value != '*' && value != '/'){
            s.push(num_map[value]);
        } else {
            double b = s.top();
            s.pop();
            double a = s.top();
            s.pop();
            if (value == '+'){
                s.push(a+b);
            } else if (value == '-'){
                s.push(a-b);
            } else if (value == '*'){
                s.push(a*b);
            } else {
                s.push(a/b);
            }
        }
    }
    cout << fixed;
    cout.precision(2);
    cout << s.top();

    return 0;
}
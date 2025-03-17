import sys, decimal
input_ = sys.stdin.readline
deci = decimal.Decimal
def minput(): return map(int, input_().split())

X, Y = minput()

s = 0
e = int(1e10)
Z = int((deci(Y)/deci(X))*100)

while True:
    if Z >= 99:
        print(-1)
        exit()
    if s == e:
        break
    
    mid = (s+e)//2
    Z_ = int((deci(Y+mid))/deci(X+mid)*100)
    # print(mid, Z_, Z)

    if Z_ > Z:
        e = mid
    else:
        s = mid+1

print(s)

## 4% 에서 틀림
# 어떤 예외가 있는걸까
# 99퍼는 100퍼가 될 수 없다
# 소수점은 버리는데.. 나누기에서 문제가 발생할 수 있나?
# 파이썬 부동소수점 오차로 인한 이슈
# decimal.Decimal 을 사용해서 오차해결
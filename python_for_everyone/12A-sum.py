# 1부터 n까지의 합을 구하는 함수
def sum_func(n):
    s = 0                       # 합을 구하기 위한 변수 s(시작 값을 0으로 지정).
    for x in range(1, n+1):     # range(1, n+1)로 1,2,...,n까지 반복합니다(n+1은 제외).
        s = s + x               # 지금까지 계산된 s값에 x를 더해서 다시 s에 저장합니다.
    return s                    # 계산된 s값을 결괏값으로 돌려줍니다.

print(sum_func(10))
print(sum_func(100))

# 1부터 n까지의 곱을 구하는 함수
def factorial(n):
    fact = 1                   # 곱을 구하기 위한 변수 fact(시작 값을 1로 지정).
    for x in range(1, n+1):    # range(1, n+1)로 1,2,...,n까지 반복합니다(n+1은 제외).
        fact = fact * x        # 지금까지 계산된 값에 x를 곱해 fact에 다시 저장합니다.
    return fact                # 계산된 fact값을 돌려줍니다.

print(factorial(5))
print(factorial(10))

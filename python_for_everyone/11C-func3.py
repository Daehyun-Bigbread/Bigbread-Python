# 결괏값이 있는 함수
def square(a):           # a의 제곱(a*a)을 구하는 함수
    c = a * a
    return c

def triangle(a, h):      # 밑변이 a이고 높이가 h인 삼각형의 넓이를 구하는 함수
    c = a * h / 2
    return c

s1 = 4
s2 = square(s1)          # s1(4)의 제곱을 구하는 함수를 호출해 결과를 s2에 저장합니다.
print(s1, s2)

print(triangle(3, 4))    # 밑변이 3이고 높이가 4인 삼각형의 넓이를 출력합니다.

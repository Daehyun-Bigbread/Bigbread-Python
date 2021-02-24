# 무작위로 덧셈 문제를 만들어서 맞추는 프로그램
import random

a = random.randint(1, 30)      # a에 1~30 사이의 임의의 수를 저장합니다.
b = random.randint(1, 30)      # b에 1~30 사이의 임의의 수를 저장합니다.

print(a, "+", b, "=")          # 문제를 출력합니다..
x = input()                    # 답을 입력받아 x에 저장합니다(문자열로 저장됩니다).
c = int(x)                     #비교를 위해 문자열을 정수로 바꿉니다.

if a + b == c:
    print("천재!")
else:
    print("바보?")

# 이차방정식을 푸는 프로그램
import math
import sys

print("ax2 + bx + c = 0")
# 계수 a,b,c를 입력받아 입력받은 문자열을 소수로 바꿉니다.
a = float(input("a? "))
b = float(input("b? "))
c = float(input("c? "))

if a == 0:
    print("a=0:이차방정식이 아닙니다.")
    sys.exit()    # 이차방정식이 아니면 프로그램 실행을 멈춥니다.

D = b*b - 4*a*c   # 판별식

if D > 0:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print("2개의 해:", x1, x2)
if D == 0:
    x = -b/(2*a)
    print("1개의 해:", x)
if D < 0:
    print("해가 없습니다.")

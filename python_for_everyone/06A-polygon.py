# 정오각형을 그리기 프로그램
import turtle as t

n = 5                 # 오각형을 그립니다(다른 값을 입력하면 다른 도형을 그립니다).
t.color("purple")
t.begin_fill()        # 색칠할 영역을 시작합니다.
for x in range(n):    # n번 반복합니다.
    t.forward(50)     # 거북이 50만큼 앞으로 이동합니다.
    t.left(360/n)     # 거북이 360/n 만큼 왼쪽으로 회전합니다.
t.end_fill()          # 색칠할 영역을 마무리합니다.

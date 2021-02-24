# 마우스로 거북이를 조종해서 그림 그리기
import turtle as t

t.speed(0)              # 거북이의 속도를 가장 빠르게 지정합니다.
t.pensize(2)            # 펜 두께를 2로 지정합니다.
t.hideturtle()          # 거북이를 화면에 보이지 않게 합니다.
t.onscreenclick(t.goto) # 마우스 버튼을 누르면 t.goto 함수를 호출합니다.
                        # 그 위치로 거북이가 움직이면서 선을 그립니다.

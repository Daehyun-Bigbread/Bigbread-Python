# 마음대로 걷는 거북이1
import turtle as t
import random

t.shape("turtle")                   # ‘거북이’ 모양의 거북이 그래픽을 사용합니다.
t.speed(0)

for x in range(500):                # 거북이를 500번 움직입니다.
    a = random.randint(1, 360)      # 1~360 사이의 아무 수나 골라 a에 저장합니다.
    t.setheading(a)                 # a 각도로 거북이의 방향을 돌립니다.
    t.forward(10)                   # 거북이를 10만큼 앞으로 이동합니다.

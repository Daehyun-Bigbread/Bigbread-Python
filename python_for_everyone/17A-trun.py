# 터틀런 만들기1
import turtle as t
import random

te = t.Turtle()     # 악당 거북이(빨간색)
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

ts = t.Turtle()     # 먹이(초록색 동그라미)
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0, -200)

def turn_right():   # 오른쪽으로 방향을 바꿉니다.
    t.setheading(0)

def turn_up():      # 위로 방향을 바꿉니다.
    t.setheading(90)

def turn_left():    # 왼쪽으로 방향을 바꿉니다.
    t.setheading(180)

def turn_down():    # 아래로 방향을 바꿉니다.
    t.setheading(270)

def play():         # 게임을 실제로 플레이하는 함수입니다.
    t.forward(10)   # 주인공 거북이 10만큼 앞으로 이동합니다.
    ang = te.towards(t.pos())
    te.setheading(ang)                # 악당 거북이의 방향을 주인공 거북이를 향하도록 맞춥니다.
    te.forward(9)                       # 악당 거북이 9만큼 앞으로 이동합니다.
    if t.distance(ts) < 12:             # 주인공과 먹이와의 거리가 12보다 작을 때(가깝게 있으면)
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        ts.goto(star_x, star_y)         # 먹이를 다른 곳으로 옮깁니다.
    if t.distance(te) >= 12:           # 주인공과 악당의 거리가 12이상이면 (멀리 있으면)
        t.ontimer(play, 100)           # 0.1초후 play 함수를 실행합니다(게임을 계속 합니다).

t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")   # ‘거북이 모양’의 커서를 사용합니다.
t.speed(0)          # 거북이 속도를 가장 빠르게로 지정합니다.
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")   # [→]를 누르면 turn_right 함수를 실행하도록 합니다.
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()          # 거북이 그래픽 창이 키보드 입력을 받도록 합니다.
play()              # play 함수를 호출해서 게임을 시작합니다.


# 터틀런 만들기2
import turtle as t
import random

score = 0           # 점수를 저장하는 변수
playing = False     # 현재 게임 플레이 중인지 확인하는 변수

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

def turn_right():                # 오른쪽으로 방향을 바꿉니다.
    t.setheading(0)

def turn_up():                   # 위로 방향을 바꿉니다.
    t.setheading(90)

def turn_left():                 # 왼쪽으로 방향을 바꿉니다.
    t.setheading(180)

def turn_down():                 # 아래로 방향을 바꿉니다.
    t.setheading(270)

def start():                    # 게임을 시작하는 함수
    global playing
    if playing == False:
        playing = True
        t.clear()              # 메시지를 지웁니다
        play()

def play():                    # 게임을 실제로 플레이하는 함수
    global score
    global playing
    t.forward(10)                       # 주인공 거북이 10만큼 앞으로 이동합니다.
    if random.randint(1, 5) == 3:       # 1~5 사이에서 뽑은 수가 3이면(20% 확률)
        ang = te.towards(t.pos())
        te.setheading(ang)              # 악당 거북이가 주인공 거북이를 바라보게 합니다.
    speed = score + 5                   # 점수에 5를 더해서 속도를 올립니다(점수가 올라가면 빨라집니다).
    if speed > 15:                      # 속도가 15를 넘지는 않도록 합니다.
        speed = 15
    te.forward(speed)
    if t.distance(te) < 12:             # 주인공과 악당의 거리가 12보다 작으면 게임을 종료합니다.
        text = "Score : " + str(score)
        message("Game Over", text)
        playing = False
        score = 0
    if t.distance(ts) < 12:             # 주인공과 먹이의 거리가 12보다 작으면(가깝게 있으면)
        score = score + 1               # 점수를 올립니다.
        t.write(score)                  # 점수를 화면에 표시합니다.
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        ts.goto(star_x, star_y)         # 먹이를 다른 곳으로 옮깁니다.
    if playing:
        t.ontimer(play, 100)            # 게임 플레이 중이면 0.1초 후 play 함수를 실행합니다.

def message(m1, m2):                    # 메시지를 화면에 표시하는 함수
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 15))
    t.home()

t.title("Turtle Run")
t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")   # 거북이 모양의 커서를 사용합니다.
t.speed(0)          # 거북이 속도를 가장 빠르게로 지정합니다
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")   # [→]를 누르면 turn_right 함수를 실행하도록 합니다.
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()          # 거북이 그래픽 창이 키보드 입력을 받도록 합니다.
message("Turtle Run", "[Space]")

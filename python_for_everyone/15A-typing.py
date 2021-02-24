# 프로젝트2: 타자 게임 만들기
import random
import time

# 단어 리스트: 여기에 단어를 추가하면 문제에 나옵니다.
w = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]
n = 1                   # 문제 번호
print("[타자 게임] 준비되면 엔터!")
input()                 # 사용자가 엔터를 누를 때까지 기다립니다.
start = time.time()     # 시작 시간을 기록합니다.

q = random.choice(w)    # 단어 리스트에서 아무거나 하나 뽑습니다.
while n <= 5:           # 문제를 5번 반복합니다.
    print("*문제", n)
    print(q)            # 문제를 보여줍니다.
    x = input()         # 사용자 입력을 받습니다.
    if q == x:          # 문제와 입력이 같을 때(올바로 입력했을 때)
        print("통과!")  # "통과!"라고 출력합니다.
        n = n + 1       # 문제 번호를 1 증가시킵니다.
        q = random.choice(w)   # 새 문제를 뽑습니다.
    else:
        print("오타! 다시도전!")

end = time.time()       # 끝난 시간을 기록합니다.
et = end - start        # 실제로 걸린 시간을 계산합니다.
et = format(et, ".2f")  # 보기 좋게 소수점 2자리까지만 표기합니다.
print("타자시간:", et, "초")

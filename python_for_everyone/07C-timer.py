# 속으로 20초를 세어서 맞추는 프로그램
import time

input("엔터를 누르고 20초를 셉니다.")
start = time.time()

input("20초 후 다시 엔터를 누릅니다.")
end = time.time()

et = end - start      # end 시간에서 start 시간을 빼면 실제 걸린 시간을 계산할 수 있습니다.
print("실제 시간:", et, "초")
print("차이:", abs(et - 20), "초")

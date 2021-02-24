# 평균, 분산, 표준편차를 구하는 프로그램
import math

# 자료값 리스트
d = [1, 2, 3, 4, 5]
print(d)

# 평균 구하기
mean = sum(d) / len(d)
print(mean)

# 분산 구하기
vsum = 0
for x in d:
    vsum = vsum + (x - mean)**2
var = vsum / len(d)
print(var)

# 표준편차 구하기
std = math.sqrt(var)
print(std)

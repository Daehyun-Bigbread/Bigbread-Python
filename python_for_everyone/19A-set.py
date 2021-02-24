# 파이썬의 집합 기능1
A = {1,2,3,4}
B = {3,4,5,6}

print(A)
print(B)

print(1 in A)
print(6 in A)
print(len(A))

print(A | B)
print(A & B)
print(A - B)

# 파이썬의 집합 기능2
C = {x for x in range(1, 11) }
D = {x for x in range(1, 11) if x % 3 == 0 }

print(C)
print(D)

print(C<D)
print(C>D)

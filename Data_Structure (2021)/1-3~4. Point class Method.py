# 1. def function(*args): 라고 함수를 정의하면, 임의의 개수의 매개 변수들을 tuple args를 통해 전달할 수 있다
def __init__(self, *args):
    self._coords = list(args) # 좌표 값을 리스트 _coords에 저장
   
# 2. 벡터 출력이 필요하므로 __str__ 메쏘드를 정의한다
def __str__(self):
    return str(tuple(self._coords))    # tuple로 바꿔주는 이유는 단순히 (x, y, z) 형식으로 출력하기 위해서 
  
# 3. __len__ magic 메쏘드를 정의한다. 이 메쏘드는 벡터의 차원을 리턴하는 것으로 len(v)의 형태로 사용할 수 있게 하는 메쏘드이다
def __len__(self):
    return len(self._coords)
  
# 4. __getitem__(self, k) 는 self의 k번째 값을 리턴하는 magic 메쏘드이다. 여기서는 k번째 좌표 값 _coords[k]를 리턴한다
def __getitem__(self, k):
    return self._coords[k]

# 5. __setitem__(self, k, val) 는 self의 k번째 값에 val 값을 대입하는 magic 메쏘드이다. 즉, _coords[k] = val이 된다
def __setitem__(self, k, val):
    self._coords[k] = val
    
# 6. 
v = Vector(1, 2, 3)  # (1, 2, 3) 3차원 벡터 v 생성
print(v)        # (1, 2, 3)
for c in v:    # for 루프를 돌면서 c = v[0], v[1], v[2]이 됨
    print(c, end=" ")
print()        # 1 2 3

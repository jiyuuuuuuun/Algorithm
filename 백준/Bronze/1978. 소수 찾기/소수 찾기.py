# 기초수학 + 완전 탐색(브루트 포스)

# 에라토스테네스의 체 -  소수판별
def is_prime(x):
  if x < 2:
    return False
  for i in range(2, int(x**0.5)+1):
    if x%i == 0:
      return False
  return True
  
N = int(input())
cnt = 0

li = list(map(int,input().split()))
for i in range(N):
  if is_prime(li[i]) == True:
    cnt += 1
  else:
    cnt += 0
  
print(cnt)
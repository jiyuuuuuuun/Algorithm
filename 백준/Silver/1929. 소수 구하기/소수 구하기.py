# 수학: 정수론(소수)
# 에라토스테네스의 체

M, N = map(int, input().split())

prime = [True] * (N+1)
prime[0] = prime[1] = False # 0, 1은 소수가 아니므로 F

for i in range(2, int(N**0.5)+1):
  if prime[i]: # 소수라면
    for j in range(i*i, N+1, i): # i의 배수들은 소수 아닌것으로 처리
      prime[j] = False
      
for i in range(M, N+1):
  if prime[i]:
    print(i)
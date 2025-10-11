# 수학: 조합론
# 이항 계수(binomial coefficient)는 이항식을 이항 정리로 전개했을 때 각 항의 계수이며, 주어진 크기의 (순서 없는) 조합의 가짓수

# nCk = (n) = __n!__
#       (k)  k!(n-k)!
N, K = map(int, input().split())

N_fac = 1
K_fac = 1
fac= 1
for i in range(1, N+1, 1):
  N_fac *= i

for i in range(1, K+1, 1):
  K_fac *= i
  
for i in range(1, N-K+1, 1):
  fac *= i

result = int(N_fac / (K_fac*fac))
print(result)
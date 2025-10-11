# 1929 소수 구하기
# 에라토스테네스의 체
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
nums = [1] * (N+1)       # 2부터 N까지의 숫자 중 소수 찾기, 처음에는 모든 수를 소수라고 가정
nums[0] = nums[1] = 0 # 0, 1은 소수가 아니므로 0으로 표시 

for i in range(2, int(N**0.5)+1): # N의 제곱근으로 이보다 큰 수는 확인할 필요 없다.
  if nums[i] == True:   # 현재 숫자 i가 소수라면 i의 배수를 False로 표시
    for j in range(2*i, N+1, i): # i의 2배수부터 i씩 증가하며 N미만까지 반복
      nums[j] = False
minority = [i for i in range(M, N+1) if nums[i] == True] # 배열에서 True로 남아있는 index를 M부터 반환

for k in range(len(minority)):
  print(minority[k])
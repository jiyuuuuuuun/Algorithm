# 자료구조: 해시

import sys

N = int(input())
N_nums = list(map(int, sys.stdin.readline().split()))
M = int(input())
M_nums = list(map(int, sys.stdin.readline().split()))


cnt = {}
result = []
for i in N_nums:
  if i in cnt:
    cnt[i] += 1
  else:
    cnt[i] = 1

for i in M_nums:
  result.append(cnt.get(i, 0))
  
print(*result)
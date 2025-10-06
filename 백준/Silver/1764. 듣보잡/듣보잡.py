# 자료구조: 해시(맵)

import sys

N, M = map(int,sys.stdin.readline().split())

no_listen = set()
no_lis_see = []
for _ in range(N):
  name1 = input().strip()
  no_listen.add(name1)
  
for _ in range(M):
  name2 = input().strip()
  if name2 in no_listen:
    no_lis_see.append(name2)
  
no_lis_see.sort()

print(len(no_lis_see))
for name in no_lis_see:
  print(name)
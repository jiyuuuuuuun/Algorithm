# 탐색 알고리즘: DFS/BFS
# DFS

import sys
sys.setrecursionlimit(10**6) # 런타임 에러(RecursionError)를 피하기 위한 재귀 깊이 제한 설정, 넉넉하게 늘려준다.

N, M = map(int, sys.stdin.readline().split())

network = [[] for _ in range(N+1)]

for _ in range(M):
  u, v = map(int, sys.stdin.readline().split())
  network[u].append(v)
  network[v].append(u)

visited = [False] * (N+1)

cnt = 0

def DFS(current):
  visited[current] = True
  
  for connect in network[current]:
    if not visited[connect]:
      DFS(connect)
      
  
for i in range(1, N+1):
  if not visited[i]:
    DFS(i)
    cnt += 1
      
print(cnt)
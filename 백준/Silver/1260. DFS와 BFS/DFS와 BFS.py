# 탐색 알고리즘: DFS/BFS

import sys

N, M, V = map(int, sys.stdin.readline().split())

network = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, input().split())
  network[a].append(b)
  network[b].append(a)
  
for i in range(1, N + 1):
  network[i].sort()       ### 각 정점의 인접 리스트를 오름차순으로 정렬

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)
  
dfs_result = []
bfs_result = []



def DFS(current):
  visited_dfs[current] = True
  dfs_result.append(current)
    
  for connect in network[current]:
    if not visited_dfs[connect]:
      DFS(connect)
  
  
  
from collections import deque

def BFS(V):
  queue = deque([V]) # V부터 탐색 시작
    
  visited_bfs[V] = True # 시작 노드는 방문처리
  
  while queue: # 큐가 빌 때까지 반복
    current = queue.popleft()
    bfs_result.append(current)
    
    for connect in network[current]:
      if not visited_bfs[connect]:
        visited_bfs[connect] = True
        queue.append(connect)
        
DFS(V), BFS(V)

print(*dfs_result)
print(*bfs_result)
# 탐색 알고리즘: DFS/BFS
#### BFS

from collections import deque

N = int(input()) # 컴퓨터의 수
M = int(input()) # 네트워크 상에서 연결되어있는 컴퓨터의 번호 쌍 수

network = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, input().split())
  network[a].append(b)
  network[b].append(a)

queue = deque([1]) # 1부터 시작
visited = [0] * (N+1)
visited[1] = 1 # 시작은 방문처리
cnt = 0

while queue:
  current = queue.popleft()
  
  for connect in network[current]:
    if visited[connect] == 0: # 방문 안했다면
      visited[connect] = 1 # 방문처리
      cnt += 1
      queue.append(connect) # 다음탐색대상으로 지정
      
print(cnt)



#### DFS(재귀)

# 탐색 알고리즘: DFS/BFS


N = int(input()) # 컴퓨터의 수
M = int(input()) # 네트워크 상에서 연결되어있는 컴퓨터의 번호 쌍 수

network = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, input().split())
  network[a].append(b)
  network[b].append(a)

visited = [0] * (N+1)
cnt = 0

def DFS(current):
  global cnt
  visited[current] = 1
  
  for connect in network[current]:
    if visited[connect] == 0: # 방문 안했다면
      cnt += 1
      DFS(connect) # 해당 노드로 이동(재귀호츌)
      
DFS(1)
print(cnt)


#### DFS(스택)

# 탐색 알고리즘: DFS/BFS


N = int(input()) # 컴퓨터의 수
M = int(input()) # 네트워크 상에서 연결되어있는 컴퓨터의 번호 쌍 수

network = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, input().split())
  network[a].append(b)
  network[b].append(a)

stack = [1] # 1부터 시작
visited = [0] * (N+1)
cnt = 0

while stack:
  current = stack.pop()
  
  if visited[current] == 0: # 방문 안했다면
    visited[current] = 1 # 방문처리
    
    if current != 1:
      cnt += 1

    for connect in network[current]:
      if not visited[connect]:
        stack.append(connect) # 다음 탐색 대상으로 지정
      
print(cnt)

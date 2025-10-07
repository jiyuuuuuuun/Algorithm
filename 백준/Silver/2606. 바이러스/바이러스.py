# 2606 바이러스
import sys
input = sys.stdin.readline

visited = set()

def DFS(cur):
  visited.add(cur)

  for nxt in adj[cur]: #다음에 찾아볼 노드를 현재리스트에서 하나씩 뽑아놓는다.
    if nxt not in visited:
      DFS(nxt)
      

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]

for _ in range(M):
  a, b = map(int, input().split())
  adj[a].append(b)
  adj[b].append(a) #a와 b가 연결되어있음을 알리는 코드 넣어준다.

DFS(1)
print(len(visited)-1)
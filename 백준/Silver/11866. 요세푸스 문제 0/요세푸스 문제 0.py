# 11866 요세푸스 문제 0
# M번째 수 제거, 제거된 수 다음부터 count한 M번쨰수 제거 반복

import sys
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())
queue = deque()
visited = []
queue.extend(range(1, N+1))

while queue:
  queue.rotate(-K+1) #K번째 수를 맨앞으로 이동
  visited.append(queue.popleft())

print(f"<{', '.join(map(str, visited))}>")
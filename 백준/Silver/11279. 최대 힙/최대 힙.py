# 자료구조: 힙(우선순위 큐)

import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
  x = int(sys.stdin.readline()) 
 
  if x > 0:
    heapq.heappush(heap, -x) # heapq는 최소힙 -> - 붙여서 저장 -> 최대힙으로
    
  else:
    if len(heap) > 0:
      max_val = heapq.heappop(heap) # 최솟값 삭제 후 반환
      print(-max_val)
      
    else:
      print(0)
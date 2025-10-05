# 자료구조: 큐/덱

import sys
from collections import deque

class Deq:
  def __init__(self):
    self.data=deque()
    
  def push_front(self, X):
    self.data.appendleft(X)
    
  def push_back(self, X):
    self.data.append(X)
    
  def pop_front(self):
    if len(self.data) == 0:
      print(-1)
    else:
      print(self.data.popleft())
    
  def pop_back(self):
    if len(self.data) == 0:
      print(-1)
    else:
      print(self.data.pop())
    
  def size(self):
    print(len(self.data))
    
  def empty(self):
    if len(self.data) == 0:
      print(1)
    else:
      print(0)
    
  def front(self):
    if len(self.data) == 0:
      print(-1)
    else:
      print(self.data[0])
    
  def back(self):
    if len(self.data) == 0:
      print(-1)
    else:
      print(self.data[-1])

N = int(sys.stdin.readline())
d = Deq()

for _ in range(N):
  out = sys.stdin.readline().split()
  
  cmd = out[0]
  
  if cmd == 'push_front':
    d.push_front(int(out[1]))
    
  elif cmd == 'push_back':
    d.push_back(int(out[1]))
    
  elif cmd == 'pop_front':
    d.pop_front()
    
  elif cmd == 'pop_back':
    d.pop_back()
    
  elif cmd == 'size':
    d.size()
    
  elif cmd == 'empty':
    d.empty()
    
  elif cmd == 'front':
    d.front()
    
  elif cmd == 'back':
    d.back()
import sys

class STACK:
  def __init__(self):
    self.li = []

  def push(self, X):
    self.li.append(X)
  
  def pop(self):
    if len(self.li) > 0:
      print(self.li.pop())
    else:
      print(-1)
  
  def size(self):
    print(len(self.li))
  
  def empty(self):
    if len(self.li) != 0:
      print(0)
    else:
      print(1)

  def top(self):
    if len(self.li) != 0:
      print(self.li[-1])
    else:
      print(-1)


N = int(sys.stdin.readline())
s = STACK()
for _ in range(N):
  out = sys.stdin.readline().split()
  if not out:
    continue

  cmd = out[0]

  if cmd == 'push':
    s.push(int(out[1]))

  elif cmd == 'pop':
    s.pop()

  elif cmd == 'size':
    s.size()

  elif cmd == 'empty':
    s.empty()

  elif cmd == 'top':
    s.top()
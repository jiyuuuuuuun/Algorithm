# 자료구조: 이진트리
# 딕셔너리로 풀기

import sys

N = int(sys.stdin.readline())
tree = {}
for _ in range(N):
  root, left, right = sys.stdin.readline().strip().split()
  tree[root] = [left, right]
    
    # 재귀로 left, right 호출
def pre(root): # root-left-right
  if root != '.':
    print(root, end='')
    pre(tree[root][0]) #left
    pre(tree[root][1]) #right
  
def inorder(root): # left-root-right
  if root != '.':
    inorder(tree[root][0]) #left
    print(root, end='')
    inorder(tree[root][1]) #right
  
  
def post(root): # left-right-root
  if root != '.':
    post(tree[root][0]) #left
    post(tree[root][1]) #right
    print(root, end='')
    


# A가 항상 root노드
pre('A')
print()
inorder('A')
print()
post('A')
print()

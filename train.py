from sys import stdin

MAX = 25010
train = [ None for i in range(MAX) ]
memo = [ None for i in range(MAX) ]

def Merge(train,init,mid,end):
  n1 = mid-init + 1
  n2 = end-mid
  print(n1)
  print(n2)
  L1,L2 = [],[]
  for i in range(n1):
    L1.append(train[n1])
  for i in range (n2):
    L2.append(train[n2])
  L1.append (MAX+1)
  L2.append (MAX+1)
  i = 0
  j = 0
  for k in range (end):
    if L1[i] <= L2[j]:
      train[k] = L1[i]
      i = i+1
    else:
      train[k] = L2[j]
      j = j+1
      
  return 0

def solve(train, m , n):
  if m < n :
    mid = m + ((n-m)>>1)
    solve(train,m,mid)
    solve(train,mid+1,n)
    Merge(train,m,mid,n)
    
 
  return 0

def main():
  global train
  inp = stdin
  cases = int(inp.readline().strip())
  while cases>0:
    n = int(inp.readline().strip())
    tok = inp.readline().strip().split()
    for i in range(n): train[i] = int(tok[i])
    print('Optimal train swapping takes {0} swaps.'.format(solve(train,0,n)))
    cases -= 1

main()

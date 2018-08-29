from sys import stdin
from collections import deque
import time

INF = float('inf')
configuracionI = []
configuracionF = []
def convertArrayToNum(array):
	return (array[0]*1000)+(array[1]*100)+(array[2]*10)+array[3]

'''def getMovements(configuracion):
	arraymovements = []
	arraymovements.append([(configuracion[0]-1)%10,configuracion[1],configuracion[2],configuracion[3]])
	arraymovements.append([(configuracion[0]+1)%10,configuracion[1],configuracion[2],configuracion[3]])
	arraymovements.append([configuracion[0],(configuracion[1]-1)%10,configuracion[2],configuracion[3]])
	arraymovements.append([configuracion[0],(configuracion[1]+1)%10,configuracion[2],configuracion[3]])
	arraymovements.append([configuracion[0],configuracion[1],(configuracion[2]-1)%10,configuracion[3]])
	arraymovements.append([configuracion[0],configuracion[1],(configuracion[2]+1)%10,configuracion[3]])
	arraymovements.append([configuracion[0],configuracion[1],configuracion[2],(configuracion[3]-1)%10])
	arraymovements.append([configuracion[0],configuracion[1],configuracion[2],(configuracion[3]+1)%10])
	return arraymovements


def BFS(configuracionI,configuracionF,visited):
	q = deque()
	countc = [0]*10000
	count = 0
	limite = [0,0,0,-1]
	q.append(configuracionI)
	q.append(limite)
	resl = convertArrayToNum(configuracionF)
	found = False
	while(q):
		act = q.popleft()
		#print(act)
		#time.sleep(1)
		if(act == [0,0,0,-1]):
			count += 1
			if(q):
				q.append(act)
			if(count == 100):
				return -1
		else:
			#print("entra")
			movements = getMovements(act)
			for i in movements:
				val = convertArrayToNum(i)

				if (visited[val] != True):	
					#print(val)
					#time.sleep(0.5)
					visited[val] = True
					#countc[val] = countc[convertArrayToNum(act)]+1
					if (val == convertArrayToNum(configuracionF)):
						#print("llega")
						found = True
						return count+1
					q.append(i)
			#count += 1
	return -1

'''
def next_states(t):
  ans = list()
  for i in range(4):
    tmp1,tmp2 = list(),list()
    for j in range(4):
      if j==i:
        tmp1.append((t[i]+1) if t[i]<9 else 0)
        tmp2.append((t[i]-1) if t[i]>0 else 9)
      else:
        tmp1.append(t[j])
        tmp2.append(t[j])
    ans.append(tuple(tmp1))
    ans.append(tuple(tmp2))
  return ans

def bfs(visited):
  global configuracionF, configuracionI
  #visited = [ 0 for _ in range(10000) ]
  dist = [ INF for _ in range(10000) ]
  queue = deque()
  queue.append((configuracionI, 0)) ; visited[convertArrayToNum(configuracionI)] = 1
  cnt = 0
  while dist[convertArrayToNum(configuracionF)]==INF and len(queue)!=0:
    u,d = queue.popleft()
    dist[convertArrayToNum(u)] = d
    #if cnt==100: #print(queue)
    cnt += 1
    for v in next_states(u):
      if visited[convertArrayToNum(v)]==0:
        queue.append((v, d+1)) ; visited[convertArrayToNum(v)] = 1
    visited[convertArrayToNum(u)] = 2
  return dist[convertArrayToNum(configuracionF)]

def main():
	global configuracionI, configuracionF
	numeroCasos = int(stdin.readline())
	stdin.readline()
	for i in range(numeroCasos):
		configuracionI = [int(x) for x in stdin.readline().split()]
		configuracionF = [int(x) for x in stdin.readline().split()]
		numeroRestricciones = int(stdin.readline())
		visited = [0 for _ in range(10000)]
		for j in range(numeroRestricciones):
			num = convertArrayToNum([int(x) for x in stdin.readline().split()])
			visited[num] = 1
		resultado = bfs(visited)
		print(resultado)
		stdin.readline()
	print()	

main()

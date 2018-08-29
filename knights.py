from sys import stdin
R = 0
C = 0
M = 0
N = 0
matriz = []
vecinos = []
visitados = []
signos = [[-1,-1],[-1,1],[1,-1],[1,1]]

def dentroDelRango(a,b):
	global R,C
	return(a < R and a >= 0 and b<C and b >= 0)

def dfs(posx,posy):
	global matriz,vecinos,visitados,signos,R,C,M,N
	#print(matriz)
	if(visitados[posy][posx]):
		return
	visitados[posy][posx] = True
	for i in range(4):
		y1 = posy+(signos[i][0]*M)
		x1 = posx+(signos[i][1]*N)
		
		if(dentroDelRango(x1,y1) and matriz[y1][x1] != -1):
			vecinos[y1][x1] += 1
			dfs(x1,y1)
		y1 = posy + signos[i][0]*N
		x1 = posx+signos[i][1]*M
		if(dentroDelRango(x1,y1) and matriz[y1][x1] != -1):
			vecinos[y1][x1] += 1
			dfs(x1,y1)
	return
def main():
	x,y=0,0
	
	global matriz,vecinos,visitados,signos,R,C,M,N
	testcases = int(stdin.readline())
	for i in range (0,testcases) :
		R,C,M,N = [int(c) for c in stdin.readline().split()]
		
		matriz = [0]*C
		#print(matriz)
		for k in range(C):
			matriz[k] = [0]*R

		vecinos = [0]*C
		for k in range(C):
			vecinos[k] = [0]*R

		visitados = [False]*C
		for k in range(C):
			visitados[k] = [False]*R

		w = int(stdin.readline())
		for j in range(w) :
			x,y = [int(ll) for ll in stdin.readline().split()]
			#print(x,y)
			#print(matriz[y][x])
			matriz[y][x] -= 1
		dfs(0,0)
		impares,pares = 0,0
		for z in range(C) :
			for u in range(R):
				if(M==0 or N==0 or N==M):
					vecinos[z][u] >> 1
				if(vecinos[z][u] or not(z or u)):
					if(vecinos[z][u] & 1):
						impares += 1
					else:
						pares += 1
		print("Case "+str(i)+" : "+str(pares)+" "+str(impares))


main()
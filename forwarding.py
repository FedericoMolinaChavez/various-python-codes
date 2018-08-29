from sys import stdin
''' para este problema tenemos una estructura principal de grafo donde almacenamos la estructura principal, se utilizara 
anexo a esto un arreglo donde vamos a guardar la cantidad de profundidad que alcanza cada nodo y vamos a almacenar en 
otro arreglo los valores de posiciones visitadas por dfs realizado.'''
def takeFirst(elem):
	return elem[0]

def dfs(valoresPos1,valoresPos,grafo,n):
	currentj = 0
	valoresPos[n] = True
	tmp = grafo[n]
	if (valoresPos[tmp] != True):
		currentj = dfs(valoresPos1,valoresPos,grafo,tmp)+1
	#print(currentj)
	valoresPos1[n] = True
	valoresPos[n] = False
	return currentj	

def iterative_dfs(valoresPos1,valoresPos,grafo,n):
  '''iterative depth first search from start'''
  count = 0
  valoresPos[n] = True
  tmp = grafo[n]
  while()



  

def calc(valoresPos1,valoresPos,grafo,n):
	resl = 0
	mx = -1
	sumatoria = [0]*n
	for i in range (1,n+1):
		if(valoresPos1[i] == True):
			continue
		tmp = dfs(valoresPos1,valoresPos,grafo,i)
		
		#print (tmp)
		if(tmp > mx):
			mx = tmp
			resl = i
	return resl

def main():
	graph = []
	valoresPos = []
	valProfundidad = []
	resultado = ""
	numeroCasos = int(stdin.readline())
	for j in range(numeroCasos) :
		numeroMarcianos = int(stdin.readline())
		graph = [0]*(numeroMarcianos+1)
		valoresPos = [False]*(numeroMarcianos+1)
		
		for i in range(numeroMarcianos) :
			c = [int(x) for x in stdin.readline().split()]
			
			graph[c[0]] = c[1]
			
		#print(graph)
	
		valoresPos1 = valoresPos
		#print(valoresPos1)
		#print(iterative_dfs(graph,1))
		resultado += "Case "+str(j+1)+": "+str(calc(valoresPos1,valoresPos,graph,numeroMarcianos))+"\n"
		
		graph = []
	#print(resultado)



main()
from sys import stdin

def productoria(lista,inicio,fin):
    producto=1
    while inicio < fin:
        producto=producto*int(lista[inicio])
        inicio=inicio+1
    return (producto)

def solve(lista,operacion,n):
    if operacion[0]=='P':
        #aqui toca hacer una productoria
        inicio=int(operacion[1])
        fin=int(operacion[2])
        total=productoria(lista,inicio,fin)        
        if total == 0:
            print(0)
        elif total > 0:
            print('+')
        else:
            print('-')
    elif operacion[0]=='C':
        indice=int(operacion[1])
        lista[indice-1]=int(operacion[2])

    
def main():
    imp= stdin
    line=imp.readline().split()
    while (len(line)!=0):
        n=int(line[0])
        noperaciones=line[1]
        lista=imp.readline().split()
        i=0
        while i < int(noperaciones):
            operacion=imp.readline().split()
            (solve(lista,operacion,n))
            i=i+1
        line=imp.readline().split()

main()
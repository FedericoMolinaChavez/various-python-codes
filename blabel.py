#babelfish by federico molina chavez
from sys import stdin

def solve(line,a):
    if (line in a):
        return (a[line])
    else:
        return ('eh')

def main():
    arregloArmado = []
    imp = stdin
    line = imp.readline().strip()
    while(len(line)>1):
        arr = line.split()
        val1,val2 = arr[0],arr[1]
        pair = (val2,val1)
        arregloArmado.append(pair)
        line = imp.readline().strip()
    a = dict(arregloArmado)
    line = imp.readline().strip()
    cont = 0
    while(len(line)>0):
        print(solve(line,a))
        cont +=1
        line = imp.readline().strip()
    #print(line)
main()
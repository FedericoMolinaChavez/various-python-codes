#add all by Federico Molina Chavez
from sys import stdin
from heapq import *

def main():
    
    imp = stdin
    a = imp.readline().strip()
    while(int(a) != 0):
        priority_queue = []
        b = imp.readline().strip().split()
        a = imp.readline().strip()
        for i in b:
            heappush(priority_queue,int(i))
        if (len(priority_queue)==1):
            print(priority_queue[0])
        else:
            suma = 0
            while (len(priority_queue)>1):
                num = heappop(priority_queue)
                num +=heappop(priority_queue)
                suma += num
                heappush(priority_queue,num)
            print (suma)
main()            
    
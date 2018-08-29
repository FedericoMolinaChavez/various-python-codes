from sys import stdin
from collections import deque

global result


def main():
    prev = deque()
    ans = ''
    dequea = deque()
    imp = stdin
    a = imp.readline().strip()
    wr,state = False, True
    while (len(a)>0):
        for i in a:
            if (i == '['):
                state = False
                wr = True
            elif (i == ']'):
                state = True
            else:
                if (state == False and wr == True):
                    dequea.extendleft(prev)
                    prev.clear()
                    wr = False
                    prev.extendleft(i)
                elif (state == False and wr == False):
                    prev.extendleft(i)
                elif (state == True and wr == False):
                    dequea.extendleft(prev)
                    prev.clear()
                    dequea.append(i)
                    wr = True
                else:
                    dequea.append(i)
        dequea.extendleft(prev)
        prev.clear()
        for i in dequea:
            ans += i
        print (ans)
        ans = ''
        dequea.clear()
        a = imp.readline().strip()
        
main()
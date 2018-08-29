#This is a simple straight forward rsa encryption decryption code
import random
import math


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def simpleSieve(sieveSize): #taken from https://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
    #creating Sieve.
    sieve = [True] * (sieveSize+1)
    # 0 and 1 are not considered prime.
    sieve[0] = False
    sieve[1] = False
    for i in range(2,int(math.sqrt(sieveSize))+1):
        if sieve[i] == False:
            continue
        for pointer in range(i**2, sieveSize+1, i):
            sieve[pointer] = False
    # Sieve is left with prime numbers == True
    primes = []
    for i in range(sieveSize+1):
        if sieve[i] == True:
            primes.append(i)
    return primes
    
                
def EEA(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = EEA(b % a, a)
        return (g, y - (b // a) * x, x)
        

def invM(b, n):
    g, x, _ = EEA(b, n)
    if g == 1:
        return x % n
                
def keyGen():
    primes = simpleSieve(1000)
    tam = len(primes)
    p = primes[tam-1]
    q = primes[tam-2]
    n = p*q
    phi = (p-1)*(q-1)
    """
    e = 0
    for i in range(2,phi):
        if (gcd(i,phi)==1):
            e = i
            break
    """
    e = random.choice(primes)
    d = invM(e,phi)
    return (e,d,n)

def Encrypt(listmsg, pubKey, n):
    listresl = []
    for i in range(len(listmsg)):
        listresl.append(pow(ord(listmsg[i]),pubKey,n))
    return listresl
    
def Decrypt(listmsgE,privKey,n):
    listmsg = []
    for i in range(len(listmsgE)):
        listmsg.append(chr(pow(listmsgE[i], privKey, n)))
    return listmsg

def main():
    vals = keyGen()
    msg = input("Message: ")
    a = Encrypt(list(msg),vals[0],vals[2])
    print "Ciphertest: ", a
    print "Decrypted Ciphertext: ", ''.join(Decrypt(a,vals[1],vals[2]))
    
    
main()



    
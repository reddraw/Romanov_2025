from random import randint
from math import gcd,sqrt

def PrimeList():
    primelist=[]
    for i in range(2,10**6):
        isPrime=True
        for j in range(2, int(sqrt(i)+1)):
            if i%j==0:
                isPrime=False
                break
        if isPrime:
            primelist.append(i)
    return primelist

def DFinder(f,e):
    r1 = f
    r2 = e
    s1 = int(1)
    s2 = int(0)
    t1 = int(0)
    t2 = int(1)
    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        r1 = r2
        r2 = r
        s = s1 - q * s2
        s1 = s2
        s2 = s
        t = t1 - q * t2
        t1 = t2
        t2 = t
    if t1 < 0:
        t1 = t1 % e
    return (t1)

def RSA():
    primelist=PrimeList()
    index2=index=randint(0, len(primelist))
    while index2==index:
        index2=randint(0,len(primelist))
    p=primelist[index]
    q=primelist[index2]
    n=p*q
    f=(p-1)*(q-1)
    e=0
    while gcd(e,f)!=1:
        e=randint(1,f)
    d=DFinder(f,e)
    return d,e,n

def Encrypt(e,n,text):
    return pow(text,e,n)
def Decrypt(d,n,text):
    return pow(text, d,n)

runner=1
otvet=0
while runner>0:
    if otvet==0:
        print("Print the number of operation you want to do")
        print("1. Cipher the word")
        print("2. Test of Units")
        print("3 or any other. Exit")
        otvet=int(input("Number:"))
    if otvet==1:
        print("Enter the number you want to cipher")
        stroka=int(input("Number:"))
        d,e,n = RSA()
        print("Public key is :"+"("+str(e)+","+str(n)+")")
        print("Private key is :" + "(" + str(d) + "," + str(n) + ")")
        print("Encrypted message is:"+str(Encrypt(e,n,stroka)))
        print("Decrypted message is:"+str(Decrypt(d,n,Encrypt(e,n,stroka))))
        if stroka==Decrypt(d,n,Encrypt(e,n,stroka)):
            print("Answer match!")
        else:
            print("Error in calculations")
        print("Exiting to main menu")
        otvet=0
    elif otvet==2:
        flags=0
        if(Encrypt(7,33,19)==13):
            flags+=1
            print("Test 1 passed")
        else: print("Test 1 is not passed")
        if(Decrypt(5,21,2)==11):
            flags+=1
            print("Test 2 passed")
        else: print("Test 2 is not passed")
        if(Encrypt(7,33,18)==6):
            flags+=1
            print("Test 3 passed")
        else: print("Test 3 is not passed")
        print("Tests passed: "+str(flags)+"/3")
        otvet=0
    else:
        print("Goodbye")
        runner=0







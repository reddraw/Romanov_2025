def MatrixCreator(kod):
    kod=kod.upper()
    kod=kod.replace("I","J")
    kodename=kod
    matrix=[]
    k=""
    for i in range(26):
        j=chr(i+65)
        if j not in kod and j!="I":
            kodename+=j

    for i in range(len(kodename)):
        if (i+1)%5==0:
            k+=kodename[i]
            matrix.append(k)
            k=""
        else:
            k+=kodename[i]
    return matrix

def BigramsCreator(slovo):
    bi=""
    bigrams=[]
    slovo=slovo.replace(" ", "")
    slovo=slovo.upper()

    for i in range(len(slovo)):
        if len(bi)==1:
            if bi==slovo[i]:
                bi+="X"
                bigrams.append(bi)
                bi=slovo[i]
            else:
                bi += slovo[i]
                bigrams.append(bi)
                bi = ""
        else:
            bi+=slovo[i]
            if (len(slovo)-1==i):
                bigrams.append(bi)
    if len(bigrams[len(bigrams)-1])==1:
        bigrams[len(bigrams) - 1]+="X"

    return bigrams

def PlayfairCipher(bigrams, matrix):
    for i in range(len(bigrams)-1):
        bigrams[i]=bigrams[i].replace("I", "J")
    ciphered=[]
    cipheredword=""
    for chars in bigrams:
        (r1,c1)=FindChar(matrix,chars[0])
        (r2,c2)=FindChar(matrix,chars[1])
        if r1==r2:
            ciphered.append(matrix[r1][(c1+1)%5])
            ciphered.append(matrix[r2][(c2+1)%5])
        elif c1==c2:
            ciphered.append(matrix[(r1+1)%5][c1])
            ciphered.append(matrix[(r2+1)%5][c2])
        else:
            ciphered.append(matrix[r1][c2])
            ciphered.append(matrix[r2][c1])
    for i in range(len(ciphered)):
        cipheredword+=ciphered[i]
    return cipheredword

def FindChar(matrix, goal):
    for i,r in enumerate(matrix):
        if goal in r:
            return(i,r.index(goal))

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
        print("Enter the word you want to cipher")
        stroka=str(input("Word:"))
        bigrams=BigramsCreator(stroka)
        print("Enter the code")
        key=str(input("Code:"))
        matrix=MatrixCreator(key)
        print(PlayfairCipher(bigrams, matrix))
        print("Exiting to main menu")
        otvet=0
    elif otvet==2:
        flags=0
        if(MatrixCreator("wheatson")==['WHEAT', 'SONBC', 'DFGJK', 'LMPQR', 'UVXYZ']):
            flags+=1
        if(BigramsCreator("IDIOCY OFTEN LOOKS LIKE INTELLIGENCE") == ['ID', 'IO', 'CY', 'OF', 'TE', 'NL', 'OX', 'OK', 'SL', 'IK', 'EI', 'NT', 'EL', 'LI', 'GE', 'NC', 'EX']):
            flags+=1
        if(PlayfairCipher(['ID', 'IO', 'CY', 'OF', 'TE', 'NL', 'OX', 'OK', 'SL', 'IK', 'EI', 'NT', 'EL', 'LI', 'GE', 'NC', 'EX'],['WHEAT', 'SONBC', 'DFGJK', 'LMPQR', 'UVXYZ'])=="KFFBBZFMWASPNVCFDUKDAGCEWPQDPNBSNE"):
            flags+=1
        print("Tests passed: "+str(flags)+"/3")
        otvet=0
    else:
        print("Goodbye")
        runner=0
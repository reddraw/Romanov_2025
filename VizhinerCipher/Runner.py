def KeyWordGenerator(stroka,key):
    keyword = ""

    for i in range(len(stroka)):
        j = i
        if j // len(key) > 0:
            while j > len(key) - 1:
                j -= len(key)
            keyword += key[j]
        else:
            keyword += key[j]
    keyword = keyword.upper()
    return keyword

def VizhenerCipher(stroka, keyword):
    ciphered = ""
    stroka=stroka.upper()
    for i in range(len(keyword)):
        kodename=ord(keyword[i])+ord(stroka[i])-64
        if kodename>90:
            kodename-=26
        ciphered+=chr(kodename)

    return ciphered

def Decipher(ciphered,keyword):
    ciphered=ciphered.upper()
    deciphered=""
    for i in range(len(keyword)):
        codename=((ord(ciphered[i])-64)-(ord(keyword[i])-64))%26+64
        deciphered+=chr(codename)
    return deciphered

runner=1
otvet=0
key=""
stroka=""

while runner>0:
    if otvet==0:
        print("Print the number of operation you want to do")
        print("1. Cipher the word")
        print("2. Decipher the word")
        print("3. Test of Units")
        print("4 or any other. Exit")
        otvet=int(input("Number:"))
    if otvet==1:
        print("Enter the word you want to cipher")
        stroka=str(input("Word:"))
        print("Enter the code")
        key=str(input("Code:"))
        key=KeyWordGenerator(stroka,key)
        print(VizhenerCipher(stroka,key))
        print("Exiting to main menu")
        otvet=0
    elif otvet==2:
        print("Enter the ciphered word")
        stroka=str(input("Ciphered:"))
        print("Enter the keyword")
        key=str(input("Code:"))
        key=KeyWordGenerator(stroka,key)
        print(Decipher(stroka,key))
        print("Exiting to main menu")
        otvet=0
    elif otvet==3:
        flags=0
        if(KeyWordGenerator("slovo","kod")=="KODKO"):
            
            flags+=1
            print("Test 1 passed")
        else: print("Test 1 is not passed")
        if(VizhenerCypher("slovo","KODKO") == "DASGD"):
            flags+=1
            print("Test 2 passed")
        else: print("Test 2 is not passed")
        if(Decipher("DASGD", "KODKO")=="SLOVO"):
            flags+=1
            print("Test 3 passed")
        else: print("Test 3 is not passed")
        print("Tests passed: "+str(flags)+"/3")
        otvet=0
    else:
        print("Goodbye")
        runner=0





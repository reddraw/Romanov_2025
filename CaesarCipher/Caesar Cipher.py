def Encrypt(slovo, kod):
    slovo2=''
    for i in range(len(slovo)):
        number = ord(slovo[i])
        if (number >= 32 and number<=64):
            slovo2 += slovo[i]
        elif (number>96 and number<123):
            if(number+kod<123):
                slovo2 += chr(number + kod)
            elif (number + kod >= 123):
                slovo2 += chr(number + kod - 26)
        elif(number<91 and number>64):
            if(number+kod<91):
                slovo2+=chr(number+kod)
            elif(number+kod>=91):
                slovo2+=chr(number+kod-26)
    return (slovo2)
def Decrypt(slovo, kod):
    slovo2 = ''
    for i in range(len(slovo)):
        number = ord(slovo[i])
        if (number >= 32 and number <= 64):
            slovo2 += slovo[i]
        elif (number > 96 and number < 123):
            if (number - kod > 96):
                slovo2 += chr(number - kod)
            elif (number - kod <=96):
                slovo2 += chr(number - kod + 26)
        elif (number < 91 and number > 64):
            if (number - kod > 64):
                slovo2 += chr(number - kod)
            elif (number - kod <= 64):
                slovo2 += chr(number - kod + 26)
    return (slovo2)
def Runner(show):
    if(Encrypt("Bebra", 4)=="Fifve" and Decrypt("Fifve",4)=="Bebra"):
        show+=1
    if(Encrypt("Among Us!!",11)=="Lxzyr Fd!!" and Decrypt("Lxzyr Fd!!",11)=="Among Us!!"):
        show+=1
    if(Encrypt("waskf I'mhjlk kjl",3)=="zdvni L'pkmon nmo" and Decrypt("zdvni L'pkmon nmo",3)=="waskf I'mhjlk kjl"):
        show+=1
    return show
show=0
slovo = str(input("Print in case you want: 1) TEST to test the program, 2) any other word to cipher it"))

if(slovo=="TEST"):
    show=Runner(show)
    print("Number of Tests passed - ",show,"/3")
else:
    kod = int(input("Input key int"))
    print(slovo, "- main word")
    ciphered=Encrypt(slovo,kod)
    print(ciphered,"- ciphered word")
    print(Decrypt(ciphered, kod), "- deciphered word")
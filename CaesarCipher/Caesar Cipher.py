def Cipher(slovo, kod):
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

def Runner(show):
    if(Cipher("Bebra",4)=="Fifve"):
        show+=1
    if(Cipher("Among the stars I'm the only flying!",11)
    =="Lxzyr esp delcd T'x esp zywj qwjtyr!"):
        show+=1
    if(Cipher("zhakwong amm", 8)=="hpisewvo iuu"):
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
    print(Cipher(slovo, kod), "- ciphered word")
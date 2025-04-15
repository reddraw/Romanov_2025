def Cipher(slovo, kod):
    slovo2=''
    for i in range(len(slovo)):
        number = ord(slovo[i])
        if (number >= 32 and number<=64):
            slovo2 += slovo[i]
        elif (number + kod < 123):
            slovo2 += chr(number + kod)
        elif (number + kod >= 123):
            slovo2 += chr(number + kod - 26)
    return (slovo2)

def Runner(show):
    if(Cipher("bebra",4)=="fifve"):
        show+=1
    if(Cipher("among the stars i'm the only flying!",11)
    =="lxzyr esp delcd t'x esp zywj qwjtyr!"):
        show+=1
    if(Cipher("zhakwong amm", 8)=="hpisewvo iuu"):
        show+=1
    return show
show=0
slovo = str(input("Choose an option: 1) TEST to test, 2) any other word to cipher it"))
if(slovo=="TEST"):
    show=Runner(show)
    print("number of Tests passed - ",show,"/3")
else:
    slovo = slovo.lower()
    kod = int(input("Input key int"))
    print(slovo, "- main word")
    print(Cipher(slovo, kod), "- ciphered word")
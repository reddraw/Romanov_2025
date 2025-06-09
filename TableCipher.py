slovo=str(input("Input word/sentence"))
kod=int(input("Input key/number"))
t=0
cipher=[]
slovo2=""
for i in range(len(slovo)):
    if t<len(str(kod)):
        cipher+=str(kod)[t]
        t+=1
        if t==len(str(kod)):
            t=0
for i in range(len(slovo)):
    number=ord(slovo[i])
    cnumber=int(cipher[i])
    if(number>96 and number+cnumber<123):
        slovo2+=chr(number+cnumber)
    elif(number==32):
        slovo2+=slovo[i]
    elif(number+cnumber>122):
        slovo2+=number+cnumber-26
    elif(number>64 and cnumber+number<91):
        slovo2+=chr(number+cnumber)
    elif(number+cnumber>90):
        slovo2=chr(number+cnumber)
print(cipher)
print(slovo2)


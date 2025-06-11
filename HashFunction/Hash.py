import hashlib

def HashCreator(data: bytes)-> bytes:
    hesh=hashlib.sha256()
    hesh.update(data)
    return hesh.digest()

runner=1
otvet=0

while runner!=0:
    if otvet == 0:
        print("Write a number of an option from given")
        print("1. Hash the data")
        print("2 or other Exit")
        otvet=int(input())
    elif otvet == 1:
        print("Enter the data")
        data=str(input())
        data=bytes(data, 'utf-8')
        print("Hash is: "+HashCreator(data).hex())
        print("Exiting to menu...")
        otvet=0
    else:
        print("Goodbye")
        runner=0

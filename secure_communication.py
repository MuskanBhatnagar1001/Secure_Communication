print("MESSAGE SENDER:")
print("Hello MIT CELL : ")
key=int(input("PLEASE ENTER K VALUE TO SHIFT TRANSFORM MESSAGE : "))
message=input('NOW PLEASE TYPE YOUR MESSAGE : ')
alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
number='0123456789'
encrypt=''
decrypt=''
for i in message:
    if i in alphabet:
        position=alphabet.find(i)
        newposition=(position+key)%52
        encrypt+=alphabet[newposition]
    elif i in number:
        position=number.find(i)
        newposition=(position+key)%10
        encrypt+=number[newposition]
    elif i==' ':
        encrypt+="@"
    elif i=='.':
        encrypt+="#"
    elif i=='%':
        encrypt+="%"
    elif i=='*':
        encrypt+="*"
    else:
        encrypt=i
print("YOU SEND - ",encrypt)
print("\n\nMESSAGE RECEIVER:")
print("HELLO INSTRUCTOR : ")
print("YOU GOT A MESSAGE : ",encrypt)
key=int(input("TO READ THIS IN ORIGINAL PLEASE TYPE K VALUE PROVIDED BY CELL: "))
for i in encrypt:
    if i in alphabet:
        pos=alphabet.find(i)
        newpos=(pos-key)%52 
        decrypt+=alphabet[newpos]
    elif i in number:
        pos=number.find(i)
        newpos=(pos-key)%10
        decrypt+=number[newpos] 
    elif i=='@':
        decrypt+=" "
    elif i=='#':
        decrypt+="."
    elif i=='%':
        decrypt+="%"
    elif i=='*':
        decrypt+="*"
    else:
        decrypt=i
print("\nTHE ORIGINAL MESSAGE IS : ",decrypt)




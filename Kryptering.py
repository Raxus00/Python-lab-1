def menu():#Meny för valen som går att mata in
        print("\n")        
        print("[1] write a uncryped text.")
        print("[2] print the saved text.")
        print("[3] Encrypt the current saved text.")
        print("[4] decrypt the encrypted text.") 
        print("[5] Exit program.")
        print("\n")
        Choice=input("Choose what you want to do:")
        return Choice
def encryption(Key, text):
    count=0
    encrypted_message=""
    for k in Key: 
        new_number=0
        Key_values = ord(k)-65      
        for t in text:          
                if count<len(text):
                    t=text[count]
                    letter_values = ord(t)-65
                    if t==' ':  
                        encrypted_message+=t
                        count+=1
                        break
                    new_number=(Key_values+letter_values)%26
                    new_number=new_number+65
                    new_letter=chr(new_number)
                    encrypted_message+=new_letter
                    count+=1
                    break
    text=encrypted_message
    return text
def check_key():
    Key=input("Choose your Key(no numbers)")
    Key=Key.upper()
    while len(Key)<len(text):
        Key=Key+Key
    print("your key is", Key)
    return Key
def decryption(Key,text):
        check=input("Enter your key:")
        check=check.upper()
        if check==Key:
            count=0
            decrypted_message=""
        elif check!=Key:
            print("Wrong key")
            decryption(Key, text)
        for k in Key: 
            new_number=0
            Key_values = ord(k)-65      
            for t in text:          
                if count<len(text):
                    t=text[count]   
                    letter_values = ord(t)-65
                    if t==' ':
                        decrypted_message+=t
                        count+=1
                        break
                    new_number=(letter_values-Key_values)%26
                    new_number=new_number+65
                    new_letter=chr(new_number)
                    decrypted_message+=new_letter
                    count+=1
                    break
        text=decrypted_message
        return text
while True: 
    Choice = menu()
    if (Choice =='1'):
        text=input("Write your text:")
        text=text.upper()
    elif(Choice=='2'):
        print(f"your text is {text}"  )
    elif (Choice=='3'):
        Key=check_key()
        text=encryption(Key, text)
    elif (Choice=='4'):
        text=decryption(Key, text)
    elif (Choice=='5'):
        quit()
    else:
        print("\n", "Only numbers from 1 to 5 are premitted", "\n")
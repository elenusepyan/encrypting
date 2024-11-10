e = int(input('Enter value'))   
d = 26 - e  
result = '' 
command = int(input('Enter what you want? 1 - encrypt, 2 - decrypt: ')) 
text = input('Enter your text: ') 

if command == 1:  
    for i in text: 
        if i.isalpha(): 
            if i.islower(): 
                new = (ord(i) - ord('a') + e) % 26 + ord('a') 
            else: 
                new = (ord(i) - ord('A') + e) % 26 + ord('A') 
            result += chr(new) 
        else: 
            result += i 
    print(f'Encrypted text: {result}') 

elif command == 2:   
    for i in text: 
        if i.isalpha(): 
            if i.islower(): 
                new = (ord(i) - ord('a') - e) % 26 + ord('a') 
            else: 
                new = (ord(i) - ord('A') - e) % 26 + ord('A') 
            result += chr(new) 
        else: 
            result += i 
    print(f'Decrypted text: {result}') 

else: 
    print('Invalid command') 
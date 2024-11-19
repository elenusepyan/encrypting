def remove_duplicates(string): 
    result = "" 
    seen = set() 
    for char in string: 
        if char not in seen: 
            result += char 
            seen.add(char) 
    return result 

def create_key(string): 
    result1 = remove_duplicates(string.replace(' ', '').upper()) 
    result2 = []  

    for ascii_code in range(ord('A'), ord('Z')+1): 
        letter = chr(ascii_code) 
        if letter not in result1: 
            result2.append(letter) 

    key = result1 + ''.join(result2) 
    return key 

def encrypt(message, key): 
    encrypted_message = ""    
    for char in message: 
        if char.isalpha():  
            index = ord(char.upper()) - ord('A') 
            encrypted_char = key[index] 
            if char.islower(): 
                encrypted_message += encrypted_char.lower() 
            else: 
                encrypted_message += encrypted_char 

        else: 
            encrypted_message += char   
    return encrypted_message 
 
string = input('Enter text for key')
key = create_key(string) 
massage = input('Enter massage for encrypt')
encrypted_message = encrypt(massage, key) 

print(f"Key: {key}") 
print(f"Encrypted Message: {encrypted_message}") 
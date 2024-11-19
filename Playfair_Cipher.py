def process_sentence(sentence): 
    used_letters = set() 
    result = "" 
    for c in sentence.lower(): 
        if c == ' ': 
            continue 
        if c == 'j': 
            c = 'i' 
        if c not in used_letters and 'a' <= c <= 'z': 
            used_letters.add(c) 
            result += c 

    for c in range(ord('a'), ord('z') + 1): 
        if chr(c) != 'j' and chr(c) not in used_letters: 
            result += chr(c) 

    return result 

def prepare_text_for_playfair(text): 
    result = "" 
    i = 0 
    while i < len(text): 
        char = text[i].lower() 
        if char < 'a' or char > 'z': 
            i += 1 
            continue 
        result += char 
        if i + 1 < len(text) and text[i + 1].lower() == char: 
            result += 'z' 
        i += 1 

    if len(result) % 2 != 0: 
        result += 'z' 
    return result 

def find_position(letter, square): 
    for i in range(5): 
        for j in range(5): 
            if square[i][j] == letter: 
                return i, j 
    return -1, -1 

def encrypt_playfair(text, square): 
    encrypted_text = "" 
    for i in range(0, len(text), 2): 
        first, second = text[i], text[i + 1] 
        pos1, pos2 = find_position(first, square), find_position(second, square) 
        if pos1[0] == pos2[0]: 
            encrypted_text += square[pos1[0]][(pos1[1] + 1) % 5] 
            encrypted_text += square[pos2[0]][(pos2[1] + 1) % 5] 
        elif pos1[1] == pos2[1]: 
            encrypted_text += square[(pos1[0] + 1) % 5][pos1[1]] 
            encrypted_text += square[(pos2[0] + 1) % 5][pos2[1]] 
        else: 
            encrypted_text += square[pos1[0]][pos2[1]] 
            encrypted_text += square[pos2[0]][pos1[1]] 
    return encrypted_text 

def decrypt_playfair(text, square): 
    decrypted_text = "" 
    for i in range(0, len(text), 2): 
        first, second = text[i], text[i + 1] 
        pos1, pos2 = find_position(first, square), find_position(second, square) 
        if pos1[0] == pos2[0]: 
            decrypted_text += square[pos1[0]][(pos1[1] - 1) % 5] 
            decrypted_text += square[pos2[0]][(pos2[1] - 1) % 5] 
        elif pos1[1] == pos2[1]: 
            decrypted_text += square[(pos1[0] - 1) % 5][pos1[1]] 
            decrypted_text += square[(pos2[0] - 1) % 5][pos2[1]] 
        else: 
            decrypted_text += square[pos1[0]][pos2[1]] 
            decrypted_text += square[pos2[0]][pos1[1]] 
    return decrypted_text.replace('z', '') 

sentence = input("Enter the key phrase: ") 
processed = process_sentence(sentence) 
if len(processed) < 25: 
    print("Error: Key must contain at least 25 unique letters.") 
else: 
    square = [[processed[i * 5 + j] for j in range(5)] for i in range(5)] 
    print("Playfair Table:") 
    for row in square: 
        print(" ".join(row)) 

    text = input("Enter text to encrypt: ") 
    prepared_text = prepare_text_for_playfair(text) 
    print("Prepared text:", " ".join(prepared_text[i:i + 2] for i in range(0, len(prepared_text), 2))) 

    encrypted = encrypt_playfair(prepared_text, square) 
    print("Encrypted text:", encrypted) 

    new_text = input("Enter text to decrypt: ") 
    decrypted = decrypt_playfair(new_text, square) 
    print("Decrypted text:", decrypted)  
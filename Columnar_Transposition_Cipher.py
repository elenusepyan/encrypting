def encrypt(message, key):
    message = message.replace(" ", "").upper()
    while len(message) % key != 0:
        message += 'Z'
    num_rows = len(message) // key
    grid = ['' for _ in range(key)]
    for i in range(num_rows):
        for j in range(key):
            grid[j] += message[i * key + j]
    return ''.join(grid)

def decrypt(encrypted_message, key):
    num_rows = len(encrypted_message) // key
    grid = ['' for _ in range(key)]
    for j in range(key):
        grid[j] = encrypted_message[j * num_rows:(j + 1) * num_rows]
    decrypted_message = ''
    for i in range(num_rows):
        for j in range(key):
            decrypted_message += grid[j][i]
    return decrypted_message

key = int(input('Enter the key: '))
message = input('Enter your text: ')
encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)
print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)

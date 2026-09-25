# Caesar Cipher Decryption

text = input("Enter encrypted message: ")
shift = int(input("Enter shift value: "))

decrypted = ""

for char in text:
    if char.isalpha():
        if char.isupper():
            decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
    else:
        decrypted += char

print("Decrypted Message:", decrypted)
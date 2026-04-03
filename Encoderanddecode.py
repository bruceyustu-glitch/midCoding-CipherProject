choice = input("encode or decode?")
if choice == "encode":

def encrypt(text, shift):
    text = text.lower()
    encrypted_text = ""
    for char in text:
        if char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 +97)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    text = text.lower()
    decrypted_text = ""
    for char in text:
        if char.islower():
            decrypted_text += chr((ord(char) + shift - 97) % 26 +97)
        else:
            decrypted_text += char
    return decrypted_text

originalmessage = input("Please enter a msg to incode")
encryptedmessage = encrypt(originalmessage, 2)
print(encryptedmessage)
DecryptedMessage = decrypt(encryptedmessage, 2)
print(DecryptedMessage)

else:
message = input("Enter your message: ")
shift = int(input("Enter the shift number: "))
encoded = ""

for char in message:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        new_char = chr((ord(char) - start + shift) % 26 + start)
        encoded += new_char
    else:
        encoded += char

print("Encoded message:", encoded)
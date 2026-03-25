message = input("Enter your message: ")
shift = int(input("Enter the shift number: "))
encoded = ""

for char in message:
    if char.isalpha():
        # Determine if the character is uppercase or lowercase
        start = ord('A') if char.isupper() else ord('a')
        
        # Shift the character and wrap around the alphabet using modulo 26
        new_char = chr((ord(char) - start + shift) % 26 + start)
        encoded += new_char
    else:
        # Keep non-alphabet characters as they are
        encoded += char

print("Encoded message:", encoded)
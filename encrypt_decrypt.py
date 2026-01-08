def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, key):
    return encrypt(text, -key)

if __name__ == "__main__":
    print("1. Encrypt")
    print("2. Decrypt")
    choice = int(input("Choose option: "))

    message = input("Enter message: ")
    key = int(input("Enter key: "))

    if choice == 1:
        print("Encrypted Text:", encrypt(message, key))
    elif choice == 2:
        print("Decrypted Text:", decrypt(message, key))
    else:
        print("Invalid choice")

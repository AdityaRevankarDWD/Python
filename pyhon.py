import random

def encrypt_message(message, shift):
    """Encrypt a message using the Caesar cipher"""
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt_message(message, shift):
    """Decrypt a message encrypted with the Caesar cipher"""
    return encrypt_message(message, -shift)

def main():
    """Main function"""
    print("Welcome to the Encryption and Decryption Toll")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    choice = input("Enter your choice (1,or 2): ")
    if choice == '1':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value for the Caesar cipher: "))
        encrypted_message = encrypt_message(message, shift)
        print("The encrypted message is:", encrypted_message)
    elif choice == '2':
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value for the Caesar cipher: "))
        decrypted_message = decrypt_message(message, shift)
        print("The decrypted message is:", decrypted_message)
    else:
        print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
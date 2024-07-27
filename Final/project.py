import json
import random
import string
import os
from cryptography.fernet import Fernet

def generate_key():
    """
    Generate and save a new encryption key to 'secret.key'.
    This function creates a new encryption key using the Fernet algorithm and saves it to a file.
    This should be done once and the key should be kept secure.
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Load the encryption key from the 'secret.key' file.

    Returns:
        bytes: The encryption key.

    Raises:
        FileNotFoundError: If the 'secret.key' file does not exist.
    """
    if not os.path.exists("secret.key"):
        print("Key file not found.")
        generate_key()
    return open("secret.key", "rb").read()

def encrypt_message(message):
    """
    Encrypt a message using the encryption key from 'secret.key'.

    Args:
        message (str): The message to encrypt.

    Returns:
        bytes: The encrypted message.

    Raises:
        Exception: If encryption fails.
    """
    try:
        key = load_key()
        fernet = Fernet(key)
        encrypted_message = fernet.encrypt(message.encode())
        return encrypted_message
    except Exception as e:
        print(f"Encryption failed: {e}")
        return None

def decrypt_message(encrypted_message):
    """
    Decrypt an encrypted message using the encryption key from 'secret.key'.

    Args:
        encrypted_message (bytes): The encrypted message to decrypt.

    Returns:
        str: The decrypted message.

    Raises:
        Exception: If decryption fails.
    """
    try:
        key = load_key()
        fernet = Fernet(key)
        decrypted_message = fernet.decrypt(encrypted_message).decode()
        return decrypted_message
    except Exception as e:
        print(f"Decryption failed: {e}")
        return None

def generate_password(length=12):
    """
    Generate a strong password with a specified length.

    Args:
        length (int): The length of the password. Defaults to 12.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If length is less than 8.
    """
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def save_passwords(passwords):
    """
    Save encrypted passwords to a JSON file 'passwords.json'.

    Args:
        passwords (dict): A dictionary where the key is the service name and the value is the encrypted password.

    Raises:
        IOError: If saving the passwords file fails.
    """
    try:
        with open('passwords.json', 'w') as file:
            json.dump(passwords, file)
    except IOError as e:
        print(f"Failed to save passwords: {e}")

def load_passwords():
    """
    Load passwords from the 'passwords.json' file.

    Returns:
        dict: A dictionary where the key is the service name and the value is the encrypted password.

    Raises:
        IOError: If loading the passwords file fails.
    """
    if not os.path.exists('passwords.json'):
        return {}
    try:
        with open('passwords.json', 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Failed to decode passwords file.")
        return {}
    except IOError as e:
        print(f"Failed to load passwords: {e}")
        return {}

def add_password():
    """
    Prompt the user to add a new password. Generates a new password, encrypts it, and saves it.
    """
    service = input("Enter the service name: ").strip()
    if not service:
        print("Service name cannot be empty.")
        return
    password = generate_password()
    if not password:
        print("Failed to generate password.")
        return
    encrypted_password = encrypt_message(password)
    if not encrypted_password:
        print("Failed to encrypt password.")
        return
    passwords = load_passwords()
    passwords[service] = encrypted_password.decode()
    save_passwords(passwords)
    print(f"Password for {service} saved: {password}")

def view_passwords():
    """
    Display all saved passwords by decrypting them.
    """
    passwords = load_passwords()
    if not passwords:
        print("No passwords found.")
        return
    for service, encrypted_password in passwords.items():
        decrypted_password = decrypt_message(encrypted_password.encode())
        if decrypted_password:
            print(f"Service: {service}, Password: {decrypted_password}")

def main():
    """
    Main function to run the password manager. Provides a menu for the user to add or view passwords.
    """
    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Exit")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            add_password()
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

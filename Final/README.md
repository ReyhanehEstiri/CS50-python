# Password Generator & Manager

## Video Demo: <https://youtu.be/3DAFDkIb9wk?si=HgrEFBRmRE0Nxqbk>
## Overview

This Python script is a simple password manager that allows you to securely store and retrieve passwords. It uses encryption to protect the stored passwords and generates random passwords for new services.

## Features

- **Generate a new encryption key**: Used for encrypting and decrypting passwords.
- **Encrypt and decrypt messages**: Securely encrypt and decrypt passwords using the `cryptography` library.
- **Generate strong passwords**: Create passwords with a mix of letters, digits, and punctuation.
- **Save and load passwords**: Store encrypted passwords in a JSON file and retrieve them later.
- **Add and view passwords**: Add new passwords to the manager and view saved passwords.

## Requirements

- Python 3.x
- `cryptography` library (install with `pip install cryptography`)

## Usage

### Generate Encryption Key

Before running the password manager for the first time, you need to generate an encryption key. Run the script once to create the `secret.key` file.

You will be presented with a menu with the following options:

- **Add Password:** Add a new password for a service. The password will be generated automatically, encrypted, and saved.
- **View Passwords:** View all saved passwords. The application will decrypt and display the passwords for all services.
- **Exit:** Exit the application.

###  Adding a Password
Select option **1** to add a new password.
Enter the **name** of the service for which you want to save the password.
The application will generate a new password, encrypt it, and save it along with the service name.

### Viewing Passwords.
Select option **2** to view all saved passwords.
The application will decrypt and display the passwords for all services.

### Exit the Program
Select option **3** to exit.


```bash
python project.py
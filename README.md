# Encryption and Decryption Application

This Python application provides a simple command-line interface for encrypting and decrypting files and folders. It uses the ChaCha20Poly1305 algorithm for encryption and decryption. The application includes three main scripts:

1. 'main.py': Allows users to choose between encryption and decryption and executes the corresponding functionality.
2. 'encrypt.py': Encrypts a specified folder using a password-derived key and stores relevant security information.
3. 'decrypt.py': Decrypts an encrypted folder using the provided password and security information.
4. 'cryptography_utils.py': Contains utility functions for key generation, file encryption, and file decryption.


## Usage

> [!CAUTION]
> The current decryptor exclusively decrypts files to the primary output directory and lacks the capability to decrypt files within subdirectories. It is advisable to refrain from encrypting directories that contain subdirectories and instead focus on encrypting individual files directly within the main directory.


1. Run main.py and choose between encryption (E) or decryption (D).
1. For encryption, provide a password, output directory, and the path to the folder to be encrypted.
1. For decryption, provide the path to the folder to be decrypted.
4. The application will generate necessary security files during encryption and use them during decryption.

## Requirements
- Python 3.x
- Required Python packages: 'cryptography'

## Important Notes
1. Ensure you have the required dependencies installed ('cryptography').
2. Security files are generated during encryption and are essential for decryption.
3. Keep your password secure and do not lose the security files.

## Author

> [!NOTE]
> Feel free to customize this template based on your project's details and add any specific instructions or information.

Matteo B. & Open AI ChatGPT 3.5

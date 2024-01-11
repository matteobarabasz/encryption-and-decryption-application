import os
import re
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

SCRYPT_N = 2**14
SCRYPT_R = 8
SCRYPT_P = 1
PBKDF2_ITERATIONS = 100000


def generate_key_from_password(password, salt=None, iterations=None):
    if salt is None:
        salt = os.urandom(16)
    if re.match("^[0-9]+$", password):
        kdf = Scrypt(
            salt=salt,
            length=32,
            n=SCRYPT_N,
            r=SCRYPT_R,
            p=SCRYPT_P,
            backend=default_backend(),
        )
    else:
        iterations = iterations or PBKDF2_ITERATIONS
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=iterations,
            backend=default_backend(),
        )
    key = kdf.derive(password.encode())
    return salt, key


def encrypt_file(key, input_file_path, output_file_path):
    chacha = ChaCha20Poly1305(key)
    with open(input_file_path, "rb") as f:
        plaintext = f.read()
    nonce = os.urandom(12)
    ciphertext = chacha.encrypt(nonce, plaintext, None)
    with open(output_file_path, "wb") as f:
        f.write(nonce)
        f.write(ciphertext)


def encrypt_folder(key, input_folder_path, output_folder_path):
    for dirpath, dirnames, filenames in os.walk(input_folder_path):
        for filename in filenames:
            input_file_path = os.path.join(dirpath, filename)
            output_file_path = os.path.join(
                output_folder_path, os.path.relpath(input_file_path, input_folder_path)
            )
            encrypt_file(key, input_file_path, output_file_path)


def decrypt_file(key, input_file_path, output_file_path):
    with open(input_file_path, "rb") as f:
        nonce = f.read(12)
        ciphertext = f.read()
        chacha = ChaCha20Poly1305(key)
        plaintext = chacha.decrypt(nonce, ciphertext, None)
    with open(output_file_path, "wb") as f:
        f.write(plaintext)


def decrypt_folder(key, input_folder_path, output_folder_path):
    for dirpath, dirnames, filenames in os.walk(input_folder_path):
        for filename in filenames:
            input_file_path = os.path.join(dirpath, filename)
            output_file_path = os.path.join(
                output_folder_path, os.path.relpath(input_file_path, input_folder_path)
            )
            decrypt_file(key, input_file_path, output_file_path)
    print("Decryption completed successfully.")

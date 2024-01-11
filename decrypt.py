import os
import time
from getpass import getpass  # Import getpass to securely prompt for password
from cryptography_utils import generate_key_from_password, decrypt_folder


def get_user_password():
    return getpass("Enter your password: ")


def main():
    decrypt_path = input("Enter the path to decrypt: ")

    if not os.path.exists(decrypt_path):
        print("Invalid path. Please provide a valid path.")
        return

    security_folder = os.path.join(decrypt_path, "security")
    if not os.path.exists(security_folder):
        print("Security folder not found. Please make sure the path is correct.")
        return

    with open(os.path.join(security_folder, "psw.txt"), "r") as f:
        password1 = get_user_password()

    with open(os.path.join(security_folder, "salt.txt"), "rb") as f:
        salt1 = f.read()

    key1 = generate_key_from_password(password1, salt1)[1]  # Take only the key part

    output_directory = os.path.join(decrypt_path, "decryptedfolder")
    os.makedirs(output_directory, exist_ok=True)

    start_time = time.time()
    decrypt_folder(
        key1, os.path.join(decrypt_path, "encryptedfolder"), output_directory
    )
    end_time = time.time()

    print(f"Decryption completed in {end_time - start_time:.2f} seconds.")


if __name__ == "__main__":
    main()

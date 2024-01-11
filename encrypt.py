import os
import shutil
import time
import secrets
from cryptography_utils import generate_key_from_password, encrypt_folder

def get_user_password():
    user_choice = input("Do you want to enter your own password? (Y/N): ").lower()
    if user_choice == "y":
        return input("Enter your password: ")
    elif user_choice == "n":
        return secrets.token_urlsafe(16)
    else:
        print("Invalid choice. Generating a random password.")
        return secrets.token_urlsafe(16)

def get_input_folder_path():
    return input("Enter the path to the input folder: ")

def main():
    password = get_user_password()
    salt, key = generate_key_from_password(password)

    output_directory = input("Enter the path to the output directory: ")
    security_folder = os.path.join(output_directory, "security")
    os.makedirs(security_folder, exist_ok=True)

    with open(os.path.join(security_folder, "psw.txt"), "w") as f:
        f.write(password)

    with open(os.path.join(security_folder, "salt.txt"), "wb") as f:
        f.write(salt)

    with open(os.path.join(security_folder, "key.txt"), "wb") as f:
        f.write(key)

    input_folder_path = get_input_folder_path()
    output_folder_path = os.path.join(output_directory, "encryptedfolder")
    shutil.copytree(input_folder_path, output_folder_path)

    start_time = time.time()
    encrypt_folder(key, input_folder_path, output_folder_path)
    end_time = time.time()

    print(f"Encryption completed in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()

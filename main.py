from encrypt import main as encrypt_main
from decrypt import main as decrypt_main

if __name__ == "__main__":
    user_choice = input("Would you like to encrypt or decrypt? (E/D): ").lower()

    if user_choice == "e":
        encrypt_main()
    elif user_choice == "d":
        decrypt_main()
    else:
        print("Invalid choice. Please enter 'E' or 'D.'")

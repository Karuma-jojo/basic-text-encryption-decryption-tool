from caeser import encrypt, decrypt

print("Basic Text Encryption and Decryption Tool")

while True:
    print()
    print("1. Caesar cipher")
    print("2. Fernet encryption")
    print("3. Exit")

    choice = input("Choose 1, 2, or 3: ")

    if choice == "1":
        print("Caesar selected. Implementation coming next.")
    elif choice == "2":
        print("Fernet selected. Implementation coming next.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

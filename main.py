from caeser import encrypt, decrypt

print("Basic Text Encryption and Decryption Tool")

while True:
    print()
    print("1. Caesar cipher")
    print("2. Fernet encryption")
    print("3. Exit")

    choice = input("Choose 1, 2, or 3: ")

    if choice == "1":
        operation = input("1. Encrypt / 2. Decrypt: ")

        if operation != "1" and operation != "2":
            print("Invalid operation.")
            continue

        text = input("Enter text: ")

        try:
            shift = int(input("Enter shift: "))
        except ValueError:
            print("Shift must be a whole number.")
            continue

        if operation == "1":
            result = encrypt(text, shift)
        else:
            result = decrypt(text, shift)

        print("Result:", result)

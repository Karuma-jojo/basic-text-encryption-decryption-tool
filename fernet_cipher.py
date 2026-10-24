from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    return key.decode("utf-8")


def encrypt(text, key):
    cipher = Fernet(key)
    encrypted_bytes = cipher.encrypt(text.encode("utf-8"))
    return encrypted_bytes.decode("utf-8")


def decrypt(encrypted_text, key):
    cipher = Fernet(key)
    decrypted_bytes = cipher.decrypt(encrypted_text.encode("utf-8"))
    return decrypted_bytes.decode("utf-8")

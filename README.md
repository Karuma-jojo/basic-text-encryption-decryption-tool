# Basic Text Encryption and Decryption Tool

A small Streamlit app with Caesar, Vigenère, and Fernet encryption and decryption.

[Open the app](https://basic-text-encryption-decryption-tool.streamlit.app/)

## Run

From the project folder:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Use

1. Choose a cipher and Encrypt or Decrypt.
2. Enter the message and its shift, keyword, or Fernet key.
3. Click Encrypt or Decrypt. You can download the result.
4. Open **Pseudocode reference** to explain the selected cipher.

For Fernet, generate and save a key before encrypting. Decryption needs the
original key. Closing or refreshing the browser session can clear the key.

Caesar and Vigenère are educational ciphers. Fernet's cryptographic operations
are provided by the `cryptography` library.

## Files

| File | Purpose |
|---|---|
| `app.py` | Browser interface and editable pseudocode for all three ciphers. |
| `caeser.py` | Caesar encryption and decryption. |
| `vigenere_cipher.py` | Vigenère encryption and decryption. |
| `fernet_cipher.py` | Fernet key generation, encryption, and decryption. |
| `requirements.txt` | Python dependencies. |
| `README.md` | Setup and usage instructions. |

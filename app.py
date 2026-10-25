import streamlit as st
from cryptography.fernet import InvalidToken
import caeser
import fernet_cipher


st.set_page_config(page_title="Text Encryption Tool", page_icon="🔐")
st.title("Text Encryption Tool")

cipher = st.selectbox("Choose a cipher", ["Caesar", "Fernet"])
operation = st.radio("Operation", ["Encrypt", "Decrypt"], horizontal=True)

# This copy keeps the key when the Fernet controls are hidden.
if "saved_fernet_key" not in st.session_state:
    st.session_state["saved_fernet_key"] = ""

if cipher == "Caesar":
    shift_text = st.text_input("Shift (whole number)", value="6")
    pseudocode = """ENCRYPT(text, shift)
  Reduce shift to its remainder after division by 26.
  Start with an empty result.
  For each character:
    If it is not an English letter, copy it unchanged and continue.
    Choose the uppercase or lowercase alphabet to match the letter.
    Find the letter's position from 0 to 25.
    Add the shift to its position.
    If the new position is at least 26, subtract 26.
    Append the letter at the new position.
  Return the result.

DECRYPT(text, shift)
  Encrypt the text using the negative of the shift."""
else:
    if "fernet_key_input" not in st.session_state:
        st.session_state["fernet_key_input"] = st.session_state["saved_fernet_key"]

    if st.button("Generate key", disabled=operation == "Decrypt"):
        st.session_state["fernet_key_input"] = fernet_cipher.generate_key()

    key = st.text_input("Secret key", type="password", key="fernet_key_input")
    st.session_state["saved_fernet_key"] = key
    st.caption("Save your key before closing or refreshing; decryption needs that same key.")

    if key:
        st.download_button(
            "Save key", data=key, file_name="fernet.key", mime="text/plain",
            on_click="ignore"
        )

    pseudocode = """GENERATE_KEY
  Ask the Fernet library to generate a secret key.
  Return the key as text.

ENCRYPT(text, key)
  Convert the text to UTF-8 bytes.
  Ask Fernet to encrypt those bytes using the key.
  Return the encrypted token as text.

DECRYPT(token, key)
  Convert the token text to bytes.
  Ask Fernet to verify and decrypt using the original key.
  If this fails, display an error.
  Otherwise return the decrypted bytes as UTF-8 text."""

text = st.text_area("Message or encrypted text", height=160)
result = None

if st.button(operation, type="primary"):
    if cipher == "Caesar":
        try:
            shift = int(shift_text)
        except ValueError:
            st.error("Enter a whole number for the shift, such as 6.")
        else:
            if operation == "Encrypt":
                result = caeser.encrypt(text, shift)
            else:
                result = caeser.decrypt(text, shift)
    elif not key:
        st.error("Generate or paste your secret key first.")
    else:
        try:
            if operation == "Encrypt":
                result = fernet_cipher.encrypt(text, key)
            else:
                result = fernet_cipher.decrypt(text, key)
        except InvalidToken:
            st.error("Could not decrypt. Check the key and encrypted text.")
        except UnicodeDecodeError:
            st.error("The decrypted content is not valid UTF-8 text.")
        except ValueError:
            st.error("Invalid key. Generate a key or paste your original Fernet key.")

if result is not None:
    st.text_area("Result", value=result, height=160, disabled=True)
    st.download_button(
        "Save result", data=result, file_name="result.txt", mime="text/plain",
        on_click="ignore"
    )

with st.expander("Pseudocode reference"):
    st.code(pseudocode, language="text")

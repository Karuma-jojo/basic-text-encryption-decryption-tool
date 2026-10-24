import streamlit as st
from cryptography.fernet import InvalidToken
import fernet_cipher


st.set_page_config(page_title="Text Encryption Tool", page_icon="🔐")

st.title("Text Encryption Tool")
st.caption("Fernet encryption and decryption")

if "fernet_key" not in st.session_state:
    st.session_state["fernet_key"] = ""

operation = st.radio("Operation", ["Encrypt", "Decrypt"], horizontal=True)

if st.button("Generate key", disabled=operation == "Decrypt"):
    st.session_state["fernet_key"] = fernet_cipher.generate_key()

key = st.text_input("Secret key", type="password", key="fernet_key")
st.caption("Save your key before closing or refreshing; decryption needs that same key.")

if key:
    st.download_button(
        "Save key", data=key, file_name="fernet.key", mime="text/plain",
        on_click="ignore"
    )

text = st.text_area("Message or encrypted text", height=160)

if st.button(operation, type="primary"):
    if not key:
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
        else:
            st.text_area("Result", value=result, height=160, disabled=True)
            st.download_button(
                "Save result", data=result, file_name="result.txt", mime="text/plain",
                on_click="ignore"
            )

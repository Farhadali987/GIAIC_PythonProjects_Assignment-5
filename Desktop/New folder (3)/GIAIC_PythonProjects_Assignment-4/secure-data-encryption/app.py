import streamlit as st
from cryptography.fernet import Fernet
import hashlib

# --- Page Config ---
st.set_page_config(page_title="Secure Data Encryption", layout="centered")

# --- Session State Initialization ---
if "fernet_key" not in st.session_state:
    st.session_state.fernet_key = Fernet.generate_key()

if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = {}

if "authorized" not in st.session_state:
    st.session_state.authorized = True

if "last_page" not in st.session_state:
    st.session_state.last_page = "Home"

fernet = Fernet(st.session_state.fernet_key)

# --- Utility Function: SHA-256 Hashing ---
def hash_passkey(passkey: str) -> str:
    return hashlib.sha256(passkey.encode()).hexdigest()

# --- Insert Encrypted Data ---
def insert_data(user_id: str, text: str, passkey: str):
    encrypted_text = fernet.encrypt(text.encode()).decode()
    hashed_passkey = hash_passkey(passkey)
    st.session_state.stored_data[user_id] = {
        "encrypted_text": encrypted_text,
        "passkey": hashed_passkey
    }
    st.success(f"✅ Data securely stored for User ID: *{user_id}*")

# --- Retrieve & Decrypt Data ---
def retrieve_data(user_id: str, passkey: str):
    if user_id not in st.session_state.stored_data:
        st.error("❌ No data found for this User ID.")
        return

    if st.session_state.failed_attempts.get(user_id, 0) >= 3:
        st.session_state.authorized = False
        st.warning("⚠ Too many failed attempts. Please log in again.")
        st.experimental_rerun()
        return

    if hash_passkey(passkey) == st.session_state.stored_data[user_id]["passkey"]:
        decrypted = fernet.decrypt(st.session_state.stored_data[user_id]["encrypted_text"].encode()).decode()
        st.success("✅ Decrypted Data:")
        st.code(decrypted, language="text")
        st.session_state.failed_attempts[user_id] = 0
    else:
        st.session_state.failed_attempts[user_id] = st.session_state.failed_attempts.get(user_id, 0) + 1
        st.error(f"❌ Incorrect passkey. Attempts left: {3 - st.session_state.failed_attempts[user_id]}")

# --- Admin Login Page ---
def login_page():
    st.title("🔐 Admin Reauthorization Required")
    st.info("You have exceeded the maximum allowed attempts.")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.session_state.authorized = True
            st.session_state.failed_attempts.clear()
            st.success("✅ Login successful!")
            st.experimental_rerun()
        else:
            st.error("❌ Invalid admin credentials.")

# --- Animated Signature ---
def show_signature():
    st.markdown(
        """
        <style>
        .signature {
            font-family: 'Courier New', monospace;
            color: #39FF14;
            font-size: 20px;
            text-align: center;
            animation: blink 1s infinite;
            margin-top: 40px;
        }
        @keyframes blink {
            0% {opacity: 1;}
            50% {opacity: 0.2;}
            100% {opacity: 1;}
        }
        </style>
        <div class="signature">Made with ❤ by <strong>Farhad Gul</strong></div>
        """,
        unsafe_allow_html=True
    )

# --- Main Application ---
def main():
    st.sidebar.title("🔐 Secure Data App")
    menu = st.sidebar.radio("Navigate", ["Home", "Insert Data", "Retrieve Data", "Admin Login"])

    if not st.session_state.authorized and menu != "Admin Login":
        st.session_state.last_page = menu
        login_page()
        return

    if menu == "Home":
        st.title("Welcome to Secure Data Encryption System")
        st.markdown(
            "This app allows you to *encrypt and store* sensitive data securely "
            "and *retrieve it* with a passkey."
        )

    elif menu == "Insert Data":
        st.title("📥 Store Your Secure Data")
        with st.form("insert_form"):
            user_id = st.text_input("User ID")
            data = st.text_area("Enter the Data to Encrypt")
            passkey = st.text_input("Set a Secure Passkey", type="password")
            submitted = st.form_submit_button("Store Data")

            if submitted:
                if user_id and data and passkey:
                    insert_data(user_id, data, passkey)
                else:
                    st.warning("Please fill in all fields.")

    elif menu == "Retrieve Data":
        st.title("🔓 Retrieve Your Encrypted Data")
        with st.form("retrieve_form"):
            user_id = st.text_input("User ID")
            passkey = st.text_input("Enter Your Passkey", type="password")
            submitted = st.form_submit_button("Decrypt Data")

            if submitted:
                if user_id and passkey:
                    retrieve_data(user_id, passkey)
                else:
                    st.warning("Both fields are required.")

    elif menu == "Admin Login":
        login_page()

    show_signature()

# --- Run App ---
if __name__ == "__main__":
    main()

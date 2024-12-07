import cryptography as cpt
from cryptography.fernet import Fernet


def generate_key():
    """
    Generate a key and save it to a file.

    Returns:
        key: bytes
    """
    key = Fernet.generate_key()
    save_key(key)
    return key


def load_key():
    """
    Load the key from the current directory.

    Returns:
        key: bytes
    """
    try:
        with open("key.key", "rb") as key_file:
            if key_file != None:
                key = key_file.read()
                return key
            else:
                key = generate_key()
                if(key == None):
                    raise Exception("failed to generate key")
                return key
    except Exception as e:
        print(f"An error occurred in load_key: {e}")
        return None


def save_key(key):
    """
    Save the key to a file.

    Args:
        key: bytes
    """
    try:
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    except Exception as e:
        print(f"An error occurred in save_key: {e}")
    

def encrypt(text):
    """
    Encrypt text.

    Args:
        text: string

    Returns:
        encrypted_text: string
    """
    try: 
        text = text.encode()
        f = Fernet(KEY)
        encrypted_text = f.encrypt(text)
        return encrypted_text.decode()
    except Exception as e:
        print(f"An error occurred in encrypt: {e}")
        return None


def decrypt(text):
    """
    Decrypt text.

    Args:
        text: string

    Returns:
        decrypted_text: string
    """
    try:
        text = text.encode()
        f = Fernet(load_key())
        decrypted_text = f.decrypt(text)
        return decrypted_text.decode()
    except Exception as e:
        print(f"An error occurred in decrypt: {e}")
        return None


def test_encrypt_decrypt():
    """
    Test the encrypt and decrypt functions.
    """
    global KEY
    try:
        load_key()
    except Exception as e:
        print(f"An error occurred in test_encrypt_decrypt: {e}")
    
    text = "This is a test."
    encrypted_text = encrypt(text)
    print(f"Encrypted: {encrypted_text}")

    decrypted_text = decrypt(encrypted_text)
    print(f"Decrypted: {decrypted_text}")
    
    assert text == decrypted_text
    print("Test passed.")


if __name__ == "__main__":
    test_encrypt_decrypt()
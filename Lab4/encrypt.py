import cryptography

def encrypt(text):
    """
    Encrypt text.

    Args:
        text: string

    Returns:
        encrypted_text: string
    """
    return cryptography.encrypt(text)


def decrypt(text):
    """
    Decrypt text.

    Args:
        text: string

    Returns:
        decrypted_text: string
    """
    return cryptography.decrypt(text)

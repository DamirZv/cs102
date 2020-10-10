
def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    keyword_length = len(keyword)
    keyword_as_int = [ord(i) for i in keyword]
    plaintext_as_int = [ord(i) for i in plaintext]
    ciphertext = ""
    for i in range(len(plaintext_as_int)):
             value = (plaintext_as_int[i] + keyword_as_int[i % keyword_length]) % 26
             ciphertext += chr(value+65)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    keyword_length = len(keyword)
    keyword_as_int = [ord(i) for i in keyword]
    ciphertext_as_int = [ord(i) for i in ciphertext]
    plaintext = ""
    for i in range(len(ciphertext_as_int)):
             value = (ciphertext_as_int[i] - keyword_as_int[i % keyword_length]+26) % 26
             plaintext += chr(value + 65)
    return plaintext


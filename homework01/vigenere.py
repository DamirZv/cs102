
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
    
    ciphertext = ""
    k = 0
    for i in plaintext:
        shift = ord(keyword[k % len(keyword)].lower()) - 97
        k += 1
        if 64 < ord(i) < 91:
            x = ord(i) + shift % 26
            if x > 90:
                x = 64 + x % 90
                ciphertext += chr(x)
            else:
                ciphertext += chr(x)
        elif 96 < ord(i) < 123:
            x = ord(i) + shift % 26
            if x > 122:
                x = 97 + x % 123
                ciphertext += chr(x)
            else:
                ciphertext += chr(x)
        else:
            ciphertext += i
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

    plaintext = ""
    k = 0
    for i in ciphertext:
        shift = ord(keyword[k % len(keyword)].lower()) - 97
        k += 1
        if 64 < ord(i) < 91:
            x = ord(i) - (shift % 26)
            if x < 65:
                x = 90 + (x - 64)
                plaintext += chr(x)
            else:
                plaintext += chr(x)
        elif 96 < ord(i) < 123:
            x = ord(i) - (shift % 26)
            if x < 97:
                x = 122 + (x - 96)
                plaintext += chr(x)
            else:
                plaintext += chr(x)
        else:
            plaintext += i
    return plaintext


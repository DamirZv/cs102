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
        shift = ord(keyword[k % len(keyword)].lower()) - ord("a")
        k += 1
        if ord("@") < ord(i) < ord("["):
            x = ord(i) + shift % 26
            if x > ord("Z"):
                x = ord("@") + x % ord("Z")
                ciphertext += chr(x)
            else:
                ciphertext += chr(x)
        elif ord("`") < ord(i) < ord("{"):
            x = ord(i) + shift % 26
            if x > ord("z"):
                x = ord("a") + x % ord("{")
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
        shift = ord(keyword[k % len(keyword)].lower()) - ord("a")
        k += 1
        if ord("@") < ord(i) < ord("["):
            x = ord(i) - (shift % 26)
            if x < ord("A"):
                x = ord("Z") + (x - ord("@"))
                plaintext += chr(x)
            else:
                plaintext += chr(x)
        elif ord("`") < ord(i) < ord("{"):
            x = ord(i) - (shift % 26)
            if x < ord("a"):
                x = ord("z") + (x - ord("`"))
                plaintext += chr(x)
            else:
                plaintext += chr(x)
        else:
            plaintext += i
    return plaintext

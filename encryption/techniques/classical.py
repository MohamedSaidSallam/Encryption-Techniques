UPPERCASE_UNICODE_START = 65
LOWERCASE_UNICODE_START = 97

CAESAR_DEFAULT_KEY = 3
caesarCipherEncryptParam = f"key size (shift), default: {CAESAR_DEFAULT_KEY}"


def caesarCipherEncrypt(input, param):
    output = ""

    key = int(param[0]) if param else CAESAR_DEFAULT_KEY

    for char in input:
        if (char.isupper()):
            output += chr((ord(char) + key - UPPERCASE_UNICODE_START) %
                          26 + UPPERCASE_UNICODE_START)
        else:
            output += chr((ord(char) + key - LOWERCASE_UNICODE_START) %
                          26 + LOWERCASE_UNICODE_START)

    return output

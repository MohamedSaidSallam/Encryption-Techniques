UPPERCASE_UNICODE_START = ord('A')
LOWERCASE_UNICODE_START = ord('a')


def getUnicodeStart(char):
    return UPPERCASE_UNICODE_START if char.isupper() else LOWERCASE_UNICODE_START


CAESAR_DEFAULT_KEY = 3
caesarCipherEncryptParam = f"key size (shift), default: {CAESAR_DEFAULT_KEY}"


def caesarCipherEncrypt(input, param):
    key = int(param[0]) if param else CAESAR_DEFAULT_KEY

    output = []
    for line in input:
        line = line.strip()
        currentOutput = ""
        for char in line:
            unicodeStart = getUnicodeStart(char)

            currentOutput += chr((ord(char) + key - unicodeStart) %
                                 26 + unicodeStart)

        output.append(currentOutput)
    return output


vigenereCipherEncryptParam = "mode(0: repeating, 1: auto), key"


def vigenereCipherEncrypt(input, param):
    isRepeating, key = not bool(int(param[0])), param[1]

    output = []
    keyI = 0
    combinedInput = ''.join([line.strip() for line in input])
    for line in input:
        currentOutput = ""
        line = line.strip()

        for i in range(len(line)):
            currentKey = key[keyI % len(key)] if isRepeating else (
                key[keyI] if keyI < len(key) else combinedInput[keyI-len(key)])
            keyI += 1
            startInput = getUnicodeStart(line[i])
            startKey = getUnicodeStart(currentKey)
            currentOutput += chr(((ord(line[i]) + ord(currentKey) -
                                   startKey - startInput) % 26) + startInput)
        output.append(currentOutput)
    return output


vernamCipherEncryptParam = "key"


def vernamCipherEncrypt(input, param):
    key = param[0]

    output = []
    for line in input:
        currentOutput = ""
        line = line.strip()

        unicodeStart = getUnicodeStart(key[0])
        for i in range(len(line)):
            currentOutput += chr((((ord(line[i])-unicodeStart)
                                   + (ord(key[i])-unicodeStart)) % 26)+unicodeStart)
        output.append(currentOutput)
    return output
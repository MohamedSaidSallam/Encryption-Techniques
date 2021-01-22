import numpy as np

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


hillCipherEncryptParam = "key matrix (elements seperated by ',', e.g. 5,17,8,3)"


def hillCipherEncrypt(input, param):
    keyArray = list(map(lambda item: int(item), param[0].split(',')))
    keyMatrixSize = 3 if len(keyArray) == 9 else 2
    key = np.matrix([keyArray[(keyMatrixSize * i):(keyMatrixSize * i) +
                              keyMatrixSize] for i in range(keyMatrixSize)])

    output = []
    for line in input:
        currentOutput = ""
        line = line.strip()

        while(len(line) % keyMatrixSize != 0):
            line += 'Z'

        for i in range(0, len(line), keyMatrixSize):
            inputMatrix = np.zeros([keyMatrixSize, 1])
            for j in range(keyMatrixSize):
                inputMatrix[j][0] = (
                    ord(line[i+j]) - UPPERCASE_UNICODE_START) % 26

            resultMatrix = key@inputMatrix
            for value in resultMatrix:
                currentOutput += chr(int(((value % 26) +
                                          UPPERCASE_UNICODE_START).flat[0]))

        output.append(currentOutput)
    return output

OUTPUT_FOLDER = 'output/'


def main(inputPath, outputPath, encrypt, algorithmParam):
    with open(inputPath, 'r') as inputFile:
        input = inputFile.readlines()
    result = encrypt(input, algorithmParam)
    with open(OUTPUT_FOLDER + outputPath, 'w') as outputFile:
        outputFile.write('\n'.join(result))

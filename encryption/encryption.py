OUTPUT_FOLDER = 'output/'


def main(inputPath, outputPath, encrypt, algorithmParam):
    with open(inputPath, 'r') as inputFile:
        input = inputFile.readlines()
    result = []
    for line in input:
        result.append(encrypt(line.strip(), algorithmParam))
    with open(OUTPUT_FOLDER + outputPath, 'w') as outputFile:
        outputFile.write('\n'.join(result))

OUTPUT_FOLDER = 'output/'


def main(inputPath, outputPath):
    with open(inputPath, 'r') as inputFile:
        input = inputFile.read()
    print(f'input: {input}')
    result = "output"
    with open(OUTPUT_FOLDER + outputPath, 'w') as outputFile:
        outputFile.write(result)

import argparse

from encryption.encryption import main

parser = argparse.ArgumentParser(
    description=f'A simple python script that offers multiple simple impementation for encryption techniques.',
    epilog='Source: https://github.com/TheDigitalPhoenixX/Encryption-Techniques'
)
parser.add_argument("-i", "--input", type=str, required=True,
                    help="Path to input file")
parser.add_argument("-o", "--output", type=str, default='output.txt',
                    help="Path to output file. (default: %(default)s)")

args = parser.parse_args()

main(inputPath=args.input,
     outputPath=args.output)

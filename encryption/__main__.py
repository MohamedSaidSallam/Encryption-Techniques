import argparse

from encryption.encryption import main
from encryption.techniques.classical import caesarCipherEncrypt, caesarCipherEncryptParam

encryptionTechniques = [
    (caesarCipherEncrypt, caesarCipherEncryptParam)
]

parser = argparse.ArgumentParser(
    description=f'A simple python script that offers multiple simple impementation for encryption techniques.',
    epilog='Source: https://github.com/TheDigitalPhoenixX/Encryption-Techniques'
)
parser.add_argument("-i", "--input", type=str, required=True,
                    help="Path to input file")
parser.add_argument("-o", "--output", type=str, default='output.txt',
                    help="Path to output file. (default: %(default)s)")
for encrypt, paramsDesc in encryptionTechniques:
    parser.add_argument(f"--{encrypt.__name__}", action='store_const', const=encrypt,  dest='encrypt',
                        help=f"selects '{encrypt.__name__}' as the encryption technique to use. (parameters: {paramsDesc})")

parser.add_argument('algoParam', nargs=argparse.REMAINDER)

args = parser.parse_args()

if not args.encrypt:
    parser.error('no encryption technique selected.')

try:
    main(inputPath=args.input,
         outputPath=args.output,
         encrypt=args.encrypt,
         algorithmParam=args.algoParam)
except Exception as ex:
    print('Exception Occured (common problem: make sure the algo param are correct):')
    print(ex)

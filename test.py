import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--extractor_size', nargs='+', type=int, default=[32],
                    help='hidden layer sizes in feature extractor/decoder')
args = parser.parse_args()
print('extrator_size', args.extractor_size)
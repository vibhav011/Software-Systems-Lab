import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("-in", "--input")
parser.add_argument("-out", "--output")
args = parser.parse_args()

with open(args.input, 'r') as f:
	absolute = f.read()

with open(args.output, 'w') as f:
	canon = os.path.realpath(absolute)
	f.write(canon)

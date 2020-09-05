import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("-in", required = True)
parser.add_argument("-out", required = True)
args = vars(parser.parse_args())

with open(args["in"], 'r') as f:
	absolute = f.read()

with open(args["out"], 'w') as f:
	canon = os.path.realpath(absolute)
	f.write(canon)

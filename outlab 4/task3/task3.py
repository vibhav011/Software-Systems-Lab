import argparse, scipy.cluster
from PIL import Image
import numpy as np

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--input', type=str, required=True)
my_parser.add_argument('--k', type=int, required=True)
my_parser.add_argument('--output', type=str, required=True)

args = vars(my_parser.parse_args())

# Reading the image
im = np.array(Image.open(args['input']), np.float)
data = np.reshape(im, (im.size//3, 3))

centroid, label = scipy.cluster.vq.kmeans2(data, int(args['k']), minit = '++')

final = np.uint8(np.reshape(centroid[label], im.shape))

# Saving the image
Image.fromarray(final).save(args['output'])
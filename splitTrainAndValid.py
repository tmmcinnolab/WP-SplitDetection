import random
import os
import subprocess
import sys
import argparse

parser = argparse.ArgumentParser(description='Object Detection using YOLO in OPENCV')
parser.add_argument('--name', help='Model name.')
parser.add_argument('--dir', help='Directory name.')
args = parser.parse_args()

def split_data_set(image_dir):

    f_val = open(args.name + "_valid.txt", 'w')
    f_train = open(args.name + "_train.txt", 'w')
    
    path, dirs, files = next(os.walk(image_dir))
    data_size = len(files)

    ind = 0
    data_test_size = int(0.1 * data_size)
    test_array = random.sample(range(data_size), k=data_test_size)

    for f in os.listdir(image_dir):
        name, ext = os.path.splitext(image_dir + '/' + f)
        if (ext == '.jpg' or ext == '.JPG'):
            ind += 1
				
            if ind in test_array:
                f_val.write('JPEG'+'/'+f+'\n')
            else:
                f_train.write('JPEG'+'/'+f+'\n')

print(sys.argv)
split_data_set(args.dir)

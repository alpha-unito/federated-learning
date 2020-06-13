import os
from os import listdir
from os.path import isfile, join
from shutil import copyfile, copy2, move
import random
from datetime import datetime
import math

TEST_PATH = '/media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train'
TOTAL_CLASSES = 1000

def merge_subset(path: str, destination_path) -> dict:
    """
    Move a PERCENTAGE of images from all classes to the destination path with all subfolders
    """

    subsets = listdir(path)

    for s in subsets:
        subset_path = join(path, s)
        classes = listdir(subset_path)
        
        for c in classes:
            class_path = join(subset_path, c)
            
            images_list = [f for f in listdir(class_path)
                            if isfile(join(class_path, f))]
            
            destination_sub_path = join(destination_path,c)
            os.mkdir(destination_sub_path)

            for im in images_list:
                image_path = join(class_path, im)
                print(image_path, destination_sub_path)
                move(image_path, destination_sub_path) # source, destination             
    

base_destination_path = TEST_PATH
new_directory = join(base_destination_path, 'merged')

try:
    os.mkdir(new_directory)
except OSError:
    raise OSError("Creation of the directory %s failed" % new_directory)

else:
    print ("Successfully created the directory %s " % new_directory)

#generate_subset(join(TEST_PATH, subset), 50, new_directory)
merge_subset(TEST_PATH, new_directory)

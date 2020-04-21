import os
from os import listdir
from os.path import isfile, join
from shutil import copyfile, copy2, move
import random
from datetime import datetime
import math

TEST_PATH = '/media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train'
TOTAL_CLASSES = 1000

def generate_random_test_subset(path: str, images_percentage, destination_path) -> dict:
    """
    Move a PERCENTAGE of images from all classes to the destination path with all subfolders
    """

    classes_directories = listdir(path)

    for im_class in classes_directories:
        source_sub_path = join(path, im_class)

        #images_list = listdir(source_sub_path)
        images_list = [f for f in listdir(source_sub_path)
                        if isfile(join(source_sub_path, f))]
        
        i = 0
        for i in range(len(images_list)):
            number = int(images_list[i].split('_')[1].replace('.JPEG', ''))
            images_list[i] = (number, images_list[i])

        images_list.sort()

        images_list = [i[1] for i in images_list]

        images_number = math.ceil(len(images_list) * (images_percentage / 100))

        print(f"Copyng {images_number}/{len(images_list)} images from {im_class}")

        destination_sub_path = join(destination_path, im_class)
        os.mkdir(destination_sub_path)
        
        for j in range(images_number):
            #pass
            print(f"    - Copying image number {j}: {images_list[j]}")
            move(join(source_sub_path, images_list[j]), destination_sub_path) # source, destination                
    

base_destination_path = '/media/lore/EA72A48772A459D9/ILSVRC2012/'
new_directory = join(base_destination_path, str(int(datetime.now().timestamp())))

try:
    os.mkdir(new_directory)
except OSError:
    raise OSError("Creation of the directory %s failed" % new_directory)

else:
    print ("Successfully created the directory %s " % new_directory)

generate_random_test_subset(TEST_PATH, 25, new_directory)

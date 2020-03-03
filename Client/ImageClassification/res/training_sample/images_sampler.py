import os
from os import listdir
from os.path import isfile, join
from shutil import copyfile, copy2
import random
from datetime import datetime

TEST_PATH = '/media/lore/6B6223601B584A05/IMAGENET/ILSVRC2012_img_train/'
TOTAL_CLASSES = 1000
TOTAL_IMAGES_FOR_CLASSES = 1300

def generate_random_test_subset(path: str, images_number, destination_path, classes_number = None) -> dict:
    """
    Copy random images from random classes to the destination path
    """

    if classes_number is None:
        classes_number = random.randint(1, images_number) # number of classes to pick

    random_classes =  random.sample(range(0, TOTAL_CLASSES - 1), classes_number)

    images_per_classes = int(images_number / classes_number)

    classes_directories = listdir(path)

    print(f"Copyng {images_number} images from {classes_number} classes.")

    for i in random_classes:
        print(f"Copying class {classes_directories[i]}")
        source_sub_path = join(path, classes_directories[i])
        destination_sub_path = join(destination_path, classes_directories[i])
        
        os.mkdir(destination_sub_path)
        
        images_list = listdir(source_sub_path)
        random_list = random.sample(range(0, min(len(images_list), TOTAL_IMAGES_FOR_CLASSES - 1)), images_per_classes)
        print(random_list)

        
        for j in random_list:
            print(f"    - Copying image number {j}: {images_list[j]}")
            copy2(join(source_sub_path, images_list[j]), destination_sub_path) # source, destination                
    

new_directory = join('./', str(int(datetime.now().timestamp())))

try:
    os.mkdir(new_directory)
except OSError:
    raise OSError("Creation of the directory %s failed" % new_directory)

else:
    print ("Successfully created the directory %s " % new_directory)

generate_random_test_subset(TEST_PATH, 100, new_directory, 10)

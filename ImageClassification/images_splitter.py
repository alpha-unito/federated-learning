import os
from os import listdir
from os.path import isfile, join
from shutil import copyfile, copy2, move
import random
from datetime import datetime
import math

SOURCE_PATH = '/media/lore/Data/ILSVRC2012/ILSVRC2012_img_train'
DESTINATION_PATH = '/media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train'
TOTAL_CLASSES = 1000

def generate_subset(path: str, images_percentage, destination_path) -> dict:
    """
    Move a PERCENTAGE of images from all classes to the destination path with all subfolders
    """

    classes_directories = listdir(path)

    for im_class in classes_directories:
        # images list
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

        # splitter
        images_number = math.ceil(len(images_list) * (images_percentage / 100))

        print(f"Copyng {images_number}/{len(images_list)} images from {im_class}")

        destination_sub_path = join(destination_path, im_class)
        os.mkdir(destination_sub_path)
        
        for j in range(images_number):
            #pass
            print(f"    - Moving image number {j}: {images_list[j]}")
            move(join(source_sub_path, images_list[j]), destination_sub_path) # source, destination                
    

def split_dataset(path: str, parts_number, destination_path) -> dict:
    
    classes_directories = listdir(path)

    """
    # create all directories
    for p in range(1, parts_number + 1):
        part_name = "subset{p:02d}".format(p=p)
        destination_part = join(destination_path, part_name)
        os.mkdir(destination_part)
    """

    class_index = 0
    # split all classes
    for im_class in classes_directories:
        
        if class_index <= 545:
            # images list
            source_sub_path = join(path, im_class)

            images_list = [f for f in listdir(source_sub_path)
                            if isfile(join(source_sub_path, f))]
            
            i = 0
            for i in range(len(images_list)):
                number = int(images_list[i].split('_')[1].replace('.JPEG', ''))
                images_list[i] = (number, images_list[i])

            images_list.sort()
            images_list = [i[1] for i in images_list]

            # splitter 
            total_images_number = len(images_list)   
            original_images_number = int(len(images_list) / parts_number)
            images_number = original_images_number
            
            """
            for p in range(1, parts_number+1):
                images_number = min(original_images_number, len(images_list))

                print(f"Copyng {images_number}/{total_images_number} images from {im_class}")
                part_name = "subset{p:02d}".format(p=p)
                destination_part = join(destination_path, part_name)
                destination_sub_path = join(destination_part, im_class)
                os.mkdir(destination_sub_path)
            
                for j in range(images_number):
                    #pass
                    print(f"    - Moving image number {j}: {images_list[j]}")
                    copy2(join(source_sub_path, images_list[j]), destination_sub_path) # source, destination                

                images_list = images_list[images_number:]
            """

            for p in range(1, parts_number):
                images_number = min(original_images_number, len(images_list))
                images_list = images_list[images_number:]

            images_number = min(original_images_number, len(images_list))
            part_name = "subset{p:02d}".format(p=parts_number)
            destination_part = join(destination_path, part_name)
            destination_sub_path = join(destination_part, im_class)
            os.mkdir(destination_sub_path)
            for j in range(images_number):
                #pass
                print(f"    - Moving image number {j}: {images_list[j]}")
                copy2(join(source_sub_path, images_list[j]), destination_sub_path) # source, destination                
    class_index += 1


new_directory = join(DESTINATION_PATH, str(int(datetime.now().timestamp())))
new_directory = join(DESTINATION_PATH, "1591300614")
"""
try:
    os.mkdir(new_directory)
except OSError:
    raise OSError("Creation of the directory %s failed" % new_directory)

else:
    print ("Successfully created the directory %s " % new_directory)
"""
#generate_subset(SOURCE_PATH, 50, new_directory)
split_dataset(SOURCE_PATH, 16, new_directory)

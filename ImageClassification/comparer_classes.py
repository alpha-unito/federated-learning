from os import listdir


SOURCE_PATH = '/media/lore/Data/ILSVRC2012/ILSVRC2012_img_train'
DESTINATION_PATH = '/media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/1591300614/subset01'

sources_classes = listdir(SOURCE_PATH)
destination_classes = listdir(DESTINATION_PATH)

for cs in sources_classes:
    if cs not in destination_classes:
        print(cs)

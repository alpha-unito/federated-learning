from __future__ import absolute_import, division, print_function, unicode_literals
from alex_net import alex_net
import tensorflow as tf
import numpy as np
from imagenet_classes import classes as in_classes

from keras.preprocessing.image import ImageDataGenerator
import keras

IMAGENET_PATH = '/media/lore/6B6223601B584A05/IMAGENET/'
# TOTAL_IMAGES = 1300 * 1000
TOTAL_IMAGES = 100
TARGET_SIZE = (224, 224)
BATCH_SIZE = 64
EPOCHS = 3
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

"""
def predict(model, x_val):
    test_generator.reset()
    pred=model.predict_generator(test_generator,
                                    steps=STEP_SIZE_TEST,
                                    verbose=1)
    predicted_class_indices=np.argmax(pred,axis=1)
    labels = (train_generator.class_indices)
    labels = dict((v,k) for k,v in labels.items())
    predictions = [labels[k] for k in predicted_class_indices]
"""

if __name__ == "__main__":
    # model = alex_net()
    model = keras.applications.mobilenet_v2.MobileNetV2()

    model.summary()

    # Compile the model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # create generator
    datagen = ImageDataGenerator()

    # prepare an iterators for each dataset
    # train_path = f'{IMAGENET_PATH}/ILSVRC2012_img_train/'
    train_path = "./res/training_sample/train"
    train_it = datagen.flow_from_directory(train_path,
                                           target_size=TARGET_SIZE,
                                           class_mode='categorical',
                                           color_mode='rgb',
                                           batch_size=BATCH_SIZE)

    """
    val_it = datagen.flow_from_directory(f'{IMAGENET_PATH}/ILSVRC2012_img_val/', 
                                            target_size=TARGET_SIZE,
                                            class_mode="categorical",
                                            color_mode="rgb",
                                            batch_size=BATCH_SIZE,
                                            shuffle=True,
                                            seed=42)
    
    test_it = datagen.flow_from_directory(f'{IMAGENET_PATH}/ILSVRC2012_img_test/',
                                            target_size=TARGET_SIZE,
                                            class_mode="categorical",
                                            color_mode="rgb",
                                            batch_size=BATCH_SIZE,
                                            shuffle=True,
                                            seed=42)
    
    # confirm the iterator works
    batchX, batchy = train_it.next()

    print(f'Batch x shape={batchX.shape}')
    print(f'Batch y shape={batchy.shape}')
    print('Batch y: ', batchy)
    """

    steps = 1
    parts = TOTAL_IMAGES / BATCH_SIZE
    if parts > 1:
        steps = parts
        if TOTAL_IMAGES % BATCH_SIZE > 0:
            steps += 1

    model.fit_generator(train_it, steps_per_epoch=steps, epochs=EPOCHS)

    # model.evaluate_generator(val_it, steps=24)

    # predict(model, training_set)

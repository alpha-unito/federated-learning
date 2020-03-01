from alex_net import alex_net
import tensorflow as tf
import numpy as np
from imagenet_classes import classes as in_classes
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from keras.preprocessing.image import ImageDataGenerator
import keras

from os import listdir
from os.path import isfile, join

IMAGENET_PATH = '/media/lore/6B6223601B584A05/IMAGENET/'
TOTAL_IMAGES = 1300 * 1000
TARGET_SIZE = (224, 224)
#BATCH_SIZE = 512
BATCH_SIZE = 64
EPOCHS = 1


def evaluate(model, x_test, y_test):
    # Evaluate the model on the test data using `evaluate`
    print('\n# Evaluate on test data')
    # results = model.evaluate(x_test, y_test, batch_size=128)
    
    results = model.evaluate_generator(test_it, steps=24)
    print('test loss, test acc:', results)


def predict(model, x_val):
    test_generator.reset()
    pred=model.predict_generator(test_generator,
                                    steps=STEP_SIZE_TEST,
                                    verbose=1)
    predicted_class_indices=np.argmax(pred,axis=1)
    labels = (train_generator.class_indices)
    labels = dict((v,k) for k,v in labels.items())
    predictions = [labels[k] for k in predicted_class_indices]

if __name__ == "__main__":
    
    # model = alex_net()
    # model = keras.applications.mobilenet_v2.MobileNetV2(input_shape=None, alpha=1.0, include_top=True, weights='imagenet', input_tensor=None, pooling=None, classes=1000)
    model = keras.applications.mobilenet_v2.MobileNetV2(classes=1000)
    model.summary()
    # Compile the model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # create generator
    """
    # construct the training image generator for data augmentation
    aug = ImageDataGenerator(rotation_range=20, zoom_range=0.15,
        width_shift_range=0.2, height_shift_range=0.2, shear_range=0.15,
        horizontal_flip=True, fill_mode="nearest")
    """
    datagen = ImageDataGenerator()
    

    # prepare an iterators for each dataset
    train_it = datagen.flow_from_directory(f'{IMAGENET_PATH}/ILSVRC2012_img_train/', 
                                            target_size=TARGET_SIZE, 
                                            class_mode='categorical', 
                                            color_mode='rgb', 
                                            batch_size = BATCH_SIZE)
    
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


    # steps = total_images / batch_size 
    # model.fit_generator(train_it, steps_per_epoch=2540, validation_data=val_it, validation_steps=8, epochs = EPOCHS)
    model.fit_generator(train_it, steps_per_epoch=(TOTAL_IMAGES / BATCH_SIZE), epochs = EPOCHS)


    # train(model, x_train, y_train)
    
    # evaluate(model, x_train, y_train)
    
    # predict(model, training_set)

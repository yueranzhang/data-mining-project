import numpy as np
from keras.layers import Conv2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import MaxPooling2D
from keras.models import Sequential
from keras.preprocessing import image

# create an object of the sequential class
classifier = Sequential()
# we added a convolution layer by using the “Conv2D” function.
classifier.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
# perform pooling operation to reduce the size of the images as much as possible
# We take a 2x2 matrix we’ll have minimum pixel loss and get a precise region where the feature are located
classifier.add(MaxPooling2D(pool_size=(2, 2)))
# convert all the pooled images into a continuous vector through Flattening
classifier.add(Flatten())
# hidden layer
classifier.add(Dense(units=128, activation='relu'))
# output layer, which should contain only one node
classifier.add(Dense(units=1, activation='sigmoid'))
# Optimizer parameter is to choose the stochastic gradient descent algorithm.
# Loss parameter is to choose the loss function.
# Finally, the metrics parameter is to choose the performance metric.
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# synthesising the training data
train_datagen = image.ImageDataGenerator(rescale=1. / 255,
                                         shear_range=0.2,
                                         zoom_range=0.2,
                                         horizontal_flip=True)
test_datagen = image.ImageDataGenerator(rescale=1. / 255)
training_set = train_datagen.flow_from_directory('training_set',
                                                 target_size=(64, 64),
                                                 batch_size=32,
                                                 class_mode='binary')
test_set = test_datagen.flow_from_directory('test_set',
                                            target_size=(64, 64),
                                            batch_size=32,
                                            class_mode='binary')
# fit the data to our model
classifier.fit_generator(training_set, steps_per_epoch=8000, epochs=25, validation_data=test_set, validation_steps=2000)
# Making new predictions from our trained model
test_image = image.load_img('test.jpg', target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
    prediction = 'cloth'
else:
    prediction = 'pants'
print(prediction)

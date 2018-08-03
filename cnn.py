from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Activation
from keras.layers import Conv2D, MaxPooling2D
from sklearn.model_selection import train_test_split
import os

#Creates the model for the initial training and performs it
def trainCNN(xtrain, xtest, ytrain, ytest, path):
    x_train, x_validation, y_train, y_validation = train_test_split(xtrain, ytrain, test_size = 0.2, random_state = 0)
    model = Sequential()
    model.add(Conv2D(32,(3,3), input_shape=(200,200,3)))
    model.add(Conv2D(32,(3,3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))
    model.add(Conv2D(64,(3,3)))
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(128))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(5))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
    model.fit(x_train, y_train,
           batch_size=32, nb_epoch=10, verbose=1, validation_data=(x_validation, y_validation))
    model.evaluate(xtest, ytest)
    saveModel(model, path)

# Saved the model as a result of the training
def saveModel(model, path):
    layers = model.layers
    first_dense_idx = [index for index, layer in enumerate(layers) if type(layer) is Dense][0]

    num_del = len(layers) - first_dense_idx
    for i in range(0, num_del):
        model.pop()
    for layer in model.layers:
        layer.trainable = False

    model.save(os.path.join(path,"model.h5"))
    model.summary()

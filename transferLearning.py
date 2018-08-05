from keras.layers import Dense, Dropout, Activation
from keras.models import load_model
from sklearn.model_selection import train_test_split
import os

# Creates the model for transfer learning and performs the training
def performTransferLearning(xtrain, xtest, ytrain, ytest, modelPath):
    x_train, x_validation, y_train, y_validation = train_test_split(xtrain, ytrain, test_size=0.2, random_state=0)
    model = load_model(os.path.join(modelPath, "model.h5"))
    model.add(Dense(128))
    model.add(Activation('relu', name='activation6'))
    model.add(Dropout(0.5, name= 'dropout4'))
    model.add(Dense(3))
    model.add(Activation('softmax', name='activation7'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam', metrics=['accuracy'])
    model.fit(x_train, y_train, validation_data=(x_validation, y_validation), epochs=30, batch_size=10)

    model.evaluate(xtest, ytest)
    # Save the model
    model.save(os.path.join(modelPath, "transferLearning.h5"))

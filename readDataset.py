import os
from PIL import Image
import numpy
from keras.utils import np_utils
from numpy import array

# Generates the train and test arrays.
def loadData(path, isModelInTrainingPhase):
    xtrain = []
    xtest = []
    ytrain = []
    ytest = []
    for folder in os.listdir(path):
        for subfolder in os.listdir(path + "/" +folder):
            subfolderPath = path + "/" + folder + "/" + subfolder
            if subfolder == "test":
                for image in os.listdir(subfolderPath):
                    if image.endswith(".jpg"):
                        imagePath = subfolderPath + "/" + image
                        img = Image.open(imagePath)
                        xtest.append(array(img))
                        ytest.append(folderTitleToInt(folder, isModelInTrainingPhase))
            elif subfolder == "train":
                for image in os.listdir(subfolderPath):
                    imagePath = subfolderPath + "/" + image
                    if image.endswith(".jpg"):
                        img = Image.open(imagePath)
                        xtrain.append(array(img))
                        ytrain.append(folderTitleToInt(folder, isModelInTrainingPhase))

    xtrain = numpy.asarray(xtrain)
    xtrain = (xtrain - xtrain.mean()) / xtrain.std()
    xtest = numpy.asarray(xtest)
    xtest = (xtest - xtest.mean()) / xtest.std()

    if isModelInTrainingPhase:
        ytrain = np_utils.to_categorical(ytrain, 5)
        ytest = np_utils.to_categorical(ytest, 5)
    else:
        ytrain = np_utils.to_categorical(ytrain, 3)
        ytest = np_utils.to_categorical(ytest, 3)

    return xtrain, xtest, ytrain, ytest

# Returns the class label as int
def folderTitleToInt(folder, isModelInTrainingPhase):
    if isModelInTrainingPhase == True:
        return fetchLabelsForTraining(folder)
    else:
        return fetchLabelsForTransferLearning(folder)

# Returns the class label as int for the initial training
def fetchLabelsForTraining(folder):
    if folder == "daisy":
        return 0
    elif folder == "dandelion":
        return 1
    elif folder == "rose":
        return 2
    elif folder == "sunflower":
        return 3
    elif folder == "tulip":
        return 4

# Returns the class label as int for the transfer learning
def fetchLabelsForTransferLearning(folder):
    if folder == "butterfly":
        return 0
    elif folder == "chandelier":
        return 1
    elif folder == "hawksbill":
        return 2

# for tensorflow use the input shape is (batch, height, width, channels) (Keras runs on Theano or Tensorflow)
# for theano is (batch, channels, height, width)










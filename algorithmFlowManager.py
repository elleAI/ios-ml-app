import readDataset
import cnn
import transferLearning
import convertToMLModel
import seperateDataset
import sys
import os

# Returns the absolute path of the current project folder
def getFolderPath():
    pathname = os.path.dirname(sys.argv[0])
    return os.path.abspath(pathname)

trainingDir = os.path.join(getFolderPath(), "datasets","trainDataset/")
transferLearningDir = os.path.join(getFolderPath(), "datasets","transferLearningDataset/")

# Performs the initial training
def performTrainingCNN():
    seperateDataset.createDatasetFolders(trainingDir)
    xtrain, xtest, ytrain, ytest = readDataset.loadData(trainingDir, True)
    modelPath = os.path.join(getFolderPath(), "models")
    cnn.trainCNN(xtrain, xtest, ytrain, ytest, modelPath)

# Performs the transfer Learning
def performTransferLearning():
    seperateDataset.createDatasetFolders(transferLearningDir)
    xtrain, xtest, ytrain, ytest = readDataset.loadData(transferLearningDir, False)
    modelPath = os.path.join(getFolderPath(), "models")
    transferLearning.performTransferLearning(xtrain, xtest, ytrain, ytest, modelPath)

# Saves the trained model to .mlmodel format
def saveCoreMLModel():
    convertToMLModel.convert(os.path.join(getFolderPath(), "models"))

# To start the whole process, call this function
def start():
    performTrainingCNN()
    performTransferLearning()
    saveCoreMLModel()

start()

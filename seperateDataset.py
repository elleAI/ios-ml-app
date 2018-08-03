import os
import shutil
from resizeDataset import resize

trainImages = []
testImages = []

# Creates train and test folders
def createDatasetFolders(folderPath):
    seperateImages(folderPath)
    for folder in os.listdir(folderPath):
            path = folderPath + "/" + folder
            if not os.path.exists(path + "/train"):
                os.makedirs(path + "/train")
            moveImages(folderPath, folder, "train", trainImages)
            if not os.path.exists(path + "/test"):
                os.makedirs(path + "/test")
            moveImages(folderPath, folder, "test", testImages)
    resize(folderPath)

# Separates the dataset to train and test images
def seperateImages(folderPath):
    for folder in os.listdir(folderPath):
        totalAmount = len((list(os.listdir(folderPath+"/"+folder))))
        testAmount = totalAmount * 20/100
        for image in os.listdir(folderPath + "/" + folder):
            if os.path.isfile(folderPath+"/"+folder + "/" + image):
                if totalAmount == testAmount:
                    testImages.append(image)
                else:
                    trainImages.append(image)
                    totalAmount -= 1

# Moves the train and test images to corresponding folders
def moveImages(basePath, folder, type, images):
    for image in images:
        source = basePath + folder + "/" + image
        destination = basePath + folder + "/" + type + "/" + image
        if os.path.exists(source):
            shutil.move(source, destination)
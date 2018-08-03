from PIL import Image
import os

# Resizes all of the images, train and test, to 200x200 dimensions
def resize(path):
    for folder in os.listdir(path):
        for subfolder in os.listdir(path +folder):
            for item in os.listdir(path+folder+ "/" + subfolder):
                 if item.endswith(".jpg"):
                    image = Image.open(path + folder + "/" + subfolder + "/" + item)
                    imResize = image.resize((200,200), Image.ANTIALIAS)
                    imResize.save(path + folder + "/" + subfolder + "/" + item, 'jpeg', quality=90)

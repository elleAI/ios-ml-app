# Create iOS Application Using Machine Learning

This project contains Convolutional Neural Network (CNN) model, trained with a dataset of flowers images.
Furthermore, this model was retrained with the technique of transfer learning for 3 new categories of images and converted to mlmodel that is connected with a simple iOS Application for testing out the results of the training.
For more in-depth explanation you can visit the [tutorial](https://pusher.com/tutorials/ios-machine-learning)

## Getting Started

To get you started you will need to clone this repository, by running

```
git clone https://github.com/elleAI/ios-ml-app.git

```
After cloning the project download the folder models from this [dropbox link](https://www.dropbox.com/sh/nbopbot03e5hr0o/AAAHeps1wOehKKGj6SK4ZGyTa?dl=0) and place it in the folder structure next to Datasets and the MachineLearningTutorial Folders.
This folder contains the trained models and also the mlmodel for the iOS Application.

Be sure to have all the prerequisites installed with correct versions and then run the script algorithmFlowManager.py, from more details visit the tutorial.

### Prerequisites

You will need to install the following:

- PyCharm (Commercial) 
- [Miniconda](https://conda.io/docs/user-guide/install/download.html)
- Python 2.7 - This will be automatically installed when miniconda or anaconda is installed
- [pip (10.0.1)](https://pip.pypa.io/en/stable/installing/)
- CORE ML Tools (0.8) - install with pip
- XCode (9.4.1)
- Keras (2.1.3) - install with pip

```
pip install library==version

example: `pip install keras==2.1.3`

```

## Built With

* [PyCharm](https://www.jetbrains.com/pycharm/download/) - IDE for creating the Machine Learning Part
* [XCode](https://developer.apple.com/xcode/) - IDE for creating the iOS Application

## Acknowledgments

* Transfer Learning Images - L. Fei-Fei, R. Fergus and P. Perona. Learning generative visual models
from few training examples: an incremental Bayesian approach tested on
101 object categories. IEEE. CVPR 2004, Workshop on Generative-Model
Based Vision. 2004

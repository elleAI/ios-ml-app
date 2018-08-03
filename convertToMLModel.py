import coremltools
from keras.models import load_model
import os

# Convertes the saved .h5 model from transfer learning to .mlmodel
def convert(path):
    model = load_model(os.path.join(path, "transferLearning.h5"))
    coreml_model = coremltools.converters.keras.convert(model,
                                                        class_labels=['butterfly','chandelier',
                                                                      'hawksbill'], input_names='input_1',
                                                        image_input_names = 'input_1')
    coreml_model.short_description = 'Model to classify category of images'
    coreml_model.save(os.path.join(path, "ObjectPredict.mlmodel"))
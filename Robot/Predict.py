from tensorflow.keras.preprocessing import image
import tensorflow as tf
import numpy as np
from robot.api.deco import keyword
import os
from robot.api import logger  # Import Robot Framework logger

MODEL = "cv-automation\models\image_multiclass_model.h5"
DIRECTORY = r"pictures/"
img_size = 250
class_indices = {'blue': 0, 'cyan': 1, 'faulty': 2, 'green': 3, 'orange': 4, 'pink': 5, 'red': 6, 'white': 7, 'yellow': 8}

def preprocess_img(img):
    img = image.load_img(img, target_size=(img_size, img_size))
    img_array = image.img_to_array(img)                              # converts image to Numpy array -> (250,250,3)
    img_array = img_array / 255.0                                    # normalization
    img_array = np.expand_dims(img_array, axis=0)                    # adds a batch dimension -> (1, 250, 250, 3)
    return img_array

def LoadModel(model_path):
    model = tf.keras.models.load_model(model_path, compile=False)
    print(f"Model Loaded: {model_path}")
    return model

def Predict(model, img, class_indices):
    try:
        img_arr = preprocess_img(img)
        prediction = model.predict(img_arr)                          # returns probabilities for each class (via softmax)
        prediction_index = np.argmax(prediction[0])                  # returns index of highest probability

        index_to_class = {v: k for k, v in class_indices.items()}    # do opp. mapping for index to colour e.g 0: 'blue' , …
        predicted_label = index_to_class[prediction_index]           # returns colour name

        # I actually don't really understand how this prediction works
        # confidence = prediction if prediction > 0.5 else 1 - prediction
        # print(f"Raw Prediction: {prediction}")
        # print(f"{prediction_class}--->{confidence * 100:.2f}%")
        return predicted_label 

    except Exception as e:
        print(f"Error loading model: {e}")
        model = None

@keyword("Predict Directory Green")
def PredictDirectoryGreen(model_path, directory):
    try:
        model = LoadModel(model_path)
        for files in os.listdir(os.path.join(directory)):
            img_path = os.path.join(directory, files)
            logger.info(f"Reading Image: {img_path}")
            print(f"Reading Image:{img_path}")
            result = Predict(model, img_path)
            logger.info(f"🔍 Prediction result: {result}")
            if result == "green":
                return "PASS"
            elif result == "faulty":
                logger.error(f"Test Failed: {result} is faulty.")
                return "FAIL"
            else:
                    # logger.info("All Images passed.")
                    logger.error(f"Unexpected result '{result}' for image: {img_path}")
                    return "FAIL"
            
    except Exception as e:
        logger.error(f"Exception occurred: {str(e)}")
        print(f"Error loading model or directory: {e}")
        return "FAIL"

@keyword("Predict Directory Red")
def PredictDirectoryRed(model_path, directory):
    try:
        model = LoadModel(model_path)
        for files in os.listdir(os.path.join(directory)):
            img_path = os.path.join(directory, files)
            print(f"Reading Image:{img_path}")
            result = Predict(model, img_path)
            if result == "red":
                return "PASS"
            elif result == "faulty":
                logger.error(f"Test Failed: {img_path} is faulty.")
                return "FAIL"
            else:
                    # logger.info("All Images passed.")
                    return "FAIL"
            
    except Exception as e:
        print(f"Error loading model or directory: {e}")
        return "FAIL"
    
@keyword("Predict Directory Pink")
def PredictDirectoryPink(model_path, directory):
    try:
        model = LoadModel(model_path)
        for files in os.listdir(os.path.join(directory)):
            img_path = os.path.join(directory, files)
            print(f"Reading Image:{img_path}")
            result = Predict(model, img_path)
            if result == "pink":
                return "PASS"
            elif result == "faulty":
                logger.error(f"Test Failed: {img_path} is faulty.")
                return "FAIL"
            else:
                    # logger.info("All Images passed.")
                    return "FAIL"
            
    except Exception as e:
        print(f"Error loading model or directory: {e}")
        return "FAIL"
    
@keyword("Predict Directory White")
def PredictDirectoryWhite(model_path, directory):
    try:
        model = LoadModel(model_path)
        for files in os.listdir(os.path.join(directory)):
            img_path = os.path.join(directory, files)
            print(f"Reading Image:{img_path}")
            result = Predict(model, img_path)
            if result == "white":
                return "PASS"
            elif result == "faulty":
                logger.error(f"Test Failed: {img_path} is faulty.")
                return "FAIL"
            else:
                    # logger.info("All Images passed.")
                    return "FAIL"
            
    except Exception as e:
        print(f"Error loading model or directory: {e}")
        return "FAIL"
    
@keyword("Predict Directory Cyan")
def PredictDirectoryCyan(model_path, directory):
    try:
        model = LoadModel(model_path)
        for files in os.listdir(os.path.join(directory)):
            img_path = os.path.join(directory, files)
            print(f"Reading Image:{img_path}")
            result = Predict(model, img_path)
            if result == "cyan":
                return "PASS"
            elif result == "faulty":
                logger.error(f"Test Failed: {img_path} is faulty.")
                return "FAIL"
            else:
                    # logger.info("All Images passed.")
                    return "FAIL"
            
    except Exception as e:
        print(f"Error loading model or directory: {e}")
        return "FAIL"
    
@keyword("Predict Directory Blue")
def PredictDirectoryBlue(model_path, directory):
    try:
        model = LoadModel(model_path)
        for files in os.listdir(os.path.join(directory)):
            img_path = os.path.join(directory, files)
            print(f"Reading Image:{img_path}")
            result = Predict(model, img_path)
            if result == "blue":
                return "PASS"
            elif result == "faulty":
                logger.error(f"Test Failed: {img_path} is faulty.")
                return "FAIL"
            else:
                    # logger.info("All Images passed.")
                    return "FAIL"
            
    except Exception as e:
        print(f"Error loading model or directory: {e}")
        return "FAIL"
    
@keyword("Predict Directory Orange")
def PredictDirectoryOrange(model_path, directory):
    try:
        model = LoadModel(model_path)
        for files in os.listdir(os.path.join(directory)):
            img_path = os.path.join(directory, files)
            print(f"Reading Image:{img_path}")
            result = Predict(model, img_path)
            if result == "orange":
                return "PASS"
            elif result == "faulty":
                logger.error(f"Test Failed: {img_path} is faulty.")
                return "FAIL"
            else:
                    # logger.info("All Images passed.")
                    return "FAIL"
            
    except Exception as e:
        print(f"Error loading model or directory: {e}")
        return "FAIL"
    
@keyword("Predict Directory Yellow")
def PredictDirectoryYellow(model_path, directory):
    try:
        model = LoadModel(model_path)
        for files in os.listdir(os.path.join(directory)):
            img_path = os.path.join(directory, files)
            print(f"Reading Image:{img_path}")
            result = Predict(model, img_path)
            if result == "yellow":
                return "PASS"
            elif result == "faulty":
                logger.error(f"Test Failed: {img_path} is faulty.")
                return "FAIL"
            else:
                    # logger.info("All Images passed.")
                    return "FAIL"
            
    except Exception as e:
        print(f"Error loading model or directory: {e}")
        return "FAIL"
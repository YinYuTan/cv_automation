from tensorflow.keras.preprocessing import image
import tensorflow as tf
import numpy as np
from robot.api.deco import keyword
import os
from robot.api import logger  # Import Robot Framework logger

script_dir = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(script_dir, '..', 'models', 'multiclass_img2_model_v11.h5')
MODEL_PATH = os.path.abspath(MODEL_PATH) 
# MODEL_PATH = "models/multiclass_img2_model_v11.h5"
# model = tf.keras.models.load_model(MODEL_PATH, compile=False)
# print(f"Model Loaded: {MODEL_PATH}")

img_size = 224
class_indices = {'blue': 0, 'cyan': 1, 'faulty': 2, 'green': 3, 'orange': 4, 'pink': 5, 'red': 6, 'white': 7, 'yellow': 8}

def preprocess_img(img):
    img = image.load_img(img, target_size=(img_size, img_size))
    img_array = image.img_to_array(img)                              # converts image to Numpy array -> (224,224,3)
    img_array = img_array / 255.0                                    # normalization
    img_array = np.expand_dims(img_array, axis=0)                    # adds a batch dimension -> (1, 224, 224, 3)
    return img_array

def LoadModel(MODEL_PATH):
    model = tf.keras.models.load_model(MODEL_PATH, compile=False)
    print(f"Model Loaded: {MODEL_PATH}")
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

@keyword("Log Embedded Image")
def log_embedded_image(image_path):
    import base64
    import os
    from robot.api import logger

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    with open(image_path, "rb") as img_file:
        ext = os.path.splitext(image_path)[1][1:].lower()
        encoded = base64.b64encode(img_file.read()).decode('utf-8')
        tag = f'<img src="data:image/{ext};base64,{encoded}" width="300"/>'
        logger.info(tag, html=True)


# @keyword("Predict Directory Colour")
# def PredictDirectoryColour(model_path, directory, expected_color):
#     try:
#         model = LoadModel(MODEL_PATH)
#         for files in os.listdir(os.path.join(directory)):
#             img_path = os.path.join(directory, files)
#             logger.info(f"Reading Image: {img_path}")
#             print(f"Reading Image:{img_path}")
#             result = Predict(img_path, class_indices)
#             logger.info(f"Prediction result: {result}")
#             if result == expected_color:
#                 return "PASS"
#             else:
#                     # logger.info("All Images passed.")
#                     logger.error(f"Unexpected result '{result}' for image: {img_path}")
#                     return "FAIL"
            
#     except Exception as e:
#         logger.error(f"Exception occurred: {str(e)}")
#         print(f"Error loading model or directory: {e}")
#         return "FAIL"

@keyword("Predict Directory Green")
def PredictDirectoryGreen(directory):
    try:
        model = LoadModel(MODEL_PATH)
        for files in os.listdir(os.path.join(directory)):
            img_path = os.path.join(directory, files)
            logger.info(f"Reading Image: {img_path}")
            print(f"Reading Image:{img_path}")
            result = Predict(model, img_path, class_indices)
            logger.info(f"Prediction result: {result}")
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
def PredictDirectoryRed(directory):
    try:
        model = LoadModel(MODEL_PATH)
        for files in os.listdir(os.path.join(directory)):
            img_path = os.path.join(directory, files)
            logger.info(f"Reading Image: {img_path}")
            print(f"Reading Image:{img_path}")
            result = Predict(model, img_path, class_indices)
            logger.info(f"Prediction result: {result}")
            if result == "red":
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
    
@keyword("Predict Directory Pink")
def PredictDirectoryPink(directory):
    try:
        model = LoadModel(MODEL_PATH)
        for files in os.listdir(os.path.join(directory)):
            img_path = os.path.join(directory, files)
            logger.info(f"Reading Image: {img_path}")
            print(f"Reading Image:{img_path}")
            result = Predict(model, img_path, class_indices)
            logger.info(f"Prediction result: {result}")
            if result == "pink":
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
    
@keyword("Predict Directory White")
def PredictDirectoryWhite(directory):
    try:
        model = LoadModel(MODEL_PATH)
        for files in os.listdir(os.path.join(directory)):
            img_path = os.path.join(directory, files)
            logger.info(f"Reading Image: {img_path}")
            print(f"Reading Image:{img_path}")
            result = Predict(model, img_path, class_indices)
            logger.info(f"Prediction result: {result}")
            if result == "white":
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
    
@keyword("Predict Directory Cyan")
def PredictDirectoryCyan(directory):
    try:
        model = LoadModel(MODEL_PATH)
        for files in os.listdir(os.path.join(directory)):
            img_path = os.path.join(directory, files)
            logger.info(f"Reading Image: {img_path}")
            print(f"Reading Image:{img_path}")
            result = Predict(model, img_path, class_indices)
            logger.info(f"Prediction result: {result}")
            if result == "cyan":
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
    
@keyword("Predict Directory Blue")
def PredictDirectoryBlue(directory):
    try:
        model = LoadModel(MODEL_PATH)
        for files in os.listdir(os.path.join(directory)):
            img_path = os.path.join(directory, files)
            logger.info(f"Reading Image: {img_path}")
            print(f"Reading Image:{img_path}")
            result = Predict(model, img_path, class_indices)
            logger.info(f"Prediction result: {result}")
            if result == "blue":
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
    
@keyword("Predict Directory Orange")
def PredictDirectoryOrange(directory):
    try:
        model = LoadModel(MODEL_PATH)
        for files in os.listdir(os.path.join(directory)):
            img_path = os.path.join(directory, files)
            logger.info(f"Reading Image: {img_path}")
            print(f"Reading Image:{img_path}")
            result = Predict(model, img_path, class_indices)
            logger.info(f"Prediction result: {result}")
            if result == "orange":
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
    
@keyword("Predict Directory Yellow")
def PredictDirectoryYellow(directory):
    try:
        model = LoadModel(MODEL_PATH)
        for files in os.listdir(os.path.join(directory)):
            img_path = os.path.join(directory, files)
            logger.info(f"Reading Image: {img_path}")
            print(f"Reading Image:{img_path}")
            result = Predict(model, img_path, class_indices)
            logger.info(f"Prediction result: {result}")
            if result == "yellow":
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
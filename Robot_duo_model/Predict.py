from tensorflow.keras.preprocessing import image
import tensorflow as tf
import numpy as np
from robot.api.deco import keyword
import os
from robot.api import logger  # Import Robot Framework logger

# MODEL = "cv-automation\models\multiclass_img2_model_v9.h5"
# DIRECTORY = r"pictures/"
img_size = 224
multiclass_indices = {'blue': 0, 'cyan': 1, 'green': 2, 'orange': 3, 'pink': 4, 'red': 5, 'white': 6, 'yellow': 7}
class_indices = {'clean': 0, 'faulty': 1}

def preprocess_img(img):
    img = image.load_img(img, target_size=(img_size, img_size))
    img_array = image.img_to_array(img)                              # converts image to Numpy array -> (224,224,3)
    img_array = img_array / 255.0                                    # normalization
    img_array = np.expand_dims(img_array, axis=0)                    # adds a batch dimension -> (1, 224, 224, 3)
    return img_array

def LoadModel(model_path):
    model = tf.keras.models.load_model(model_path, compile=False)
    print(f"Model Loaded: {model_path}")
    return model


def Predict(model, img, class_indices):
    try:
        img_arr = preprocess_img(img)
        prediction = model.predict(img_arr)

        if prediction.shape[1] == 1:
            # Binary case (sigmoid): prediction is a float like 0.91
            prob = float(prediction[0][0])
            prediction_label = int(prediction[0][0] > 0.5)
            logger.info(f"Raw prediction (sigmoid): {prob:.4f}")
        else:
            # Multiclass case (softmax): prediction is an array of class probs
            prediction_label = np.argmax(prediction[0])

        index_to_class = {v: k for k, v in class_indices.items()}
        predicted_label = index_to_class[prediction_label]

        return predicted_label

    except Exception as e:
        print(f"Error loading model: {e}")
        return None

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


@keyword("Predict Directory Colour")
def PredictDirectoryColour(model_path, directory, expected_color):
    try:
        model = LoadModel(model_path)
        for files in os.listdir(os.path.join(directory)):
            img_path = os.path.join(directory, files)
            logger.info(f"Reading Image: {img_path}")
            print(f"Reading Image:{img_path}")
            result = Predict(model, img_path, multiclass_indices)
            logger.info(f"Prediction result: {result}")
            if result == expected_color:
                return "PASS"
            else:
                    # logger.info("All Images passed.")
                    logger.error(f"Unexpected result '{result}' for image: {img_path}")
                    return "FAIL"
            
    except Exception as e:
        logger.error(f"Exception occurred: {str(e)}")
        print(f"Error loading model or directory: {e}")
        return "FAIL"


# @keyword("Predict Directory Green")
# def PredictDirectoryGreen(model_path, directory):
#     try:
#         model = LoadModel(model_path)
#         for files in os.listdir(os.path.join(directory)):
#             img_path = os.path.join(directory, files)
#             logger.info(f"Reading Image: {img_path}")
#             print(f"Reading Image:{img_path}")
#             result = Predict(model, img_path, multiclass_indices)
#             logger.info(f"Prediction result: {result}")
#             if result == "green":
#                 return "PASS"
#             else:
#                     # logger.info("All Images passed.")
#                     logger.error(f"Unexpected result '{result}' for image: {img_path}")
#                     return "FAIL"
            
#     except Exception as e:
#         logger.error(f"Exception occurred: {str(e)}")
#         print(f"Error loading model or directory: {e}")
#         return "FAIL"

# @keyword("Predict Directory Red")
# def PredictDirectoryRed(model_path, directory):
#     try:
#         model = LoadModel(model_path)
#         for files in os.listdir(os.path.join(directory)):
#             img_path = os.path.join(directory, files)
#             logger.info(f"Reading Image: {img_path}")
#             print(f"Reading Image:{img_path}")
#             result = Predict(model, img_path, multiclass_indices)
#             logger.info(f"Prediction result: {result}")
#             if result == "red":
#                 return "PASS"
#             else:
#                     # logger.info("All Images passed.")
#                     logger.error(f"Unexpected result '{result}' for image: {img_path}")
#                     return "FAIL"
            
#     except Exception as e:
#         logger.error(f"Exception occurred: {str(e)}")
#         print(f"Error loading model or directory: {e}")
#         return "FAIL"
    
# @keyword("Predict Directory Pink")
# def PredictDirectoryPink(model_path, directory):
#     try:
#         model = LoadModel(model_path)
#         for files in os.listdir(os.path.join(directory)):
#             img_path = os.path.join(directory, files)
#             logger.info(f"Reading Image: {img_path}")
#             print(f"Reading Image:{img_path}")
#             result = Predict(model, img_path, multiclass_indices)
#             logger.info(f"Prediction result: {result}")
#             if result == "pink":
#                 return "PASS"
#             else:
#                     # logger.info("All Images passed.")
#                     logger.error(f"Unexpected result '{result}' for image: {img_path}")
#                     return "FAIL"
            
#     except Exception as e:
#         logger.error(f"Exception occurred: {str(e)}")
#         print(f"Error loading model or directory: {e}")
#         return "FAIL"
    
# @keyword("Predict Directory White")
# def PredictDirectoryWhite(model_path, directory):
#     try:
#         model = LoadModel(model_path)
#         for files in os.listdir(os.path.join(directory)):
#             img_path = os.path.join(directory, files)
#             logger.info(f"Reading Image: {img_path}")
#             print(f"Reading Image:{img_path}")
#             result = Predict(model, img_path, multiclass_indices)
#             logger.info(f"Prediction result: {result}")
#             if result == "white":
#                 return "PASS"
#             else:
#                     # logger.info("All Images passed.")
#                     logger.error(f"Unexpected result '{result}' for image: {img_path}")
#                     return "FAIL"
            
#     except Exception as e:
#         logger.error(f"Exception occurred: {str(e)}")
#         print(f"Error loading model or directory: {e}")
#         return "FAIL"
    
# @keyword("Predict Directory Cyan")
# def PredictDirectoryCyan(model_path, directory):
#     try:
#         model = LoadModel(model_path)
#         for files in os.listdir(os.path.join(directory)):
#             img_path = os.path.join(directory, files)
#             logger.info(f"Reading Image: {img_path}")
#             print(f"Reading Image:{img_path}")
#             result = Predict(model, img_path, multiclass_indices)
#             logger.info(f"Prediction result: {result}")
#             if result == "cyan":
#                 return "PASS"
#             else:
#                     # logger.info("All Images passed.")
#                     logger.error(f"Unexpected result '{result}' for image: {img_path}")
#                     return "FAIL"
            
#     except Exception as e:
#         logger.error(f"Exception occurred: {str(e)}")
#         print(f"Error loading model or directory: {e}")
#         return "FAIL"
    
# @keyword("Predict Directory Blue")
# def PredictDirectoryBlue(model_path, directory):
#     try:
#         model = LoadModel(model_path)
#         for files in os.listdir(os.path.join(directory)):
#             img_path = os.path.join(directory, files)
#             logger.info(f"Reading Image: {img_path}")
#             print(f"Reading Image:{img_path}")
#             result = Predict(model, img_path, multiclass_indices)
#             logger.info(f"Prediction result: {result}")
#             if result == "blue":
#                 return "PASS"
#             else:
#                     # logger.info("All Images passed.")
#                     logger.error(f"Unexpected result '{result}' for image: {img_path}")
#                     return "FAIL"
            
#     except Exception as e:
#         logger.error(f"Exception occurred: {str(e)}")
#         print(f"Error loading model or directory: {e}")
#         return "FAIL"
    
# @keyword("Predict Directory Orange")
# def PredictDirectoryOrange(model_path, directory):
#     try:
#         model = LoadModel(model_path)
#         for files in os.listdir(os.path.join(directory)):
#             img_path = os.path.join(directory, files)
#             logger.info(f"Reading Image: {img_path}")
#             print(f"Reading Image:{img_path}")
#             result = Predict(model, img_path, multiclass_indices)
#             logger.info(f"Prediction result: {result}")
#             if result == "orange":
#                 return "PASS"
#             else:
#                     # logger.info("All Images passed.")
#                     logger.error(f"Unexpected result '{result}' for image: {img_path}")
#                     return "FAIL"
            
#     except Exception as e:
#         logger.error(f"Exception occurred: {str(e)}")
#         print(f"Error loading model or directory: {e}")
#         return "FAIL"
    
# @keyword("Predict Directory Yellow")
# def PredictDirectoryYellow(model_path, directory):
#     try:
#         model = LoadModel(model_path)
#         for files in os.listdir(os.path.join(directory)):
#             img_path = os.path.join(directory, files)
#             logger.info(f"Reading Image: {img_path}")
#             print(f"Reading Image:{img_path}")
#             result = Predict(model, img_path, multiclass_indices)
#             logger.info(f"Prediction result: {result}")
#             if result == "yellow":
#                 return "PASS"
#             else:
#                     # logger.info("All Images passed.")
#                     logger.error(f"Unexpected result '{result}' for image: {img_path}")
#                     return "FAIL"
            
#     except Exception as e:
#         logger.error(f"Exception occurred: {str(e)}")
#         print(f"Error loading model or directory: {e}")
#         return "FAIL"
    
@keyword("Predict Directory Faulty")
def PredictDirectoryFaulty(model_path, directory):
    try:
        model = LoadModel(model_path)
        for files in os.listdir(os.path.join(directory)):
            img_path = os.path.join(directory, files)
            logger.info(f"Reading Image: {img_path}")
            print(f"Reading Image:{img_path}")
            result = Predict(model, img_path, class_indices)
            logger.info(f"Prediction result: {result}")
            if result == "clean":
                return "PASS"
            else:
                    # logger.info("All Images passed.")
                    logger.error(f"Unexpected result '{result}' for image: {img_path}")
                    return "FAIL"
            
    except Exception as e:
        logger.error(f"Exception occurred: {str(e)}")
        print(f"Error loading model or directory: {e}")
        return "FAIL"
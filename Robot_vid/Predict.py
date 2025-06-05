from tensorflow.keras.preprocessing import image
import tensorflow as tf
import cv2
import numpy as np
from robot.api.deco import keyword
import os
from robot.api import logger  # Import Robot Framework logger

script_dir = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(script_dir, '..', 'models', 'video_recognition', 'video_model11.h5')
# MODEL_PATH = os.path.join(script_dir, '..', 'models', 'video_recognition', 'video_darkfaulty_model4.h5')
MODEL_PATH = os.path.abspath(MODEL_PATH) 
model = tf.keras.models.load_model(MODEL_PATH, compile=False)
# MODEL_PATH = "models/multiclass_img2_model_v11.h5"
# model = tf.keras.models.load_model(MODEL_PATH, compile=False)
# print(f"Model Loaded: {MODEL_PATH}")

img_size=160
target_size=(img_size, img_size)
frame_count = 300
class_indices = {'starlight': 0, 'wave': 1, 'spectrum_cycling': 2}
# class_indices = {'starlight': 0, 'wave': 1, 'spectrum_cycling': 2, 'faulty': 3}

def load_video_frames(video_path):
    cap = cv2.VideoCapture(str(video_path))
    frames = []
    while len(frames) < frame_count and cap.isOpened():
        ret, frame = cap.read()
        if not ret or frame is None:
            break
        frame = cv2.resize(frame, target_size)
        frame = frame.astype(np.float32)
        frame = frame / 255.0
        frames.append(frame)
    cap.release()
    if len(frames) < frame_count:
        pad_frame = np.zeros((target_size[1], target_size[0], 3), dtype=np.float32)
        frames += [pad_frame] * (frame_count - len(frames))
    elif len(frames) > frame_count:
        frames = frames[:frame_count]  # Trim if needed
    return np.array(frames, dtype=np.float32)

def Predict(model, vid, class_indices):
    try:
        vid_arr = load_video_frames(vid)
        input_tensor = np.expand_dims(vid_arr, axis=0)
        prediction = model.predict(input_tensor)[0]                 # returns probabilities for each class (via softmax)
        prediction_index = np.argmax(prediction)               # returns index of highest probability

        index_to_class = {v: k for k, v in class_indices.items()}    # do opp. mapping for index to colour e.g 0: 'blue' , …
        predicted_label = index_to_class[prediction_index]           # returns class name

        return predicted_label, prediction

    except Exception as e:
        print(f"Error loading model: {e}")
        model = None

@keyword("Log Embedded Frame")
def log_embedded_frame(video_path):
    import cv2
    import base64
    from robot.api import logger

    cap = cv2.VideoCapture(str(video_path))
    ret, frame = cap.read()
    cap.release()

    if not ret or frame is None:
        logger.warn(f"Could not read frame from video: {video_path}")
        return

    frame = cv2.resize(frame, (300, 200))

    # Encode frame to JPEG in memory
    ret, buf = cv2.imencode('.jpg', frame)
    if not ret:
        logger.warn("Failed to encode frame to JPEG")
        return

    b64 = base64.b64encode(buf.tobytes()).decode('utf-8')
    img_tag = f'<img src="data:image/jpeg;base64,{b64}" width="300"/>'
    logger.info("Showing first frame of video")

    logger.info(img_tag, html=True)

@keyword("Predict Directory Spectrum")
def PredictDirectorySpectrum(directory):
    try:
        for files in os.listdir(os.path.join(directory)):
            vid_path = os.path.join(directory, files)
            logger.info(f"Reading Video: {vid_path}")
            print(f"Reading Video:{vid_path}")

            # result = Predict(model, vid_path, class_indices)
            predicted_label, prediction_probs = Predict(model, vid_path, class_indices)

            if prediction_probs is not None:
                logger.info("Prediction probabilities:\n" +
                            np.array2string(prediction_probs, precision=4, suppress_small=True))

            logger.info(f"Prediction result: {predicted_label}")
            if predicted_label == "spectrum_cycling":
                return "PASS"
            elif predicted_label == "faulty":
                logger.error(f"Test Failed: {predicted_label} is faulty.")
                return "FAIL"
            else:
                    # logger.info("All Videos passed.")
                    logger.error(f"Unexpected result '{predicted_label}' for video: {vid_path}")
                    return "FAIL"
            
    except Exception as e:
        logger.error(f"Exception occurred: {str(e)}")
        print(f"Error loading model or directory: {e}")
        return "FAIL"
    
@keyword("Predict Directory Wave")
def PredictDirectoryWave(directory):
    try:
        for files in os.listdir(os.path.join(directory)):
            vid_path = os.path.join(directory, files)
            logger.info(f"Reading Video: {vid_path}")
            print(f"Reading Video:{vid_path}")

            # result = Predict(model, vid_path, class_indices)
            predicted_label, prediction_probs = Predict(model, vid_path, class_indices)

            if prediction_probs is not None:
                logger.info("Prediction probabilities:\n" +
                            np.array2string(prediction_probs, precision=4, suppress_small=True))

            logger.info(f"Prediction result: {predicted_label}")
            if predicted_label == "wave":
                return "PASS"
            elif predicted_label == "faulty":
                logger.error(f"Test Failed: {predicted_label} is faulty.")
                return "FAIL"
            else:
                    # logger.info("All Videos passed.")
                    logger.error(f"Unexpected result '{predicted_label}' for video: {vid_path}")
                    return "FAIL"
            
    except Exception as e:
        logger.error(f"Exception occurred: {str(e)}")
        print(f"Error loading model or directory: {e}")
        return "FAIL"
        
@keyword("Predict Directory Starlight")
def PredictDirectoryStarlight(directory):
    try:
        for files in os.listdir(os.path.join(directory)):
            vid_path = os.path.join(directory, files)
            logger.info(f"Reading Video: {vid_path}")
            print(f"Reading Video:{vid_path}")

            # result = Predict(model, vid_path, class_indices)
            predicted_label, prediction_probs = Predict(model, vid_path, class_indices)

            if prediction_probs is not None:
                logger.info("Prediction probabilities:\n" +
                            np.array2string(prediction_probs, precision=4, suppress_small=True))

            logger.info(f"Prediction result: {predicted_label}")
            if predicted_label == "starlight":
                return "PASS"
            elif predicted_label == "faulty":
                logger.error(f"Test Failed: {predicted_label} is faulty.")
                return "FAIL"
            else:
                    # logger.info("All Videos passed.")
                    logger.error(f"Unexpected result '{predicted_label}' for video: {vid_path}")
                    return "FAIL"
            
    except Exception as e:
        logger.error(f"Exception occurred: {str(e)}")
        print(f"Error loading model or directory: {e}")
        return "FAIL"

    #Previous
    # def preprocess_img(img):
    #     img = image.load_img(img, target_size=(img_size, img_size))
    #     img_array = image.img_to_array(img)                              # converts image to Numpy array -> (224,224,3)
    #     img_array = img_array / 255.0                                    # normalization
    #     img_array = np.expand_dims(img_array, axis=0)                    # adds a batch dimension -> (1, 224, 224, 3)
    #     return img_array
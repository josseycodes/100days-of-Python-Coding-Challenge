import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np

# Load the pre-trained MobileNetV2 model
model = MobileNetV2(weights='imagenet', include_top=True)

# Function to perform image recognition
def recognize_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224)) # MobileNetV2 expects images of size 224x224
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
 
    # Make predictions
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0] # Get top 3 predictions
    for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
        print("{}. {}: {:.2f}%".format(i + 1, label, score * 100))

# Example usage
image_path = 'example_image.jpg' # Path to your image
recognize_image(image_path)

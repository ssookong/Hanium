from keras.models import load_model
# Load the pre-trained model
model = load_model("Our_Model190.h5")

from keras.preprocessing.image import load_img, img_to_array
import numpy as np
from PIL import Image

# Load a new image
for i in range(1,4):
    image_path = 'data/picr'+str(i)+'.jpg'  # Replace with the actual path
    img = load_img(image_path, target_size=(300, 300))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    prediction = model.predict(img_array)
    print(prediction)
    # Interpret the prediction
    if prediction[0][0] > 0.5:
        result = "Full"
    else:
        result = "Empty"

    print("Prediction:", result)
    

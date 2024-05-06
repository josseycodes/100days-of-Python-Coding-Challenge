import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

# Define the path to your image dataset
dataset_path = 'path_to_your_dataset'

# Create an instance of the ImageDataGenerator class with augmentation parameters
datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Load an example image from the dataset
img = load_img('example_image.jpg')
x = img_to_array(img)
x = x.reshape((1,) + x.shape)

# Generate augmented images and save them to the specified directory
i = 0
for batch in datagen.flow(x, batch_size=1, save_to_dir='augmented_images', save_prefix='aug', save_format='jpg'):
    i += 1
    if i > 20:  # Generate 20 augmented images
        break

# Display one of the augmented images
augmented_img = load_img('augmented_images/aug_0_0.jpg')
plt.imshow(augmented_img)
plt.axis('off')
plt.show()

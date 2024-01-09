import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy.io import loadmat

# Load the original image
# image = Image.open('datasets/Data/test_data/hesam/images/mads_bottom_left_4_squares_2000.png')
image = Image.open('datasets/Data/test_data/images/IMG_918.jpg')
image = np.array(image)

# Load the prediction
data = loadmat('predictions/IMG_918.mat')
# data = loadmat('predictions/mads_bottom_left_4_squares_2000.mat')
estimation = data['estimation']

# Create an overlay of the prediction on the original image
overlay = image.copy()
overlay[estimation > 0] = [255, 0, 0]  # Change prediction areas to red

# Display the result
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(overlay)
plt.title('Image with Predictions')

plt.show()
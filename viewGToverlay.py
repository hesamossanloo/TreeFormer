from PIL import Image
from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np

# Load the original image
image = Image.open('datasets/Data/test_data/images/IMG_918.jpg')

# Load the gt and density map
density_map = np.load('datasets/Data/test_data/ground_truth/IMG_918_densitymap.npy')
print("DM: ", density_map)
gt_data = loadmat('datasets/Data/test_data/ground_truth/GT_IMG_918.mat')
tree_location = gt_data['image_info'][0][0][0][0][0]
print("TL: ",tree_location)

# Normalize the density map and ground truth locations
density_map = density_map / np.max(density_map)
tree_location = tree_location / np.max(tree_location)

# Display the original image
plt.imshow(image, cmap='gray')

# Overlay the density map
plt.imshow(density_map, cmap='jet', alpha=0.5)

# Overlay the ground truth locations
plt.scatter(tree_location[:, 1], tree_location[:, 0], s=10, c='white')

plt.show()

import numpy as np
from scipy.io import loadmat

# Load the ground truth and predicted density maps
ground_truth_density = np.load('datasets/Data/test_data/ground_truth/IMG_470_densitymap.npy')
predicted = loadmat('predictions/IMG_470.mat')
predicted_density = predicted['estimation']

# Calculate the Mean Squared Error
mse = np.mean((ground_truth_density - predicted_density) ** 2)

# Calculate the maximum possible MSE
max_mse = np.mean((ground_truth_density - np.max(ground_truth_density)) ** 2)

# Calculate the accuracy percentage
accuracy = (1 - mse / max_mse) * 100

print(f'Accuracy: {accuracy}%')
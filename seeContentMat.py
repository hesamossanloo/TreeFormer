from scipy.io import loadmat

# Load the .mat file
# data = loadmat('datasets/Data/test_data/ground_truth/GT_IMG_470.mat')
# data = loadmat('datasets/Data/test_data/ground_truth/IMG_470_densitymap.npy')
data = loadmat('predictions/IMG_158.mat')

# Print the data
# print(data['image_info'])
# print(data['gt'])
print(data['estimation'])
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits
import seaborn as sns

# Part a: Load the digits dataset
digits_data = load_digits()

# Part b: Create a DataFrame for pixel features
pixels_df = pd.DataFrame(digits_data.data)
digit_labels = digits_data.target  # Target labels

# Part c: Extract the first image row
first_image_row = pixels_df.iloc[0]

# Part d: Convert the first image row to a numpy array
first_image_array = first_image_row.to_numpy()

# Part e: Reshape the array into an 8x8 grid
first_image_grid = first_image_array.reshape(8, 8)

# Part f: Display the first digit image
plt.figure()
plt.imshow(first_image_grid, cmap='gray')  # cmap='gray' for grayscale images
plt.axis('off')  # Turn off axis
plt.title("First Digit Image")
plt.show()

# Part g: Scale the pixel data
scaler = StandardScaler()
scaled_pixels = scaler.fit_transform(pixels_df)

# Part h: Perform PCA with 2 components
pca_model = PCA(n_components=2)
pixels_pca_transformed = pca_model.fit_transform(scaled_pixels)

# Part i: Print explained variance by the PCA components
explained_variance_ratio = pca_model.explained_variance_ratio_
print(f"Explained variance by the first 2 components: {explained_variance_ratio}")
print(f"Total variance explained by 2 components: {np.sum(explained_variance_ratio):.2f}")

# Part j: Scatter plot of PCA-transformed data
plt.figure()
sns.scatterplot(
    x=pixels_pca_transformed[:, 0],
    y=pixels_pca_transformed[:, 1],
    hue=digit_labels,
    palette='tab10',
    s=100,
    marker='o',
    legend='full'
)
plt.title("PCA of Digits Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(title="Digit Label")
plt.show()

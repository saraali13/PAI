# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#column_names = ["id","diagnosis","radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"]

data = pd.read_csv("data.csv")

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)
kmeans=KMeans(n_clusters=2, init="k-means++")
kmeans.fit(data_scaled)
print(kmeans.inertia_)
SSE = []
for i in range(1, 20):
    kmeans = KMeans(n_clusters=i, init='k-means++')
    kmeans.fit(data_scaled)
    SSE.append(kmeans.inertia_)

plt.figure()
plt.plot(frame["Cluster"], frame["SSE"],marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of clusters')
plt.ylabel('Within-Cluster Sum of Squares')
plt.grid(True)
plt.show()

optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, init='k-means++', max_iter=300, n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(data_scaled)

data['Cluster'] = y_kmeans

plt.figure(figsize=(8,6))
plt.scatter(data_scaled[y_kmeans == 0, 0], data_scaled[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(data_scaled[y_kmeans == 1, 0], data_scaled[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(data_scaled[y_kmeans == 2, 0], data_scaled[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', marker='X', label='Centroids')

plt.title('K-Means Clustering (k=3)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)
plt.show()

print(data.head())

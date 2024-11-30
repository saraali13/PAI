from nltk import accuracy
from scipy.ndimage import label
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the heart disease dataset
df = pd.read_csv("heart.csv")
X = df.drop(columns=["target"])
y = df["target"]
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=8)

scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.fit_transform(X_test)

#n_range= range(1,251)
n_samples_train = len(X_train)
n_range = range(1, n_samples_train + 1)
accuracies=[]
for i in n_range:
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train_scaled, y_train)
    y_prediction = knn.predict(X_test_scaled)
    accuracies.append(accuracy_score(y_test, y_prediction))

best_neigh=n_range[accuracies.index(max(accuracies))]
worst_neigh=n_range[accuracies.index(min(accuracies))]

# Output the results
print("Best Neighbour: ",best_neigh)
print("Highest Accuracy: ", max(accuracies))
print("Worst neighbour: ",worst_neigh)
print("Lowest Accuracy: ", min(accuracies))

plt.figure()
plt.plot(n_range,accuracies ,label="Accuracy",color="g")
plt.legend()
plt.scatter([best_neigh],[max(accuracies)],label="Best Accuracy",marker="*")
plt.scatter([worst_neigh],[min(accuracies)],label="Worst Accuracy",marker="*")
plt.title("Heart Disease Prediction Accuracy vs Neighbours")
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")
plt.show()

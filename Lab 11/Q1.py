from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the heart disease dataset
df = pd.read_csv('heart.csv')

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=8)

haccuracy = -1
laccuracy = 1
hpred = None
lpred = None


for i in range(1, 251):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    # Update highest accuracy
    if accuracy > haccuracy:
        haccuracy = accuracy
        hpred = y_pred

    # Update lowest accuracy
    if accuracy < laccuracy:
        laccuracy = accuracy
        lpred = y_pred

# Output the results
print("Highest Accuracy: ", haccuracy)
print("Lowest Accuracy: ", laccuracy)
print("Predictions for Highest Accuracy: ", hpred)
print("Predictions for Lowest Accuracy: ", lpred)

# Changed plt.figimage to plt.figure to set the figure size.
plt.figure(figsize=(20, 5))
plt.title("Heart Disease Prediction")
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")
plt.plot(hpred, label="Highest Prediction")
plt.plot(lpred,  label="Highest Prediction")
plt.legend()
plt.show()

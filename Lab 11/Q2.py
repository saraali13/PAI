from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

# Load the heart disease dataset
df = pd.read_csv('heart.csv')
y = df.pop('target')

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=8)

haccuracy = -1
laccuracy = 1

for i in range(1, 11):
  X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=i)
  knn = KNeighborsClassifier(n_neighbors=i)
  knn.fit(X_train, y_train)
  y_pred = knn.predict(X_test)

  accuracy = accuracy_score(y_test, y_pred)
  print(accuracy," ")
  # Update highest accuracy
  if accuracy > haccuracy:
      haccuracy = accuracy

  # Update lowest accuracy
  if accuracy < laccuracy:
      laccuracy = accuracy


# Output the results
print("Highest Accuracy: ", haccuracy)
print("Lowest Accuracy: ", laccuracy)

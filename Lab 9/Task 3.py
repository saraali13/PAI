from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv("Iris.csv")
x = df["Species"]
y = df["PetalWidthCm"]
colors = {'Iris-setosa': 'red', 'Iris-versicolor': 'blue', 'Iris-virginica': 'green'}
plt.scatter(df['Species'], df['PetalWidthCm'], c=df['Species'].map(colors))

plt.show()

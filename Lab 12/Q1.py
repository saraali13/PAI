from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt

df = pd.read_csv('Iris.csv')
df = df.drop(columns=['SepalWidthCm', 'SepalLengthCm'])
print(df.head())

plt.scatter(df['PetalWidthCm'], df['PetalLengthCm'])
plt.show()

km = KMeans(n_clusters=3)

y_predicted = km.fit_predict(df[['PetalLengthCm', 'PetalWidthCm']])
print(y_predicted)

df['cluster'] = y_predicted
print(df.head())

df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]
df3 = df[df.cluster == 2]

plt.scatter(df1['PetalWidthCm'], df1['PetalLengthCm'], color = 'green')
plt.scatter(df2['PetalWidthCm'], df2['PetalLengthCm'], color = 'red')
plt.scatter(df3['PetalWidthCm'], df3['PetalLengthCm'], color = 'blue')

plt.xlabel('PetalLengthCm')
plt.ylabel('PetalWidthCm')

plt.legend()
plt.show()

scaler = MinMaxScaler()
scaler.fit(df[['PetalLengthCm']])
df[['PetalLengthCm']] = scaler.transform(df[['PetalLengthCm']])

scaler.fit(df[['PetalWidthCm']])
df[['PetalWidthCm']] = scaler.transform(df[['PetalWidthCm']])
print(df)

km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['PetalLengthCm', 'PetalWidthCm']])
print(y_predicted)

df['cluster'] = y_predicted
print(df)
print(km.cluster_centers_)

df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]
df3 = df[df.cluster == 2]

plt.scatter(df1['PetalWidthCm'], df1['PetalLengthCm'], color = 'green')
plt.scatter(df2['PetalWidthCm'], df2['PetalLengthCm'], color = 'red')
plt.scatter(df3['PetalWidthCm'], df3['PetalLengthCm'], color = 'blue')

plt.xlabel('PetalLengthCm')
plt.ylabel('PetalWidthCm')

plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], color = 'purple', label = 'centroid', marker = "+")

plt.legend()
plt.show()

k_rng = range(1, 10)
sse = []

for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df[['PetalWidthCm', 'PetalLengthCm']])
    sse.append(km.inertia_)

print(sse)

plt.xlabel('K')
plt.ylabel('Sum of sqaured errors')
plt.plot(k_rng, sse)
plt.show()

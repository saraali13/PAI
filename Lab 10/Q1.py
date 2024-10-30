import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("heart.csv")

plt.figure()
sns.histplot(data=df,x="fbs")
plt.show()

plt.figure()
sns.boxplot(x="fbs",y="age",data=df)
plt.show()

plt.figure()
sns.scatterplot(data=df,x="fbs",y="age")
plt.show()

plt.figure()
sns.lineplot(y=df["age"],x=df["fbs"])
plt.show()

plt.figure()
sns.displot(df)
plt.ylabel("fbs")
plt.show()

plt.figure()
sns.pairplot(df,hue="age")
plt.show()


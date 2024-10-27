import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Sea_Level.csv")

plt.scatter(df['Year'], df['SeaLevel'], marker='+', label="Sea Level Rise")
plt.xlabel("Year")
plt.ylabel("Sea Level")
plt.title("Sea Level Rise Over the Past 100 Years")
plt.legend()
plt.show()

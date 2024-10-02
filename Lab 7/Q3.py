import pandas as pd

df = pd.read_csv("heart.csv")
df["sex"] = df["sex"].replace({0: "male", 1: "female"})
df = df.rename(columns={"sex": "Gender"})

df.groupby('Gender').mean()

print((df['chol']).max())
print(df)

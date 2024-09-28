import pandas as pd

#CSV file is submitted on GCR
df=pd.read_csv("world_alcohol_consumption.csv")
new_df=df[(df["Year"]==1987)|(df["Year"]==1989)]

print(new_df)

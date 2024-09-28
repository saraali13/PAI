import pandas as pd

#XLSX file is submitted on GCR
df=pd.read_excel("employee.xlsx")
new_df=df[df["Year_Joined"]==2022]

print(new_df)
